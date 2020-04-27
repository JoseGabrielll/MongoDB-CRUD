from pymongo import MongoClient

client = MongoClient() #nessa instancia pode ser passado vários parâmetros como url, porta, etc.
db = client.get_database('alunosdb') #se o banco existir ele acessa o banco , se nao existir ele cria
collection = db.get_collection('alunos') #importa a coleção (semelhante a tabela do mySQL) (se existir retorna, se nao cria uma nova)

'''
#criando dados (Create) Descomenta na primeira vez que for rodar para gerar os documentos na coleção
data = {
    'nome': 'Felipe',
    'idade': 26,
    'endereco': 'Rua teste 1 , numero 25'
}

collection.insert(data) #insere os dados na coleção

#inserindo vários objetos de uma vez:
data2 = [
    {
        'nome': 'Gabriel',
        'idade': 26,
        'endereco': 'Rua teste 2, numero 10'
    },
    {
        'nome': 'Ana',
        'idade': 38,
        'endereco': 'Rua teste 3, numero 120'
    }
]

collection.insert(data2) #insere os dois objetos de uma vez
'''

#Lendo/recuperando dados (Read)

#exemplo 1: Exibindo todos os alunos
print('Exibindo alunos cadastrados:')
for aluno in collection.find():
    print(aluno.get('_id'), aluno.get('nome'))

#exemplo 2: Buscando por nome
print('Buscando por nome:')
for aluno in collection.find({'nome': 'Gabriel'}):
    print(aluno.get('_id'), aluno.get('nome'))

#exemplo3: Buscando por idade
print('Buscando por idade:')
for aluno in collection.find({'idade': {'$gte': 25}}): #buscando todos os alunos com idade maior ou igual a 25 anos
    print(aluno.get('_id'), aluno.get('nome'))

#exemplo4: criando filtro fora com várias condições
filters = {
    '$and': [
        {'nome': 'Gabriel'},
        {'idade': 26}
    ]
}
print('Buscando por vários filtros:')
for aluno in collection.find(filters):
    print(aluno)

#Atualizando dados (Update)

#Exemplo 1 Fazendo update apenas no primeiro caso que encontrar
print('Atualizando dados de uma pessoa:')
collection.update_one(
    {'nome': 'Ana' },
    {'$set': {'idade': 30}} #Se o $set nao for utilizado o documento que tem nome Ana será apagado e adicionado apenas idade 
)

for aluno in collection.find({'nome' : 'Ana'}):
    print(aluno)

#Exemplo 2 Fazendo update para todos os casos no banco de dados
print('Atualizando dados de todas as pessoas:')
collection.update_many(
    {'idade': 26},
    {'$set':{ 'endereco' : 'Rua atualizada, numero 1000' }}
)
for aluno in collection.find({'idade' : 26}):
    print(aluno)

#Removendo dados (Delete)

#Exemplo1 Apagando um dado
print('Removendo alunos')
collection.remove(
    {'nome' : 'Ana'} #removendo quem tem o nome ana
)

for aluno in collection.find():
    print(aluno)
