from calendar import month
from re import T
from libvisual import *
from libformat import format, create_user
from datetime import date

menu_itens_main = ['Cadastrar', 'Listar', 'Sair']
menu_itens_list = ['Acessar um Usuário', 'Gerar Relatório', 'voltar ao menu principal']
information = ['nome', 'login','senha', 'email', 'telefone', 'endereço(Rua, Número, Bairro, Cidade, CEP)', 'data de nascimento']
users = []
date = date.today()
day, month, year = date.day, date.month, date.year

def read_users():
    with open('clientes.txt', 'r') as f:
        for line in f:
            users.append(eval(line))
            
def append_on_txt(cliente):
    with open('clientes.txt', 'a') as f:
        f.write(str(cliente) + '\n')

def menu_list_choice():
    while True:
        opc = input()    
        if opc == '1':
            while True:
                print_line('Acessar um Usuário', 50)
                print('Caso deseje sair, digite "Sair" ')
                login = input('Informe o login do usuário que deseja acessar: ')
    
                for user in users:
                    if user['login'] == login:
                        print('Nome: ' + user['nome'])
                        print('Login: ' + user['login'])
                        print('Email: ' + user['email'])
                        print('Telefone: ' + user['telefone'])
                        print('Endereço: ' + user['endereço(Rua, Número, Bairro, Cidade, CEP)'] + '\n')  
                        break
                print('Deseja acessar outro usuário? (S/N)')
                yesorno = input()
                if yesorno == 'S':
                    continue
                elif yesorno == 'N':
                    menu_users(menu_itens_list, users)
                    break
                else:
                    print('Opção invalida')
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
        head_user()
        user = create_user(information)
        if user == {}:
            pass
        else:
            return user
               
def generate_report():
    c = 1
    name = 'relatorio_' + str(date) + '.txt'
    with open(name, 'w') as f:
        f.write('Relatório de usuários cadastrados\n')
        f.write('A Atom possui ' + str(len(users)) + ' usuários cadastrados\n')
        for user in users:
            f.write(f'{c} - ' + user['nome'] + '\n')
            c += 1
            
        f.write('\n')
        f.write('Russas, ' + str(day) + '/' + str(month) + '/' + str(year) + '\n')
    
    
def main():
    read_users()
    invalid_input_state = False
    users_state = False
    registration_state = False
    
    while True:
        clean(invalid_input_state, users_state, registration_state)
        reset_states()
        menu(menu_itens_main, invalid_input_state, registration_state, users_state)
        opc = input()
        if opc == '1':
            append_on_txt(registration())
            registration_state = True
        elif opc == '2':
            menu_users(menu_itens_list, users)
            menu_list_choice()    
        elif opc == '3':     
            break   
        elif opc == '':
            pass
        else:
            invalid_input_state = True
            registration_state = False


        

if __name__ == "__main__":
    main()