import mysql.connector

mydb = mysql.connector.connect(
  host="10.1.1.109",
  user="admin",
  password="admin",
  database=""
)

mycursor = mydb.cursor()

mycursor.execute("create database pesquisa")

mycursor.execute("show databases")

for x in mycursor:
    print(x)
#MENU
def menu():
    print('''Menu:
    Olá, as respostas para essas perguntas são anônimas e nos ajudam a melhorar nosso atendimento ao cliente.
        [1] - Iniciar as perguntas
        [2] - Sair  ''')
    int(input('Escolha uma opção: '))

iniciarPerguntas = 1
sair = 2