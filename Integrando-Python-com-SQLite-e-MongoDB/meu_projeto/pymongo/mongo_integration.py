from pymongo import MongoClient

# Conectando ao MongoDB Atlas
client = MongoClient('mongodb+srv://meu_usuario:minha_senha@cluster0.mongodb.net/test?retryWrites=true&w=majority')
db = client['banco']
collection = db['clientes']

# Estrutura de dados para inserir
clientes_data = [
    {
        "nome": "João Silva",
        "email": "joao@example.com",
        "contas": [
            {"numero": "12345", "saldo": 1000}
        ]
    },
    {
        "nome": "Maria Souza",
        "email": "maria@example.com",
        "contas": [
            {"numero": "67890", "saldo": 2000}
        ]
    }
]

# Inserindo documentos
collection.insert_many(clientes_data)
