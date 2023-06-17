import mysql.connect

#FUNÇÕES 
def conectar():
    banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="pesquisa"
    )
    return banco

#AREA ADMINISTRATIVA
def administrar():
    while True:
        print('''\n   \033[35mO que deseja fazer?\033[m
[ 1 ] Adicionar Dados
[ 2 ] Listar os Dados
[ 3 ] Filtrar Dados
[ 4 ] Alterar Dados
[ 5 ] Apagar Dados
[ 6 ] Trocar Tabela
[ 7 ] Sair''')
        try:
            escolha = int(input('\n \033[36mDigite aqui\033[m : '))
        except:
            print('\n   \033[31mDEVE SER UM NÚMERO!\033[m')
        else:
            if escolha == 7:
                break


def select(tabelas):
    print('''\033[32m\n Qual tabela você deseja listar?: \033[m
    [ 1 ] Tabela de perguntas
    [ 2 ] Tabela de estilos musicais''')
    while True:
        try:
            tabela = int(input('\n    \033[33mSua resposta : \033[m'))
            tabela -= 1
            tabela = tabelas[tabela][0]
        except:
            print('\033[31m\n    Opção inválida! por favor, digite novamente. . . \n\033[m')
        else:
            if tabela == 1:
                listar_perguntas = f'SELECT * perguntas'
                exec.execute(listar_perguntas)
                print('\n   \033[33mListagem Realizada!!\033[m')
            elif tabela == 2:
                listar_estilos = f'SELECT * estilos_musicais'
                exec.execute(listar_estilos)
                print('\n   \033[33mListagem Realizada!!\033[m')
            return tabela

def get_colunas(banco, tabela):
    conexao = banco.conectar()
    exec = conexao.cursor()
    
    exec.execute(f'DESCRIBE {tabela}')
    colunas = exec.fetchall()
    
    exec.close()
    conexao.close()
    return colunas

def delete(banco, tabela):
    conexao = banco.conectar()
    exec = conexao.cursor()
    id = int(input(f'\n\033[31mDigite o id do(a) {tabela} que deseja apagar : \033[m'))
    deletar = f'DELETE FROM {tabela} WHERE id = %s'
    valores = [id]

    exec.execute(deletar, valores)
    conexao.commit()
    exec.close()
    conexao.close()
    print('\n   \033[33mDados deletado com Sucesso!!\033[m')


#MENU
while True:
    print('''Menu:
    Olá, as respostas para essas perguntas são anônimas e nos ajudam a melhorar nosso atendimento ao cliente.
        [1] - Iniciar as perguntas
        [2] - Área de administração 
        [3] - Sair''')
    try:
        escolha = int(input('\n \033[36mEscolha uma opção:\033[m '))
    except: 
        print()
    else:
        if escolha == 1:
            print('ok')
        
        elif escolha == 2:
            input('Usuário: ')
            input('Senha: ')
            administrar()

        elif escolha == 3:
            print('Até mais! Obrigado por participar')
            break
