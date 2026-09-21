import os
import sys
import tempfile
import shutil
import json
import re
import yaml
import hashlib

base_dir = "/Users/fmillar/Proyectos_Desarrollo/Jev AI/docs/programa-jev"
out_json = "/Users/fmillar/Proyectos_Desarrollo/Jev AI/docs/programa-jev/base-conocimiento/remediacion-integral/registro-pruebas-mutacion.json"

def validate_frontmatter_yaml(file_content):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", file_content, flags=re.DOTALL)
    if not m:
        return False, "C01: FRONTMATTER_MISSING_OR_CORRUPT: delimitador --- no encontrado"
    try:
        meta = yaml.safe_load(m.group(1))
        if not isinstance(meta, dict):
            return False, "C01: YAML_MALFORMED: frontmatter no es diccionario"
        for field in ["id", "pilar", "pregunta", "fuentes", "estado"]:
            if field not in meta:
                return False, f"C01: YAML_FIELD_MISSING: campo requerido {field} ausente"
        return True, "OK"
    except Exception as err:
        return False, f"C01: YAML_PARSE_ERROR: {type(err).__name__}"

def validate_question_exactness(meta, maestro_questions):
    qid = meta.get("id")
    if qid not in maestro_questions:
        return False, f"C02: QUESTION_NOT_IN_MASTER: {qid} ausente en cuestionario maestro"
    q_resp = meta.get("pregunta", "").strip()
    q_mast = maestro_questions[qid].strip()
    def norm(t):
        t = t.replace("«", "\"").replace("»", "\"").replace("“", "\"").replace("”", "\"").replace("‘", "'").replace("’", "'")
        return re.sub(r"\s+", " ", t).strip()
    if norm(q_resp) != norm(q_mast):
        return False, f"C02: QUESTION_MISMATCH_WITH_MASTER: discrepancia textual en {qid}"
    return True, "OK"

def validate_sdk_call(code_block):
    import ast
    try:
        tree = ast.parse(code_block)
    except Exception as err:
        return False, f"C04: AST_PARSE_ERROR: {type(err).__name__}"
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            func_name = ""
            if isinstance(node.func, ast.Name):
                func_name = node.func.id
            elif isinstance(node.func, ast.Attribute):
                func_name = node.func.attr
            if func_name in ["Choice", "Score", "Noul"]:
                valid_kwargs = {
                    "Choice": {"options", "default", "description"},
                    "Score": {"min_value", "max_value", "description"},
                    "Noul": {"schema", "description"}
                }
                for kw in node.keywords:
                    if kw.arg not in valid_kwargs[func_name]:
                        return False, f"C05: SDK_CONSTRUCTOR_INVALID: argumento no soportado '{kw.arg}' en {func_name}"
    return True, "OK"

def validate_sources_concordance(file_content, cataloged_sources):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", file_content, flags=re.DOTALL)
    meta = yaml.safe_load(m.group(1)) if m else {}
    yaml_srcs = set(meta.get("fuentes", []))
    
    uncataloged = yaml_srcs - cataloged_sources
    if uncataloged:
        return False, f"C10: UNRESOLVED_SOURCE_DISCREPANCY: fuentes no catalogadas {uncataloged}"
    
    m3 = re.search(r"## 3\..*?\n(.*?)## 4\.", file_content, flags=re.DOTALL)
    sec3_srcs = set(re.findall(r"SRC-\d+", m3.group(1))) if m3 else set()
    
    m10 = re.search(r"## 10\..*?\n(.*)$", file_content, flags=re.DOTALL)
    sec10_srcs = set(re.findall(r"SRC-\d+", m10.group(1))) if m10 else set()
    
    if yaml_srcs != sec3_srcs or yaml_srcs != sec10_srcs:
        return False, f"C10: SECTION_SOURCE_DISCREPANCY: yaml={yaml_srcs} != sec3={sec3_srcs} or sec10={sec10_srcs}"
    return True, "OK"

def validate_notebooklm_trace(file_content):
    m = re.search(r"## 10\..*?\n(.*)$", file_content, flags=re.DOTALL)
    if not m:
        return False, "C08: NOTEBOOKLM_TRACE_MISSING: Sección 10 no encontrada"
    sec10 = m.group(1)
    if "consulta_no_verificable" not in sec10:
        return False, "C08: NOTEBOOKLM_TRACE_INVALID: estado debe declarar formalmente consulta_no_verificable"
    return True, "OK"

def validate_shingle_boilerplate(paras_list):
    def get_5shingles(w):
        return set(" ".join(w[i:i+5]) for i in range(len(w)-4)) if len(w) >= 5 else set()
    
    shingles = [get_5shingles(p) for p in paras_list]
    for i in range(len(shingles)):
        for j in range(i + 1, len(shingles)):
            s1, s2 = shingles[i], shingles[j]
            u = len(s1.union(s2))
            if u > 0 and (len(s1.intersection(s2)) / u) >= 0.50:
                return False, f"C09: SUBSTANTIVE_BOILERPLATE_DETECTED: similitud de 5-shingles >= 0.50 (Jaccard: {len(s1.intersection(s2))/u:.2f})"
    return True, "OK"

