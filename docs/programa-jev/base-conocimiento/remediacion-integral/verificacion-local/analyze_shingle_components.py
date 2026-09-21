import os
import re
from collections import defaultdict
import json

base_dir = "/Users/fmillar/Proyectos_Desarrollo/Jev AI/docs/programa-jev/base-conocimiento/respuestas"

def normalize_text(text):
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
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
            paras = re.split(r"\n\s*\n", sec)
            for p_idx, p in enumerate(paras):
                p_clean = p.strip()
                if not p_clean or p_clean.startswith("#") or p_clean.startswith("|") or p_clean.startswith("```"):
                    continue
                norm = normalize_text(p_clean)
                words = norm.split()
                if len(words) >= 15:
                    shingles = get_5shingles(words)
                    paragraphs.append({
                        "qid": qid,
                        "sec_num": sec_num,
                        "p_idx": p_idx,
                        "raw": p_clean,
                        "words": words,
                        "shingles": shingles
                    })

shingle_index = defaultdict(list)
for idx, p in enumerate(paragraphs):
    for sh in p["shingles"]:
        shingle_index[sh].append(idx)

checked_pairs = set()
graph = defaultdict(set)
pairs = []

for idx1, p1 in enumerate(paragraphs):
    candidates = set()
    for sh in p1["shingles"]:
        for idx2 in shingle_index[sh]:
            if idx2 > idx1 and paragraphs[idx2]["qid"] != p1["qid"]:
                candidates.add(idx2)

    for idx2 in candidates:
        pair_key = (idx1, idx2)
        if pair_key in checked_pairs:
            continue
        checked_pairs.add(pair_key)
        p2 = paragraphs[idx2]
        s1 = p1["shingles"]
        s2 = p2["shingles"]
        inter = len(s1.intersection(s2))
        union = len(s1.union(s2))
        if union > 0:
            jaccard = inter / union
            if jaccard >= 0.50:
                pairs.append((idx1, idx2, jaccard))
                graph[idx1].add(idx2)
                graph[idx2].add(idx1)

visited = set()
components = []
for node in graph:
    if node not in visited:
        comp = []
        queue = [node]
        visited.add(node)
        while queue:
            curr = queue.pop(0)
            comp.append(curr)
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        components.append(comp)

components.sort(key=lambda c: len(c), reverse=True)
print(f"Total componentes conectados con Jaccard >= 0.50: {len(components)}")
for i, comp in enumerate(components):
    qids = set(paragraphs[idx]["qid"] for idx in comp)
    sec_nums = set(paragraphs[idx]["sec_num"] for idx in comp)
    sample_p = paragraphs[comp[0]]
    raw_sample = sample_p["raw"][:180].replace("\n", " ")
    print(f"Componente {i+1}: {len(comp)} párrafos en {len(qids)} archivos. Secciones: {sec_nums}")
    print(f"  Muestra: {raw_sample}\n")
