from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Conexão MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",      # teu usuário do MySQL
    password="",      # tua senha do MySQL
    database="mybrothers"
)

cursor = db.cursor(dictionary=True)

# Página inicial - mostrar posts
@app.route('/')
def index():
    cursor.execute("SELECT * FROM posts ORDER BY data DESC")
    posts = cursor.fetchall()
    return render_template("index.html", posts=posts)

# Rota para postar
@app.route('/postar', methods=['POST'])
def postar():
    titulo = request.form['titulo']
    conteudo = request.form['conteudo']
    autor = request.form['autor']

    sql = "INSERT INTO posts (titulo, conteudo, autor) VALUES (%s, %s, %s)"
    values = (titulo, conteudo, autor)
    cursor.execute(sql, values)
    db.commit()

    return redirect('/')
    
if __name__ == "__main__":
    app.run(debug=True)
