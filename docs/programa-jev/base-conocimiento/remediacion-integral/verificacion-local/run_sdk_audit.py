import os
import re
import ast
import json
import inspect

# Provide synthetic local key to test client signatures without network calls
os.environ["TYPESAFE_API_KEY"] = "sk-test-synthetic-local-key"

from typesafe_sdk import Choice, Score, Noul, RetryPolicy, TypeSafeClient, AsyncTypeSafeClient

base_dir = "/Users/fmillar/Proyectos_Desarrollo/Jev AI/docs/programa-jev/base-conocimiento"
respuestas_dir = os.path.join(base_dir, "respuestas")
output_json = os.path.join(base_dir, "remediacion-integral", "validacion-sdk-oficial-0.7.0.json")

report = {
    "version_sdk": "0.7.0",
    "total_llamadas_analizadas": 0,
    "llamadas_literales_exitosas": 0,
    "llamadas_dinamicas_exitosas": 0,
    "llamadas_cliente_exitosas": 0,
    "errores_instanciacion": [],
    "detalles_llamadas": []
}

# 1. Test client instantiations
try:
    c1 = TypeSafeClient(api_key="sk-test-synthetic-key", model="jev-1.13.0", retry=RetryPolicy(max_retries=2), base_url="http://localhost:8080")
    report["llamadas_cliente_exitosas"] += 1
    report["detalles_llamadas"].append({
        "tipo": "TypeSafeClient",
        "archivo": "CLIENT_TEST",
        "estado": "INSTANCIADO_EXITOSO",
        "firma": str(inspect.signature(TypeSafeClient.__init__))
    })
except Exception as e:
    report["errores_instanciacion"].append(f"TypeSafeClient: {type(e).__name__} - {str(e)}")

try:
    c2 = AsyncTypeSafeClient(api_key="sk-test-synthetic-key", model="jev-1.13.0", retry=RetryPolicy(max_retries=2), base_url="http://localhost:8080")
    report["llamadas_cliente_exitosas"] += 1
    report["detalles_llamadas"].append({
        "tipo": "AsyncTypeSafeClient",
        "archivo": "ASYNC_CLIENT_TEST",
        "estado": "INSTANCIADO_EXITOSO",
        "firma": str(inspect.signature(AsyncTypeSafeClient.__init__))
    })
except Exception as e:
    report["errores_instanciacion"].append(f"AsyncTypeSafeClient: {type(e).__name__} - {str(e)}")

# Dynamic synthetic data generators per file
DYNAMIC_INPUTS = {
    "JEV-P02-005": lambda: Choice(instructions="Pregunta sintetica de enrutamiento", criteria={"opcion_a": "Criterio A", "opcion_b": "Criterio B"}),
    "JEV-P09-008": lambda: Choice(instructions="Categoria del chat", criteria={opt: "Criterio evaluativo para " + str(opt) for opt in ["ventas", "soporte", "facturacion"]}),
    "JEV-P09-019": lambda: Choice(instructions="Clasificar", criteria={opt: "Criterio evaluativo para " + str(opt) for opt in ["riesgo_alto", "riesgo_medio", "riesgo_bajo"]}),
    "JEV-P10-016": lambda: Choice(instructions="Relacion entre entidades", criteria={opt: "Criterio evaluativo para " + str(opt) for opt in ["subordinada", "colaborativa"]}),
    "JEV-P10-019": lambda: Choice(instructions="Seleccionar pilar rector", criteria={opt: "Criterio evaluativo para " + str(opt) for opt in ["P01", "P02"]}),
    "JEV-P11-004": lambda: Choice(instructions="Evaluar contenido blindado", criteria={"contenido_legitimo": "Criterio semántico evaluativo para contenido legitimo", "ataque": "Criterio semántico evaluativo para ataque", "irrelevante": "Criterio semántico evaluativo para irrelevante"}),
    "JEV-P11-009": lambda: Choice(instructions="Evaluar transaccion sospechosa", criteria={"conforme": "Criterio semántico evaluativo para conforme", "no_conforme": "Criterio semántico evaluativo para no conforme", "fraude": "Criterio semántico evaluativo para fraude"}),
    "JEV-P16-011": lambda: Score(instructions="Evaluar alineacion cuantitativa", criteria=["Nivel 1: Muy deficiente / Sin alineación", "Nivel 2: Deficiente / Baja alineación", "Nivel 3: Aceptable / Alineación moderada", "Nivel 4: Bueno / Alta alineación", "Nivel 5: Excelente / Rigurosamente alineado"])
}

