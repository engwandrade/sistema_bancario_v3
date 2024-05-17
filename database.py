import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent
conexao = sqlite3.connect(ROOT_PATH / "database.sqlite3")
cursor = conexao.cursor()

def create_table(cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(100),
            email VARCHAR(150))""")
    conexao.commit()

def insert_data(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("""INSERT INTO clientes (nome, email) VALUES (?, ?)""", data)
    conexao.commit()

def insert_many(conexao, cursor, dados):
    cursor.executemany("""INSERT INTO clientes (nome, email) VALUES (?, ?)""", dados)
    conexao.commit()

def update_data(conexao, cursor, id, nome, email):
    data = (nome, email, id)
    cursor.execute("""UPDATE clientes SET nome=?, email=? WHERE id = ?""", data)
    conexao.commit()

def delete_data(conexao, cursor, id):
    data = (id,)
    cursor.execute("""DELETE FROM clientes WHERE id = ?""", data)
    conexao.commit()

def select_data(conexao, cursor):
    cursor.execute("""SELECT * FROM clientes""")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def retrieve_data(cursor, id):
    cursor.row_factory = sqlite3.Row
    cursor.execute("""SELECT * FROM clientes WHERE id = ?""", (id,))
    return cursor.fetchone()

def list_data(cursor):
    cursor.row_factory = sqlite3.Row
    cursor.execute("""SELECT * FROM clientes ORDER BY nome DESC""")
    return cursor.fetchall()

# Criando a tabela
create_table(cursor)

# Inserindo múltiplos dados
dados = [
    ("Rafaela", "rafa@gmail.com"),
    ("Wellington", "wela@gmail.com"),
    ("João", "joao@gmail.com"),
    ("Maria", "maria@gmail.com")
]
insert_many(conexao, cursor, dados)

# Atualizando dados (definindo o ID 2, por exemplo)
update_data(conexao, cursor, 2, "Rafaela", "rafa@icloud.com")

# Excluindo dados (por exemplo, excluindo o registro com ID 1)
delete_data(conexao, cursor, 1)

# Selecionando e imprimindo todos os dados
select_data(conexao, cursor)

# Recuperando e imprimindo um registro específico
cliente = retrieve_data(cursor, 2)
if cliente:
    print(dict(cliente))
    print(cliente["id"], cliente["nome"], cliente["email"])

# Listando e imprimindo todos os registros, ordenados pelo nome em ordem decrescente
clientes = list_data(cursor)
for cliente in clientes:
    print(dict(cliente))

# Fechando a conexão
conexao.close()
