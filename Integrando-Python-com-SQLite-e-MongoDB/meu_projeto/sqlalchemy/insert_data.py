from models import Cliente, Conta, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# Inserindo clientes e contas
cliente1 = Cliente(nome="João Silva", email="joao@example.com")
conta1 = Conta(numero="12345", saldo=1000, cliente=cliente1)

cliente2 = Cliente(nome="Maria Souza", email="maria@example.com")
conta2 = Conta(numero="67890", saldo=2000, cliente=cliente2)

session.add(cliente1)
session.add(conta1)
session.add(cliente2)
session.add(conta2)

session.commit()