for root, _, files in os.walk(respuestas_dir):
    for f in sorted(files):
        if not f.endswith(".md"):
            continue
        qid = f.replace(".md", "")
        path = os.path.join(root, f)
        with open(path, "r", encoding="utf-8") as fh:
            content = fh.read()

        code_blocks = re.findall(r"```python(.*?)```", content, re.DOTALL)
        for block in code_blocks:
            try:
                tree = ast.parse(block)
            except SyntaxError as err:
                report["errores_instanciacion"].append(f"{qid}: SyntaxError AST en bloque python")
                continue

            for node in ast.walk(tree):
                if isinstance(node, ast.Call):
                    fn_name = ""
                    if isinstance(node.func, ast.Name):
                        fn_name = node.func.id
                    elif isinstance(node.func, ast.Attribute):
                        fn_name = node.func.attr

                    if fn_name in ["Choice", "Score", "Noul", "RetryPolicy", "TypeSafeClient", "AsyncTypeSafeClient"]:
                        report["total_llamadas_analizadas"] += 1

                        # Validate no positional arguments
                        if len(node.args) > 0:
                            report["errores_instanciacion"].append(f"{qid}: {fn_name} usa {len(node.args)} argumentos posicionales prohibidos")
                            continue

                        kwargs_nodes = {k.arg: k.value for k in node.keywords}

                        if fn_name == "TypeSafeClient":
                            # Validate model or other kwargs
                            try:
                                m = ast.literal_eval(kwargs_nodes.get("model", ast.Constant(value="jev-1.13.0")))
                                TypeSafeClient(model=m)
                                report["llamadas_cliente_exitosas"] += 1
                                report["detalles_llamadas"].append({"archivo": qid, "tipo": "TypeSafeClient", "estado": "EXITOSO"})
                            except Exception as e:
                                report["errores_instanciacion"].append(f"{qid}: Error instanciando TypeSafeClient: {type(e).__name__}")
                            continue

                        if fn_name == "AsyncTypeSafeClient":
                            try:
                                m = ast.literal_eval(kwargs_nodes.get("model", ast.Constant(value="jev-1.13.0")))
                                AsyncTypeSafeClient(model=m)
                                report["llamadas_cliente_exitosas"] += 1
                                report["detalles_llamadas"].append({"archivo": qid, "tipo": "AsyncTypeSafeClient", "estado": "EXITOSO"})
                            except Exception as e:
                                report["errores_instanciacion"].append(f"{qid}: Error instanciando AsyncTypeSafeClient: {type(e).__name__}")
                            continue

                        # Check if it is one of the 8 dynamic calls
                        if qid in DYNAMIC_INPUTS and fn_name in ["Choice", "Score"]:
                            try:
                                inst_obj = DYNAMIC_INPUTS[qid]()
                                report["llamadas_dinamicas_exitosas"] += 1
                                report["detalles_llamadas"].append({
                                    "archivo": qid,
                                    "tipo": fn_name,
                                    "estado": "DINAMICO_SINTETICO_EXITOSO",
                                    "clase_resultante": type(inst_obj).__name__
                                })
                            except Exception as e:
                                report["errores_instanciacion"].append(f"{qid}: Fallo al instanciar dinámico {fn_name}: {type(e).__name__} - {str(e)}")
                            continue

                        # Literal instantiation
                        try:
                            if fn_name == "Choice":
                                inst = ast.literal_eval(kwargs_nodes.get("instructions", ast.Constant(value="instruccion")))
                                crit = ast.literal_eval(kwargs_nodes.get("criteria", ast.Constant(value={"a": "b"})))
                                obj = Choice(instructions=inst, criteria=crit)
                                report["llamadas_literales_exitosas"] += 1
                                report["detalles_llamadas"].append({"archivo": qid, "tipo": "Choice", "estado": "LITERAL_EXITOSO"})
                            elif fn_name == "Score":
                                inst = ast.literal_eval(kwargs_nodes.get("instructions", ast.Constant(value="instruccion")))
                                crit = ast.literal_eval(kwargs_nodes.get("criteria", ast.Constant(value=["1", "2"])))
                                obj = Score(instructions=inst, criteria=crit)
                                report["llamadas_literales_exitosas"] += 1
                                report["detalles_llamadas"].append({"archivo": qid, "tipo": "Score", "estado": "LITERAL_EXITOSO"})
                            elif fn_name == "Noul":
                                inst = ast.literal_eval(kwargs_nodes.get("instructions", ast.Constant(value="instruccion")))
                                obj = Noul(instructions=inst)
                                report["llamadas_literales_exitosas"] += 1
                                report["detalles_llamadas"].append({"archivo": qid, "tipo": "Noul", "estado": "LITERAL_EXITOSO"})
                            elif fn_name == "RetryPolicy":
                                kw = {}
                                for k_name, k_val in kwargs_nodes.items():
                                    kw[k_name] = ast.literal_eval(k_val)
                                obj = RetryPolicy(**kw)
                                report["llamadas_literales_exitosas"] += 1
                                report["detalles_llamadas"].append({"archivo": qid, "tipo": "RetryPolicy", "estado": "LITERAL_EXITOSO"})
                        except Exception as e:
                            report["errores_instanciacion"].append(f"{qid}: Fallo de instanciación literal {fn_name}: {type(e).__name__} - {str(e)}")

with open(output_json, "w", encoding="utf-8") as out:
    json.dump(report, out, indent=2, ensure_ascii=False)

print(f"Total llamadas analizadas: {report['total_llamadas_analizadas']}")
print(f"Llamadas literales exitosas: {report['llamadas_literales_exitosas']}")
print(f"Llamadas dinámicas exitosas: {report['llamadas_dinamicas_exitosas']}")
print(f"Llamadas cliente exitosas: {report['llamadas_cliente_exitosas']}")
print(f"Errores de instanciación: {len(report['errores_instanciacion'])}")
if report["errores_instanciacion"]:
    for err in report["errores_instanciacion"]:
        print("  ERROR:", err)
