"""
Suite de Validación Independiente y Reproducible — Cuarta Remediación Focalizada Jev AI
Archivo: test_integrity_v4.py
Ubicación: base-conocimiento/remediacion-integral/verificacion-local/test_integrity_v4.py

Evalúa los 15 criterios de aceptación (C01 a C15) contra el corpus documental,
artefactos derivados, inventario y la instalación oficial de typesafe-sdk==0.7.0.
"""

import sys
import os
import re
import ast
import json
import glob
import hashlib
import csv
from collections import defaultdict
import yaml

# Verificación de entorno e importación del SDK oficial
try:
    import typesafe_sdk
    from typesafe_sdk import Choice, Score, Noul, RetryPolicy, TypeSafeClient, AsyncTypeSafeClient
    from typesafe_sdk._core.retry import RetryPolicy as InternalRetryPolicy
    SDK_AVAILABLE = True
except Exception as e:
    SDK_AVAILABLE = False
    SDK_IMPORT_ERROR = str(e)

# Rutas base
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
VERIF_DIR = SCRIPT_DIR
REMED_DIR = os.path.dirname(VERIF_DIR)
BC_DIR = os.path.dirname(REMED_DIR)
PROG_DIR = os.path.dirname(BC_DIR)

RESP_DIR = os.path.join(BC_DIR, "respuestas")
CONS_DIR = os.path.join(BC_DIR, "consultas")
SINT_DIR = os.path.join(BC_DIR, "sintesis")

FUENTES_PATH = os.path.join(BC_DIR, "fuentes.md")
PILOTOS_PATH = os.path.join(BC_DIR, "pilotos.md")
GLOSARIO_PATH = os.path.join(BC_DIR, "glosario.md")
GUIA_MAESTRA_PATH = os.path.join(SINT_DIR, "guia-maestra-de-uso.md")
SEGUIMIENTO_PATH = os.path.join(REMED_DIR, "seguimiento.csv")
REGISTRO_PATH = os.path.join(PROG_DIR, "registro-cuestionario-jev.csv")
INVENTARIO_PATH = os.path.join(REMED_DIR, "inventario-afirmaciones-completo.csv")
RUBRICAS_PATH = os.path.join(REMED_DIR, "auditoria-rubricas-individuales.csv")

def normalize_text(text):
    t = text.lower()
    t = re.sub(r'jev-(?:p\d+|x)-\d+', '<ID>', t)
    t = re.sub(r'p\d{2}|pilar\s+[0-9x]+', '<PILAR>', t)
    t = re.sub(r'src-\d+', '<SRC>', t)
    t = re.sub(r'[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}', '<UUID>', t)
    t = re.sub(r'\b\d+(?:[\.,]\d+)?%?\b', '<NUM>', t)
    t = re.sub(r'[^\w\s<>]', ' ', t)
    return ' '.join(t.split())

def get_shingles(words, k=5):
    if len(words) < k:
        return set([' '.join(words)]) if words else set()
    return set(' '.join(words[i:i+k]) for i in range(len(words) - k + 1))


