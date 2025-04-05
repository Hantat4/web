from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para almacenar las noticias
noticias = []

@app.route("/")
def index():
    return render_template("index.html", noticias=noticias)  # Pasa la lista de noticias a la plantilla

@app.route("/Sobre-la-page")
def sobre_la_page():
    return render_template("Sobre_la_page.html")

@app.route("/N-len")
def n_len():
    return render_template("N_len.html")

@app.route("/olim")
def olim():
    return render_template("olim.html")

@app.route("/title")
def title():
    return render_template("title.html")

@app.route("/procesar_noticia", methods=["POST"])
def procesar_noticia():
    titulo = request.form["titulo"]
    descripcion = request.form["descripcion"]
    imagen = request.files["imagen"]

    print(f"Título: {titulo}")
    print(f"Descripción: {descripcion}")

    if imagen:
        print(f"Imagen recibida: {imagen.filename}")

    # Si se sube una imagen, guardarla en la carpeta estática
    if imagen:
        imagen.save(f"static/img/{imagen.filename}")
        imagen_url = f"static/img/{imagen.filename}"
    else:
        imagen_url = None

    # Guardar la noticia en la lista
    noticia = {
        'titulo': titulo,
        'descripcion': descripcion,
        'imagen_url': imagen_url
    }
    noticias.append(noticia)

    # Redirigir a la página principal para mostrar la noticia
    return redirect(url_for('index'))

# Ruta para borrar una noticia
@app.route("/borrar_noticia/<int:index>", methods=["POST"])
def borrar_noticia(index):
    # Eliminar la noticia de la lista usando su índice
    if 0 <= index < len(noticias):
        noticias.pop(index)
    return redirect(url_for('index'))  # Redirige de nuevo a la página principal

if __name__ == "__main__":
    app.run(debug=True)