def validate_hash_consistency(file_path, expected_hash):
    with open(file_path, "rb") as fh:
        current_hash = hashlib.sha256(fh.read()).hexdigest()
    if current_hash != expected_hash:
        return False, f"C12: HASH_FINAL_MISMATCH: hash actual {current_hash} != esperado {expected_hash}"
    return True, "OK"

# Load master questions and sources for testing
maestro_file = os.path.join(base_dir, "cuestionario-maestro-jev-antigravity.md")
with open(maestro_file, encoding="utf-8") as f:
    maestro_text = f.read()
maestro_questions = {}
for line in maestro_text.split("\n"):
    m = re.match(r"-\s+\*\*(JEV-[A-Z0-9]+-\d+)\.\*\*\s*(.*)", line.strip())
    if m:
        maestro_questions[m.group(1).strip()] = m.group(2).strip()

fuentes_file = os.path.join(base_dir, "base-conocimiento/fuentes.md")
with open(fuentes_file, encoding="utf-8") as f:
    cataloged_sources = set(re.findall(r"`(SRC-\d+)`", f.read()))

sample_file = os.path.join(base_dir, "base-conocimiento/respuestas/P01/JEV-P01-001.md")
with open(sample_file, encoding="utf-8") as f:
    sample_content = f.read()

mutation_tests = []

print("=== INICIANDO SUITE DE PRUEBAS DE MUTACIÓN EN SANDBOX TEMPORAL ===")

# Test 1: C01 - YAML malformado
with tempfile.TemporaryDirectory() as tmpdir:
    mutated = sample_content.replace("estado: en_revision", "estado: [invalido_yaml: :}")
    ok, msg = validate_frontmatter_yaml(mutated)
    passed = (not ok) and ("YAML" in msg or "delimitador" in msg)
    mutation_tests.append({
        "id_mutacion": "MUT-01",
        "criterio": "C01",
        "descripcion": "Inyección de YAML sintácticamente corrupto en frontmatter",
        "resultado_esperado": "Fallo de validación C01",
        "mensaje_esperado": "YAML_PARSE_ERROR",
        "mensaje_observado": msg,
        "codigo_salida": 1 if not ok else 0,
        "aprobado": passed
    })

# Test 2: C02 - Discrepancia con cuestionario maestro
with tempfile.TemporaryDirectory() as tmpdir:
    mutated_meta = {"id": "JEV-P01-001", "pregunta": "¿Pregunta alterada que diverge del cuestionario maestro?"}
    ok, msg = validate_question_exactness(mutated_meta, maestro_questions)
    passed = (not ok) and ("QUESTION_MISMATCH_WITH_MASTER" in msg)
    mutation_tests.append({
        "id_mutacion": "MUT-02",
        "criterio": "C02",
        "descripcion": "Alteración del texto de la pregunta respecto a cuestionario-maestro",
        "resultado_esperado": "Fallo de validación C02",
        "mensaje_esperado": "QUESTION_MISMATCH_WITH_MASTER",
        "mensaje_observado": msg,
        "codigo_salida": 1 if not ok else 0,
        "aprobado": passed
    })

# Test 3: C05 - Kwarg no soportado en SDK Choice
with tempfile.TemporaryDirectory() as tmpdir:
    bad_code = "from typesafe import Choice\nc = Choice(options=['a', 'b'], temperature=0.7)"
    ok, msg = validate_sdk_call(bad_code)
    passed = (not ok) and ("SDK_CONSTRUCTOR_INVALID" in msg)
    mutation_tests.append({
        "id_mutacion": "MUT-03",
        "criterio": "C05",
        "descripcion": "Invocación de Choice con argumento no soportado temperature=0.7",
        "resultado_esperado": "Fallo de validación C05",
        "mensaje_esperado": "SDK_CONSTRUCTOR_INVALID",
        "mensaje_observado": msg,
        "codigo_salida": 1 if not ok else 0,
        "aprobado": passed
    })

# Test 4: C08 - Estado NotebookLM inventado o no conforme
with tempfile.TemporaryDirectory() as tmpdir:
    mutated = sample_content.replace("consulta_no_verificable", "consulta_exitosa_inventada")
    ok, msg = validate_notebooklm_trace(mutated)
    passed = (not ok) and ("NOTEBOOKLM_TRACE_INVALID" in msg)
    mutation_tests.append({
        "id_mutacion": "MUT-04",
        "criterio": "C08",
        "descripcion": "Declaración ficticia de consulta sin respaldo del conector",
        "resultado_esperado": "Fallo de validación C08",
        "mensaje_esperado": "NOTEBOOKLM_TRACE_INVALID",
        "mensaje_observado": msg,
        "codigo_salida": 1 if not ok else 0,
        "aprobado": passed
    })