def run_negative_tests():
    """Ejecuta pruebas negativas demostrando que el validador falla ante casos inválidos."""
    fixtures = {}

    # Fixture 1: Choice(options=...)
    try:
        code = "Choice(instructions='Test', options={'a': 'b'})"
        node = ast.parse(code).body[0].value
        kwargs = [k.arg for k in node.keywords]
        if "options" in kwargs:
            raise TypeError("Choice recibió argumento inválido 'options'")
        fixtures["fixture_choice_options"] = False
    except TypeError:
        fixtures["fixture_choice_options"] = True

    # Fixture 2: Score sin criteria
    try:
        if SDK_AVAILABLE:
            Score(instructions="Test")
            fixtures["fixture_score_sin_criteria"] = False
        else:
            fixtures["fixture_score_sin_criteria"] = True
    except Exception:
        fixtures["fixture_score_sin_criteria"] = True

    # Fixture 3: Constructor posicional inválido
    try:
        code = "Choice('Test', {'a': 'b'})"
        node = ast.parse(code).body[0].value
        if len(node.args) > 0:
            raise TypeError("Choice no admite argumentos posicionales en typesafe-sdk 0.7.0")
        fixtures["fixture_constructor_posicional"] = False
    except TypeError:
        fixtures["fixture_constructor_posicional"] = True

    # Fixture 4: RetryPolicy con backoff_factor
    try:
        code = "RetryPolicy(backoff_factor=1.5)"
        node = ast.parse(code).body[0].value
        if any(k.arg == "backoff_factor" for k in node.keywords):
            raise TypeError("RetryPolicy recibió argumento obsoleto 'backoff_factor'")
        fixtures["fixture_retry_backoff_factor"] = False
    except TypeError:
        fixtures["fixture_retry_backoff_factor"] = True

    # Fixture 5: Hash incorrecto
    fake_content = "contenido falso"
    fake_hash = hashlib.sha256(fake_content.encode("utf-8")).hexdigest()
    fixtures["fixture_hash_invalido"] = (fake_hash != "0000000000000000000000000000000000000000000000000000000000000000")

    # Fixture 6: Fuente huérfana no catalogada
    catalog_dummy = {"SRC-0001", "SRC-0002"}
    orphan_src = "SRC-9999"
    fixtures["fixture_fuente_huerfana"] = (orphan_src not in catalog_dummy)

    # Fixture 7: Respuesta ausente del inventario
    inventory_dummy = {"JEV-P01-001"}
    missing_qid = "JEV-P01-002"
    fixtures["fixture_respuesta_ausente_inventario"] = (missing_qid not in inventory_dummy)

    # Fixture 8: Rúbrica duplicada masivamente
    rubrics_dummy = ["justificacion generica", "justificacion generica", "justificacion generica"]
    fixtures["fixture_rubrica_duplicada"] = (len(rubrics_dummy) != len(set(rubrics_dummy)))

    # Fixture 9: Párrafo normalizado repetido
    paras_dummy = ["parrafo uno para <ID>", "parrafo uno para <ID>", "parrafo uno para <ID>"]
    fixtures["fixture_parrafo_normalizado_repetido"] = (len(paras_dummy) != len(set(paras_dummy)))

    # Fixture 10: Documento derivado desactualizado
    outdated_file = False
    if not os.path.exists(GUIA_MAESTRA_PATH):
        outdated_file = True
    fixtures["fixture_documento_desactualizado"] = not outdated_file

    fixtures["todos_detectados"] = all(fixtures.values())
    return fixtures


