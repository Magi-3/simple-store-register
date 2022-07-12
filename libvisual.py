def clean():
    print(('\n') * 100)
        
def print_line(texto, tamanho):
    print(texto.center(tamanho))

def head():
    print('*********** PHONK LOJA *************')

def head_user():
    print('*********** CADASTRO *************')
        
def head_show_users():
    print('*********** USUÁRIOS *************')
    
def menu(lista):
    count = 1
    head()
    print('\n')
     
    for i in lista:
        print('[{}]' ' {}'.format(count, i))
        count += 1  

def menu_users(lista, users):
    count = 1
    head_show_users()
    
    for user in users:
            print(' - ' + user['nome completo'] + ' - ' + user['login'])
    print('\n')
    
    for i in lista:
        print('[{}]' ' {}'.format(count, i))
        count += 1