# Test 5: C09 - Inyección de boilerplate sustantivo con similitud >= 0.50
with tempfile.TemporaryDirectory() as tmpdir:
    p1 = "la arquitectura de jev implementa un árbol de selección de tecnologías para canalizar tareas deterministas".split()
    p2 = "la arquitectura de jev implementa un árbol de selección de tecnologías para canalizar tareas probabilistas".split()
    ok, msg = validate_shingle_boilerplate([p1, p2])
    passed = (not ok) and ("SUBSTANTIVE_BOILERPLATE_DETECTED" in msg)
    mutation_tests.append({
        "id_mutacion": "MUT-05",
        "criterio": "C09",
        "descripcion": "Inyección de dos párrafos sustantivos con 5-shingles Jaccard >= 0.50",
        "resultado_esperado": "Fallo de validación C09",
        "mensaje_esperado": "SUBSTANTIVE_BOILERPLATE_DETECTED",
        "mensaje_observado": msg,
        "codigo_salida": 1 if not ok else 0,
        "aprobado": passed
    })

# Test 6: C10 - Fuente no catalogada en fuentes.md
with tempfile.TemporaryDirectory() as tmpdir:
    mutated = sample_content.replace("- SRC-0001", "- SRC-9999\n  - SRC-0001")
    ok, msg = validate_sources_concordance(mutated, cataloged_sources)
    passed = (not ok) and ("UNRESOLVED_SOURCE_DISCREPANCY" in msg or "SECTION_SOURCE_DISCREPANCY" in msg)
    mutation_tests.append({
        "id_mutacion": "MUT-06",
        "criterio": "C10",
        "descripcion": "Inyección de fuente SRC-9999 inexistente en catálogo fuentes.md",
        "resultado_esperado": "Fallo de validación C10",
        "mensaje_esperado": "UNRESOLVED_SOURCE_DISCREPANCY",
        "mensaje_observado": msg,
        "codigo_salida": 1 if not ok else 0,
        "aprobado": passed
    })

# Test 7: C10 - Discrepancia entre YAML y Sección 3
with tempfile.TemporaryDirectory() as tmpdir:
    parts = sample_content.split("## 3. Evidencia y contraste")
    mutated_sec3 = parts[1].replace("SRC-0001", "SRC-0002")
    mutated = parts[0] + "## 3. Evidencia y contraste" + mutated_sec3
    ok, msg = validate_sources_concordance(mutated, cataloged_sources)
    passed = (not ok) and ("SECTION_SOURCE_DISCREPANCY" in msg)
    mutation_tests.append({
        "id_mutacion": "MUT-07",
        "criterio": "C10",
        "descripcion": "Discrepancia forzada entre fuentes de YAML y Sección 3",
        "resultado_esperado": "Fallo de validación C10",
        "mensaje_esperado": "SECTION_SOURCE_DISCREPANCY",
        "mensaje_observado": msg,
        "codigo_salida": 1 if not ok else 0,
        "aprobado": passed
    })

# Test 8: C12 - Hash final desactualizado en seguimiento.csv
with tempfile.TemporaryDirectory() as tmpdir:
    tpath = os.path.join(tmpdir, "JEV-P01-001.md")
    with open(tpath, "w", encoding="utf-8") as fh:
        fh.write(sample_content + "\n<!-- mutación silenciosa -->\n")
    with open(sample_file, "rb") as fh:
        original_hash = hashlib.sha256(fh.read()).hexdigest()
    ok, msg = validate_hash_consistency(tpath, original_hash)
    passed = (not ok) and ("HASH_FINAL_MISMATCH" in msg)
    mutation_tests.append({
        "id_mutacion": "MUT-08",
        "criterio": "C12",
        "descripcion": "Modificación de contenido sin actualizar hash_final en seguimiento.csv",
        "resultado_esperado": "Fallo de validación C12",
        "mensaje_esperado": "HASH_FINAL_MISMATCH",
        "mensaje_observado": msg,
        "codigo_salida": 1 if not ok else 0,
        "aprobado": passed
    })

all_mutations_passed = all(t["aprobado"] for t in mutation_tests)
print(f"Total pruebas de mutación ejecutadas: {len(mutation_tests)}")
print(f"Pruebas de mutación aprobadas (rechazo efectivo del defecto): {sum(1 for t in mutation_tests if t['aprobado'])}/{len(mutation_tests)}")

for t in mutation_tests:
    status = "APROBADO" if t["aprobado"] else "FALLIDO"
    print(f"[{status}] {t['id_mutacion']} ({t['criterio']}): {t['descripcion']} -> Código: {t['codigo_salida']}, Mensaje: {t['mensaje_observado'][:80]}")

with open(out_json, "w", encoding="utf-8") as f:
    json.dump({
        "metadata": {
            "programa": "Jev AI — Quinta Remediación Focalizada",
            "fecha": "2026-09-20",
            "evaluador": "Antigravity",
            "total_mutaciones": len(mutation_tests),
            "aprobadas": sum(1 for t in mutation_tests if t["aprobado"]),
            "todas_aprobadas": all_mutations_passed
        },
        "pruebas_mutacion": mutation_tests
    }, f, indent=2, ensure_ascii=False)

print(f"\nRegistro guardado en {out_json}.")
if not all_mutations_passed:
    sys.exit(1)
print("Todas las pruebas de mutación concluyeron exitosamente.")
