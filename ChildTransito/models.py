from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Questionarios(Base):
    __tablename__ = 'tb_questionarios'
    id = Column(Integer, primary_key=True)
    pergunta = Column(String(255))
    nivel= Column(String(255))
    alternativa1= Column(String(255))
    alternativa2= Column(String(255))
    alternativa3= Column(String(255))
    alternativa4= Column(String(255))
    resposta= Column(String(255))
    
