from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Date
from .db import Base

# Aqui criamos uma Tabela de usuário de Exemplo
class User(Base):
    # Aqui vai o nome da tabela no Banco de Dados
    __tablename__ = 'users'

    # Definição de Colunas
    # Nome do Campo                 Definição do tipo da coluna
    id                  =           Column(Integer, primary_key=True)
    name                =           Column(String)
    valor               =           Column(Float, default=0.0)

    # Retorna uma representação da Tabela
    def __repr__(self):
        return f'Usuário {self.id}'
