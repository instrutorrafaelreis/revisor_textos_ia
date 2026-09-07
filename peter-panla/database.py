import sqlite3
import os

DB_FILE = 'escola.db'

def init_db():
    # Remove existing db to start fresh for prototype
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
        
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Create Table
    cursor.execute('''
        CREATE TABLE alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            nota TEXT NOT NULL
        )
    ''')
    
    # Insert dummy data (all Fs)
    alunos = [
        ('Joao', 'F'),
        ('Maria', 'F'),
        ('Carlos', 'F'),
        ('Ana', 'F'),
        ('Pedro', 'F')
    ]
    cursor.executemany('INSERT INTO alunos (nome, nota) VALUES (?, ?)', alunos)
    
    conn.commit()
    conn.close()

def get_all_alunos():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT nome, nota FROM alunos')
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_nota(nome, nova_nota):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('UPDATE alunos SET nota = ? WHERE nome = ?', (nova_nota, nome))
    conn.commit()
    changes = conn.total_changes
    conn.close()
    return changes > 0

if __name__ == '__main__':
    init_db()
    print(get_all_alunos())
