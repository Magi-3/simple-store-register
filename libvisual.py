from itertools import count

c = 0

def clean(invalid_input_state, users_state, registration_state):
    if invalid_input_state == True:
        print('/n' * 100)
        print('Opção inválida')
        
    elif users_state == True:
        print('/n' * 100)
        print('Não existem usuários cadastrados')
        users_state = False
    elif registration_state == True:
        print('/n' * 100)
        print('Cadastro realizado com sucesso')
        registration_state = False
        
def print_line(texto, tamanho):
    print(texto.center(tamanho))

def head():
    print('*********** MENU *************')

def head_user():
    print('*********** CADASTRO *************')
        
def head_show_users():
    print('*********** USUÁRIOS *************')
    
def user_erro():
    print('Usuário vazio')
    return True    
    
def menu(lista, erro, cadastro_ok, usuarios_ok):
    count = 1
    head()
    print('\n')
    
    if erro == True:
        print('Opção inválida')
    
    elif cadastro_ok == True:
        print('Cadastro realizado com sucesso')
    
    elif usuarios_ok == True:
        print('Não existem usuários cadastrados')    
    for i in lista:
        print('[{}]' ' {}'.format(count, i))
        count += 1  

def menu_users(lista, users):
    count = 1
    head_show_users()
    
    for user in users:
            print(' - ' + user['nome'])
    print('\n')
    
    for i in lista:
        print('[{}]' ' {}'.format(count, i))
        count += 1

def reset_states():
    global invalid_input_state
    global users_state
    global registration_state 
    
    invalid_input_state = False
    users_state = False
    registration_state = False