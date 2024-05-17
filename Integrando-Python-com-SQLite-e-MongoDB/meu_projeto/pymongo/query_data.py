from pymongo import MongoClient

# Conectando ao MongoDB Atlas
client = MongoClient('mongodb+srv://<username>:<password>@<cluster-url>/test?retryWrites=true&w=majority')
db = client['banco']
collection = db['clientes']

# Recuperando dados
clientes = collection.find()
for cliente in clientes:
    print(f"Cliente: {cliente['nome']}, Email: {cliente['email']}")
    for conta in cliente['contas']:
        print(f"  Conta Número: {conta['numero']}, Saldo: {conta['saldo']}")
