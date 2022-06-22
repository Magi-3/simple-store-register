
clientes = []
data = {'dia': '22', 'mes': '06', 'ano': '2022'}

def verifica_lista():
    if len(clientes) == 0:
        return True
    else:
        return False
       
def validar_login(login):
    for cliente in clientes:
        if cliente['login'] == login:
            return True
    return False

def exibir_menu_principal():
    print('1 - Cadastrar cliente')
    print('2 - Listar clientes')
    print('3 - Sair')
    print('Digite a opção desejada: ')

def exibir_menu_listar():
    print('1 - criar relatorio')
    print('2 - mostrar dados do cliente')
    print('3 - Voltar ao menu')
    print('Digite a opção desejada: ')
        
def cadastrar_cliente():
    print('Cadastro de cliente')
    nome = input('Nome: ')
    login = input('login: ')
    endereco = input('Endereço completo(Rua, número, complemento, bairro, cidade, cep e ponto de referencia) ').split(',')
    telefone = input('Telefone: ')
    data = input('data de nascimento: ')
    id = len(clientes) + 1
    cliente = {'nome': nome, 'login': login, 'endereco': endereco, 'telefone': telefone, 'data': data, 'id': id}
    if validar_login(login):
        print('Login já existe')
    else:
        return cliente
        print('Cliente cadastrado com sucesso')
    
def mostrar_dados_cliente(login):
    if verifica_lista():
        print('Não há clientes cadastrados')
    else:
        print('Dados do cliente /n')
        for cliente in clientes:
            if cliente['login'] == login:
                print(cliente)
            
    print('/n 1 - Voltar ao menu')
    print('Digite a opção desejada: ')
   
def gerar_relatorio():
    with open('relatorio.txt', 'w') as relatorio:
        relatorio.write('A loja SUISSE tem no total de {} clientes\n'.format(len(clientes)))
        for cliente in clientes:
            relatorio.write('{}. - {}\n'.format(numero=cliente['numero'], nome=cliente['nome']))
        relatorio.write('Documento gerado em {}\n'.format(data=data))
def listar_clientes():
    print('Lista de clientes')
    if verifica_lista():
        print('Não há clientes cadastrados')
    else:
        for cliente in clientes:
            print(cliente['login'])
    
def main():
    while True:
        exibir_menu_principal()
        opcao = input()
        
        if opcao == '1':
            clientes.append(cadastrar_cliente())
        elif opcao == '2':
            listar_clientes()
            exibir_menu_listar()
            opcao = input()
            
            if opcao == '1':
                gerar_relatorio()
            elif opcao == '2':
                for cliente in clientes:
                    login = input('Digite o login do cliente: ')
                    for cliente in clientes:
                        if cliente['login'] == login:
                            mostrar_dados_cliente(login)
            elif opcao == '3':
                continue 
                   
        elif opcao == '3':
            break
        
                    
if __name__ == '__main__':
    main()