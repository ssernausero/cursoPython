import json
from pathlib import Path

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
TAREAS_FILE = Path(app.root_path) / "tareas.json"


def cargar_tareas():
    try:
        with TAREAS_FILE.open(encoding="utf-8") as archivo:
            tareas_guardadas = json.load(archivo)
    except FileNotFoundError:
        return []

    if not isinstance(tareas_guardadas, list):
        raise TypeError(f"El archivo {TAREAS_FILE} debe contener una lista de tareas.")

    for tarea in tareas_guardadas:
        if (
            not isinstance(tarea, dict)
            or not isinstance(tarea.get("id"), int)
            or isinstance(tarea.get("id"), bool)
            or not isinstance(tarea.get("texto"), str)
            or not isinstance(tarea.get("hecho"), bool)
        ):
            raise TypeError(f"El archivo {TAREAS_FILE} contiene una tarea con formato inválido.")

    return tareas_guardadas


def guardar_tareas():
    TAREAS_FILE.write_text(
        json.dumps(tareas, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


tareas = cargar_tareas()
siguiente_id = max((tarea["id"] for tarea in tareas), default=0) + 1


@app.route("/")
def index():
    tareas_ordenadas = sorted(tareas, key=lambda tarea: tarea["hecho"])
    return render_template("index.html", tareas=tareas_ordenadas)


def agregar_tarea(texto):
    global siguiente_id

    tareas.append({"id": siguiente_id, "texto": texto, "hecho": False})
    siguiente_id += 1
    guardar_tareas()


def completar_tarea(id):
    for tarea in tareas:
        if tarea["id"] == id and not tarea["hecho"]:
            tarea["hecho"] = True
            guardar_tareas()
            break


@app.route("/agregar", methods=["POST"])
def agregar():
    texto_tarea = request.form.get("texto_tarea")
    if texto_tarea:
        agregar_tarea(texto_tarea)
    return redirect(url_for("index"))


@app.route("/completar/<int:id>")
def completar(id):
    completar_tarea(id)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
