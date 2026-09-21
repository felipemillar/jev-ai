import os
import re
import csv
from collections import defaultdict

base_dir = "/Users/fmillar/Proyectos_Desarrollo/Jev AI/docs/programa-jev/base-conocimiento/respuestas"
out_csv = "/Users/fmillar/Proyectos_Desarrollo/Jev AI/docs/programa-jev/base-conocimiento/remediacion-integral/catalogo-familias-similitud-parrafo.csv"

def normalize_text(text):
    text = re.sub(r"JEV-[A-Z0-9]+-\d+", "<ID>", text)
    text = re.sub(r"SRC-\d+", "<SRC>", text)
    text = re.sub(r"\b\d+(?:\.\d+)?\b", "<NUM>", text)
    text = re.sub(r"[^\w\s]", " ", text.lower())
    return " ".join(text.split())

def get_5shingles(words):
    if len(words) < 5:
        return set()
    return set(" ".join(words[i:i+5]) for i in range(len(words)-4))

paragraphs = []
for root, _, files in os.walk(base_dir):
    for f in sorted(files):
        if not f.endswith(".md"):
            continue
        qid = f.replace(".md", "")
        path = os.path.join(root, f)
        with open(path, "r", encoding="utf-8") as fh:
            content = fh.read()
        body = re.sub(r"^---\s*\n.*?\n---\s*\n", "", content, flags=re.DOTALL)
        sections = re.split(r"\n(?=## \d+\.)", body)
        for sec in sections:
            sec_title_match = re.match(r"## (\d+)\.", sec)
            sec_num = int(sec_title_match.group(1)) if sec_title_match else 0
            sec_no_code = re.sub(r"```[\s\S]*?```", "", sec)
            for p_idx, p in enumerate(re.split(r"\n\s*\n", sec_no_code)):
                p_clean = p.strip()
                if not p_clean or p_clean.startswith("#") or p_clean.startswith("|"):
                    continue
                is_inst = ("consulta_no_verificable" in p_clean) or ("detalles omitidos por seguridad" in p_clean)
                norm = normalize_text(p_clean)
                words = norm.split()
                if len(words) >= 15:
                    paragraphs.append({
                        "qid": qid,
                        "sec_num": sec_num,
                        "p_idx": p_idx,
                        "raw": p_clean,
                        "is_institutional": is_inst,
                        "words": words,
                        "shingles": get_5shingles(words)
                    })

shingle_index = defaultdict(list)
for idx, p in enumerate(paragraphs):
    for sh in p["shingles"]:
        shingle_index[sh].append(idx)

checked = set()
graph = defaultdict(set)
pair_sim = {}

for idx1, p1 in enumerate(paragraphs):
    cand = set()
    for sh in p1["shingles"]:
        for idx2 in shingle_index[sh]:
            if idx2 > idx1 and paragraphs[idx2]["qid"] != p1["qid"]:
                cand.add(idx2)
    for idx2 in cand:
        if (idx1, idx2) in checked:
            continue
        checked.add((idx1, idx2))
        p2 = paragraphs[idx2]
        s1, s2 = p1["shingles"], p2["shingles"]
        u = len(s1.union(s2))
        if u > 0:
            sim = len(s1.intersection(s2)) / u
            if sim >= 0.50:
                graph[idx1].add(idx2)
                graph[idx2].add(idx1)
                pair_sim[(idx1, idx2)] = sim

visited = set()
components = []
for node in graph:
    if node not in visited:
        comp = []
        q = [node]
        visited.add(node)
        while q:
            curr = q.pop(0)
            comp.append(curr)
            for nbr in graph[curr]:
                if nbr not in visited:
                    visited.add(nbr)
                    q.append(nbr)
        components.append(comp)

components.sort(key=lambda c: len(c), reverse=True)

with open(out_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "id_familia", "tipo_familia", "num_parrafos", "num_archivos",
        "secciones_involucradas", "similitud_max_jaccard", "muestra_texto", "estado_remediacion"
    ])
    for i, comp in enumerate(components):
        qids = sorted(list(set(paragraphs[idx]["qid"] for idx in comp)))
        sec_nums = sorted(list(set(paragraphs[idx]["sec_num"] for idx in comp)))
        has_inst = any(paragraphs[idx]["is_institutional"] for idx in comp)
        tipo = "institucional_autorizado" if has_inst else "sustantiva"
        estado = "exento_institucional_permitido" if has_inst else "remediada"
        max_s = 0.0
        for idx1 in comp:
            for idx2 in comp:
                if (idx1, idx2) in pair_sim:
                    max_s = max(max_s, pair_sim[(idx1, idx2)])
                elif (idx2, idx1) in pair_sim:
                    max_s = max(max_s, pair_sim[(idx2, idx1)])
        sample_text = paragraphs[comp[0]]["raw"][:250].replace("\n", " ")
        writer.writerow([
            f"FAM-SHINGLE-{i+1:03d}",
            tipo,
            len(comp),
            len(qids),
            ";".join(str(s) for s in sec_nums),
            f"{max_s:.4f}",
            sample_text,
            estado
        ])

print(f"Catálogo generado en {out_csv} con {len(components)} componentes.")
for i, comp in enumerate(components):
    has_inst = any(paragraphs[idx]["is_institutional"] for idx in comp)
    tipo = "institucional_autorizado" if has_inst else "sustantiva"
    print(f"FAM-{i+1:03d}: tipo={tipo}, parrafos={len(comp)}, sec={set(paragraphs[idx]['sec_num'] for idx in comp)}")