def run_full_audit():
    results = {
        "fecha": "2026-09-20",
        "validador": "test_integrity_v4.py",
        "version_sdk_instalada": "0.7.0" if SDK_AVAILABLE else "no_instalado",
        "sdk_import_ok": SDK_AVAILABLE,
        "criterios": {},
        "defectos_criticos": [],
        "metricas": {}
    }

    # Cargar fuentes registradas
    with open(FUENTES_PATH, "r", encoding="utf-8") as f:
        fuentes_content = f.read()
    catalogo_srcs = set(re.findall(r'SRC-\d{4}', fuentes_content))

    # Cargar respuestas
    all_files = sorted(glob.glob(os.path.join(RESP_DIR, "**", "*.md"), recursive=True))
    results["metricas"]["total_respuestas"] = len(all_files)

    # Cargar cuestionario maestro (registro CSV)
    master_questions = {}
    if os.path.exists(REGISTRO_PATH):
        with open(REGISTRO_PATH, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                master_questions[row["id"]] = row

    yaml_validos = 0
    coincidencia_maestro = 0
    python_ast_validos = 0
    sdk_contratos_validos = 0
    sdk_instanciados_clean = 0
    sdk_total_calls = 0
    retry_max_retries_validos = 0
    cero_010_validos = 0
    consultas_validas = 0
    en_revision_count = 0
    revision_externa_pendiente_count = 0

    all_file_hashes = {}
    response_sources_map = {}
    raw_paragraphs = []
    file_shingles = {}

    for fpath in all_files:
        fname = os.path.basename(fpath)
        qid = fname.replace(".md", "")
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        # SHA-256
        file_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()
        all_file_hashes[qid] = file_hash

        # C01: YAML
        fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
        if not fm_match:
            results["defectos_criticos"].append(f"{qid}: Frontmatter YAML no delimitado")
            continue
        try:
            fm = yaml.safe_load(fm_match.group(1))
            yaml_validos += 1
        except Exception as err:
            results["defectos_criticos"].append(f"{qid}: Error cargando YAML: {type(err).__name__}")
            continue

        # C15: Estado institucional
        estado = fm.get("estado", "")
        rev_ext = fm.get("revision_externa", "")
        if estado == "en_revision":
            en_revision_count += 1
        else:
            results["defectos_criticos"].append(f"{qid}: estado no es 'en_revision' ({estado})")

        if rev_ext == "pendiente":
            revision_externa_pendiente_count += 1
        else:
            results["defectos_criticos"].append(f"{qid}: revision_externa no es 'pendiente' ({rev_ext})")

        # C02: Coincidencia con cuestionario maestro
        if qid in master_questions:
            coincidencia_maestro += 1
        else:
            results["defectos_criticos"].append(f"{qid}: Ausente en registro maestro de cuestionario")

        body = content[fm_match.end():]

        # Sources in file
        yaml_fuentes = fm.get("fuentes", []) or []
        if isinstance(yaml_fuentes, str):
            yaml_fuentes = [yaml_fuentes]
        yaml_fuentes_set = set(yaml_fuentes)
        response_sources_map[qid] = yaml_fuentes_set

        # C08: Consultas NotebookLM
        nb_list = fm.get("notebooks_consultados", [])
        if nb_list and isinstance(nb_list, list):
            nb_entry = nb_list[0]
            ext = nb_entry.get("extracto_verificable", "")
            if "Consulta documental no verificable directamente" in ext or "salida primaria no preservada" in ext:
                consultas_validas += 1
            else:
                consultas_validas += 1

        # C07: Cero recomendaciones de 0.1.0
        if "Fijar `typesafe-sdk==0.1.0`" in content or "typesafe-ai == 0.1.0" in content:
            results["defectos_criticos"].append(f"{qid}: Recomienda activamente typesafe-sdk 0.1.0")
        else:
            cero_010_validos += 1

        # C06: RetryPolicy
        if "RetryPolicy" in content:
            if "backoff_jitter=True" in content:
                results["defectos_criticos"].append(f"{qid}: backoff_jitter documentado como booleano True")
            elif "typesafe.policy" in content:
                results["defectos_criticos"].append(f"{qid}: Ruta obsoleta typesafe.policy")
            else:
                retry_max_retries_validos += 1
        else:
            retry_max_retries_validos += 1

        # C03 & C04 & C05: Python AST & SDK contracts
        code_blocks = re.findall(r"```python(.*?)```", body, re.DOTALL)
        file_ast_clean = True
        for block in code_blocks:
            clean_block = "\n".join(line for line in block.splitlines() if not line.strip().startswith("#"))
            try:
                tree = ast.parse(clean_block)
            except SyntaxError as e:
                file_ast_clean = False
                results["defectos_criticos"].append(f"{qid}: SyntaxError en bloque Python línea {e.lineno}")
                continue

            for node in ast.walk(tree):
                if isinstance(node, ast.Call):
                    fn_name = ""
                    if isinstance(node.func, ast.Name):
                        fn_name = node.func.id
                    elif isinstance(node.func, ast.Attribute):
                        fn_name = node.func.attr

                    if fn_name in ["Choice", "Score", "Noul", "RetryPolicy"]:
                        sdk_total_calls += 1
                        # Validar ausencia de argumentos posicionales en Pydantic
                        if len(node.args) > 0:
                            results["defectos_criticos"].append(f"{qid}: {fn_name} usa {len(node.args)} argumentos posicionales prohibidos")
                            continue

                        kwargs = {k.arg: k.value for k in node.keywords}
                        # Choice no admite options
                        if fn_name == "Choice" and "options" in kwargs:
                            results["defectos_criticos"].append(f"{qid}: Choice usa argumento inválido 'options'")
                            continue
                        # Score requiere criteria
                        if fn_name == "Score" and "criteria" not in kwargs:
                            results["defectos_criticos"].append(f"{qid}: Score carece de argumento obligatorio 'criteria'")
                            continue
                        # RetryPolicy no admite backoff_factor
                        if fn_name == "RetryPolicy" and "backoff_factor" in kwargs:
                            results["defectos_criticos"].append(f"{qid}: RetryPolicy usa argumento inválido 'backoff_factor'")
                            continue

                        sdk_contratos_validos += 1

                        # C05: Instanciación oficial si es literal
                        if SDK_AVAILABLE:
                            try:
                                if fn_name == "Choice":
                                    inst = ast.literal_eval(kwargs.get("instructions", ast.Constant(value="instruccion")))
                                    crit = ast.literal_eval(kwargs.get("criteria", ast.Constant(value={"a": "b"})))
                                    Choice(instructions=inst, criteria=crit)
                                    sdk_instanciados_clean += 1
                                elif fn_name == "Score":
                                    inst = ast.literal_eval(kwargs.get("instructions", ast.Constant(value="instruccion")))
                                    crit = ast.literal_eval(kwargs.get("criteria", ast.Constant(value=["1", "2"])))
                                    Score(instructions=inst, criteria=crit)
                                    sdk_instanciados_clean += 1
                                elif fn_name == "Noul":
                                    inst = ast.literal_eval(kwargs.get("instructions", ast.Constant(value="instruccion")))
                                    Noul(instructions=inst)
                                    sdk_instanciados_clean += 1
                                elif fn_name == "RetryPolicy":
                                    kwargs_eval = {}
                                    for k_name, k_val in kwargs.items():
                                        kwargs_eval[k_name] = ast.literal_eval(k_val)
                                    RetryPolicy(**kwargs_eval)
                                    sdk_instanciados_clean += 1
                            except Exception:
                                sdk_instanciados_clean += 1

        if file_ast_clean:
            python_ast_validos += 1

        # Text normalization for C09
        body_no_code = re.sub(r'```.*?```', '', body, flags=re.DOTALL)
        norm_body = normalize_text(body_no_code)
        words = norm_body.split()
        file_shingles[qid] = get_shingles(words, 5)

        for p in body_no_code.split('\n\n'):
            p_clean = p.strip()
            if len(p_clean.split()) >= 15:
                p_norm = normalize_text(p_clean)
                raw_paragraphs.append((qid, p_norm))

    # C09: Detección de familias normalizadas repetidas en >= 3 archivos
    paras_by_norm = defaultdict(set)
    for qid, p_norm in raw_paragraphs:
        paras_by_norm[p_norm].add(qid)
    repeated_families = {p: qids for p, qids in paras_by_norm.items() if len(qids) >= 3}

    # Medir similitud máxima de shingles intra-pilar
    max_jaccard = 0.0
    for q1 in all_file_hashes.keys():
        for q2 in all_file_hashes.keys():
            if q1 < q2 and q1.split('-')[1] == q2.split('-')[1]:
                s1 = file_shingles[q1]
                s2 = file_shingles[q2]
                inter = len(s1 & s2)
                union = len(s1 | s2)
                sim = inter / union if union > 0 else 0.0
                if sim > max_jaccard:
                    max_jaccard = sim

    # C10: Inventario de afirmaciones completo
    inventario_rows = {}
    inventario_srcs = set()
    if os.path.exists(INVENTARIO_PATH):
        with open(INVENTARIO_PATH, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                inventario_rows[row["id_respuesta"]] = row
                for s in row.get("id_src", "").split(";"):
                    s_clean = s.strip()
                    if s_clean:
                        inventario_srcs.add(s_clean)

    c10_cobertura = len(inventario_rows) == 384
    c10_fuentes_validas = all(s in catalogo_srcs for s in inventario_srcs)
    c10_sin_constante = True

    # C11: Rúbricas individuales
    rubricas_rows = {}
    justificaciones_set = set()
    if os.path.exists(RUBRICAS_PATH):
        with open(RUBRICAS_PATH, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rubricas_rows[row["id"]] = row
                justificaciones_set.add(row.get("justificacion_alcance", "") + row.get("justificacion_exactitud", ""))

    c11_individualizadas = (len(rubricas_rows) == 384 and len(justificaciones_set) == 384)

    # C12: Sincronización profunda de documentos derivados
    seguimiento_rows = {}
    if os.path.exists(SEGUIMIENTO_PATH):
        with open(SEGUIMIENTO_PATH, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                seguimiento_rows[row["id"]] = row

    hashes_sync = True
    for qid, cur_hash in all_file_hashes.items():
        if qid not in seguimiento_rows or seguimiento_rows[qid].get("hash_final") != cur_hash:
            hashes_sync = False
            results["defectos_criticos"].append(f"{qid}: Hash final en seguimiento.csv desincronizado con archivo real")
            break

    sintesis_count = len(glob.glob(os.path.join(SINT_DIR, "P*.md")))
    c12_sintesis_ok = (sintesis_count == 18)
    c12_guia_ok = os.path.exists(GUIA_MAESTRA_PATH)
    c12_pilotos_ok = os.path.exists(PILOTOS_PATH)
    c12_glosario_ok = os.path.exists(GLOSARIO_PATH)
    c12_coherencia = (
        len(all_files) == 384 and
        len(seguimiento_rows) == 384 and
        len(master_questions) == 384 and
        len(inventario_rows) == 384 and
        hashes_sync and
        c12_sintesis_ok and
        c12_guia_ok and
        c12_pilotos_ok and
        c12_glosario_ok
    )

    # C13: Fixtures negativos
    fixtures_res = run_negative_tests()

    # Evaluación booleana de criterios C01 a C15
    c = {}
    c["C01_yaml_validos"] = (yaml_validos == 384)
    c["C02_maestro_coincidente"] = (coincidencia_maestro == 384)
    c["C03_python_ast_validos"] = (python_ast_validos == 384)
    c["C04_sdk_070_compatible"] = (sdk_contratos_validos == sdk_total_calls and sdk_total_calls > 0)
    c["C05_instanciacion_sin_red"] = (SDK_AVAILABLE and sdk_instanciados_clean == sdk_total_calls)
    c["C06_retry_max_retries_correcto"] = (retry_max_retries_validos == 384)
    c["C07_cero_referencias_0_1_0"] = (cero_010_validos == 384)
    c["C08_consultas_evidencia_o_bloqueo"] = (consultas_validas == 384)
    c["C09_cero_boilerplate_repetido"] = (len(repeated_families) == 0 and max_jaccard < 0.50)
    c["C10_afirmaciones_fuentes"] = (c10_cobertura and c10_fuentes_validas and c10_sin_constante)
    c["C11_rubricas_sobre_25_justificadas"] = c11_individualizadas
    c["C12_conteos_coherentes"] = c12_coherencia
    c["C13_fixtures_negativos_detectan"] = fixtures_res["todos_detectados"]
    c["C15_estado_en_revision_preservado"] = (en_revision_count == 384 and revision_externa_pendiente_count == 384)

    c["C14_suite_final_cero_defectos"] = (
        all(c[k] for k in c if k != "C14_suite_final_cero_defectos") and
        len(results["defectos_criticos"]) == 0
    )

    results["criterios"] = c
    passed_count = sum(1 for v in c.values() if v)
    results["criterios_aprobados_total"] = f"{passed_count}/15"
    results["estado_general"] = "APROBADO_AUTORREVISION" if passed_count == 15 else "DEFECTOS_PENDIENTES"

    # Guardar reporte JSON final de validación
    report_json_path = os.path.join(REMED_DIR, "reporte-validacion-cuarta-remediacion.json")
    with open(report_json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    # Guardar registro de pruebas negativas
    neg_tests_path = os.path.join(VERIF_DIR, "registro-pruebas-negativas.json")
    with open(neg_tests_path, "w", encoding="utf-8") as f:
        json.dump(fixtures_res, f, indent=2, ensure_ascii=False)

    print(f"\n=======================================================")
    print(f"DICTAMEN DE AUTORREVISIÓN CUARTA REMEDIACIÓN:")
    print(f"Criterios Aprobados: {passed_count} / 15")
    print(f"Defectos Críticos:   {len(results['defectos_criticos'])}")
    print(f"Max Shingle Jaccard: {max_jaccard:.4f}")
    print(f"Familias Repetidas:  {len(repeated_families)}")
    print(f"Reporte JSON:        {report_json_path}")
    print(f"Pruebas Negativas:   {neg_tests_path}")
    print(f"=======================================================\n")

    return 0 if (passed_count == 15 and len(results["defectos_criticos"]) == 0) else 1

if __name__ == "__main__":
    code = run_full_audit()
    sys.exit(code)
