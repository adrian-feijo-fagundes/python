import sqlite3

def conectar():
    return sqlite3.connect("teste.db")


def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()


def adicionar_tarefa(descricao):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO tarefas (descricao) VALUES (?)", descricao
    )

    conexao.commit()
    conexao.close()


def listar_tarefas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM tarefas")

    tarefas = cursor.fetchall()

    conexao.close()

    return tarefas