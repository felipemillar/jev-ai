import os
import re
import json
import yaml

base_dir = "/Users/fmillar/Proyectos_Desarrollo/Jev AI/docs/programa-jev/base-conocimiento"
with open(os.path.join(base_dir, "remediacion-integral", "scratch_fuentes_parsed.json"), "r", encoding="utf-8") as f:
    sources = json.load(f)

test_file = os.path.join(base_dir, "respuestas", "P09", "JEV-P09-001.md")
with open(test_file, "r", encoding="utf-8") as f:
    content = f.read()

fm_m = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
fm = yaml.safe_load(fm_m.group(1))
qid = fm["id"]
pregunta = fm["pregunta"]
yaml_srcs = fm.get("fuentes", [])

print("QID:", qid)
print("Pregunta:", pregunta)
print("YAML sources:", yaml_srcs)
for s in yaml_srcs:
    s_info = sources.get(s, {})
    title = s_info.get("title", "")
    stype = s_info.get("type", "")
    print(f"  {s}: {title} ({stype})")
