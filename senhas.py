import sqlite3


conn = sqlite3.connect('senhas.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
''')

def menu():
    print('f pra inserir nova senha: ')
    print('L pra listar: ')
    print('r pra recuperar: ')
    print('s pra sair: ')

def get_password(service):
    cursor.execute(f'''
    SELECT (username, password) FROM users
    WHERE service = '{service}')
''')

    if cursor.rowcount == 0:
        print('serviço não cadastrado (use L para verificar os serviços')

    else:
        for user in cursor.fetchall():
            print(user)


def insert_password(service, username, password):
    cursor.execute(f'''
    INSERT INTO users (service, username, password)
    VALUES ('{service}','{username}','{password}')
    ''')
    conn.commit()

def show_service():
    cursor.execute('''
    SELECT service FROM users;
    ''')

    for service in cursor.fetchall():
        print(service)

while True:

    menu()
    
    opção = input(str('o que deseja fazer: ')).upper()

    if opção not in ['F','L','R','S']:
        print('\nOpção inválida!!\n')
        continue

    if opção == 'S':
        break

    else:
        if opção == 'F':
            service = input('nome do serviço: ')
            password = input('qual senha: ')
            username = input('username: ')
            insert_password(service, username, password)
            

        if  opção == 'L':
            show_service()

        if opção == 'R':
            serviço = input('qual serviço deseja ver? ')
            get_password(serviço)

conn.close()