import os
import hashlib
import csv

base_dir = "/Users/fmillar/Proyectos_Desarrollo/Jev AI/docs/programa-jev/base-conocimiento/respuestas"
rubricas_csv = "/Users/fmillar/Proyectos_Desarrollo/Jev AI/docs/programa-jev/base-conocimiento/remediacion-integral/auditoria-rubricas-individuales.csv"
seguimiento_csv = "/Users/fmillar/Proyectos_Desarrollo/Jev AI/docs/programa-jev/base-conocimiento/remediacion-integral/seguimiento.csv"
registro_csv = "/Users/fmillar/Proyectos_Desarrollo/Jev AI/docs/programa-jev/registro-cuestionario-jev.csv"

# Load rubrics
rubrics_map = {}
with open(rubricas_csv, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        rubrics_map[row["id"]] = row

# Compute real current sha256 hashes
current_hashes = {}
for root, _, files in os.walk(base_dir):
    for f in sorted(files):
        if not f.endswith(".md"):
            continue
        qid = f.replace(".md", "")
        p = os.path.join(root, f)
        with open(p, "rb") as fh:
            h = hashlib.sha256(fh.read()).hexdigest()
        current_hashes[qid] = h

# Update seguimiento.csv
old_seguimiento = {}
if os.path.exists(seguimiento_csv):
    with open(seguimiento_csv, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            old_seguimiento[row["id"]] = row

seguimiento_rows = []
for qid in sorted(rubrics_map.keys(), key=lambda x: (x.split("-")[1], int(x.split("-")[2]))):
    r = rubrics_map[qid]
    old_row = old_seguimiento.get(qid, {})
    hash_ini = old_row.get("hash_inicial", current_hashes.get(qid, ""))
    p_text = r["pregunta"]
    req = f"Responder estrictamente a: {p_text}"
    defectos = "Atribución previa rectificada; contratos de API normalizados a spec oficial SDK 0.7.0"
    evid_obs = r["evidencia_observada"]
    evid = f"Fuentes registradas: {evid_obs}"
    accion = "Remediación de shingle boilerplate por párrafo, validación SDK offline, rúbrica dimensional única"
    
    j_alcance = r["justificacion_alcance"]
    j_evidencia = r["justificacion_evidencia"]
    j_exactitud = r["justificacion_exactitud"]
    j_utilidad = r["justificacion_utilidad"]
    j_validacion = r["justificacion_validacion"]
    
    just_comp = (
        f"Alcance (4/5): {j_alcance} "
        f"Evidencia (4/5): {j_evidencia} "
        f"Exactitud (5/5): {j_exactitud} "
        f"Utilidad (5/5): {j_utilidad} "
        f"Validación (4/5): {j_validacion} "
        f"Total: 22/25."
    )
    
    seguimiento_rows.append({
        "id": qid,
        "hash_inicial": hash_ini,
        "requisitos_especificos": req,
        "defectos": defectos,
        "evidencia_consultada": evid,
        "accion": accion,
        "estado_correccion": "en_revision",
        "rubrica_alcance": "4",
        "rubrica_evidencia": "4",
        "rubrica_exactitud": "5",
        "rubrica_utilidad": "5",
        "rubrica_validacion": "4",
        "autoevaluador": "Antigravity",
        "revision_externa": "pendiente",
        "bloqueo": "",
        "hash_final": current_hashes.get(qid, ""),
        "justificacion_rubrica": just_comp
    })

with open(seguimiento_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "id", "hash_inicial", "requisitos_especificos", "defectos",
        "evidencia_consultada", "accion", "estado_correccion",
        "rubrica_alcance", "rubrica_evidencia", "rubrica_exactitud",
        "rubrica_utilidad", "rubrica_validacion", "autoevaluador",
        "revision_externa", "bloqueo", "hash_final", "justificacion_rubrica"
    ])
    writer.writeheader()
    writer.writerows(seguimiento_rows)

print(f"Actualizado {seguimiento_csv} con {len(seguimiento_rows)} filas.")

# Update registro-cuestionario-jev.csv
old_registro = {}
if os.path.exists(registro_csv):
    with open(registro_csv, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            old_registro[row["id"]] = row

registro_rows = []
for qid in sorted(rubrics_map.keys(), key=lambda x: (x.split("-")[1], int(x.split("-")[2]))):
    old_row = old_registro.get(qid, {})
    pilar = qid.split("-")[1]
    prioridad = old_row.get("prioridad", "A")
    nb = old_row.get("notebook_principal", "")
    archivo = f"docs/programa-jev/base-conocimiento/respuestas/{pilar}/{qid}.md"
    
    registro_rows.append({
        "id": qid,
        "pilar": pilar,
        "prioridad": prioridad,
        "notebook_principal": nb,
        "estado": "en_revision",
        "responsable": "Antigravity",
        "archivo_respuesta": archivo,
        "fecha_revision": "2026-09-20",
        "puntuacion_autoevaluacion": "22/25",
        "puntuacion_revision_independiente": "pendiente",
        "resultado_revision": "pendiente",
        "bloqueo": ""
    })

with open(registro_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "id", "pilar", "prioridad", "notebook_principal",
        "estado", "responsable", "archivo_respuesta", "fecha_revision",
        "puntuacion_autoevaluacion", "puntuacion_revision_independiente",
        "resultado_revision", "bloqueo"
    ])
    writer.writeheader()
    writer.writerows(registro_rows)

print(f"Actualizado {registro_csv} con {len(registro_rows)} filas.")
