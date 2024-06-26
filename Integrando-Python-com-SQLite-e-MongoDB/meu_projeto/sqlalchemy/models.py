from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String)
    contas = relationship("Conta", back_populates="cliente")

class Conta(Base):
    __tablename__ = 'contas'
    id = Column(Integer, primary_key=True)
    numero = Column(String)
    saldo = Column(Integer)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    cliente = relationship("Cliente", back_populates="contas")

# Configurando o banco de dados
engine = create_engine('sqlite:///banco.db')
Base.metadata.create_all(engine)
