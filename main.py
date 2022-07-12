from libvisual import *
from datetime import date
import time

menu_itens_main = ['Cadastrar', 'Listar', 'Sair']
menu_itens_list = ['Acessar um Usuário', 'Gerar Relatório', 'voltar ao menu principal']
information = ['nome completo', 'login','senha', 'email', 'telefone', 'endereço(Rua, Número, Bairro, Cidade, CEP, complemento, ponto de referencia)', 'data de nascimento']
users = []
date = date.today()
day, month, year = date.day, date.month, date.year

def check_login(login):
    for user in users:
        if user['login'] == login:
            return True
    return False

def read_db():
    db_client = open('clientes.txt', 'r')
    clients = db_client.readlines()
    db_client.close()
    return clients

def read_users():
    with open('clientes.txt', 'r') as f:
        clients = read_db()
        for client in clients:
            user = eval(client)
            users.append(user)
            
def append_on_txt(cliente):
    with open('clientes.txt', 'a') as f:
        f.write(str(cliente) + '\n')

def create_user(info):
    user = {}
    for data in info:
        print(data + ':')
        opc = input()
        if data == 'login':
            while check_login(opc):
                print('Login já existe, digite outro login')
                opc = input()
        user.update({data : opc})
    return user
        
def find_user(login):
    for user in users:
        if user['login'] == login:
            return user
    return None
                    
def menu_list_choice():
    while True:
        clean()
        menu_users(menu_itens_list, users)
        opc = input()    
        if opc == '1':
           while True:
            print('Digite o login do usuário:')
            login = input()
            user = find_user(login)
            if user == None:
                print('Usuário não encontrado')
                time.sleep(2)
                break
            else:
                #imprimir todos os dados do usuario usando print_line   
                print_line('Nome Completo:', 50)
                print_line(user['nome completo'], 50)
                print_line('Login:', 50)
                print_line(user['login'], 50)
                print_line('Senha:', 50)
                print_line(user['senha'], 50)
                print_line('Email:', 50)
                print_line(user['email'], 50)
                print_line('Telefone:', 50)
                print_line(user['telefone'], 50)
                print_line('Endereço:', 50)
                print_line(user['endereço(Rua, Número, Bairro, Cidade, CEP, complemento, ponto de referencia)'], 50)
                print('\n')
                print('Deseja acessar outro usuário? (s/n)')
                opc = input()
                if opc == 's':
                    continue
                elif opc == 'n':
                    break
        elif opc == '2':
            print_line('Gerar Relatório', 50)
            generate_report()
            print('Relatório gerado com sucesso')
            print('\n')
            menu_users(menu_itens_list, users)
            
        elif opc == '3':
            break
        else:
            print('Informação inválida')
            pass
                                
def registration():
    while True:
        user = create_user(information)
        users.append(user)
        return user
               
def generate_report():
    c = 1
    name = 'relatorio_' + str(date) + '.txt'
    with open(name, 'w') as f:
        f.write('Relatório de usuários cadastrados\n')
        f.write('A PHONK possui ' + str(len(users)) + ' usuários cadastrados\n')
        for user in users:
            f.write(f'{c} - ' + user['nome completo'] + '\n')
            c += 1
            
        f.write('\n')
        f.write('Russas, ' + str(day) + '/' + str(month) + '/' + str(year) + '\n')
    
    
def main():
    read_users()
    while True:
        clean()
        menu(menu_itens_main)
        opc = input()
        if opc == '1':
            head_user()
            append_on_txt(registration())
            print('Usuário cadastrado com sucesso')
            time.sleep(2)

        elif opc == '2':
            menu_list_choice()    
        elif opc == '3':     
            break   
        elif opc == '':
            print('Opção inválida')
            time.sleep(2)
        else:
            print('Opção inválida')
            time.sleep(2)
            pass

        

if __name__ == "__main__":
    main()