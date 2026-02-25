from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, Date
from sqlalchemy.orm import Session, DeclarativeBase
import os
from datetime import datetime

class Base (DeclarativeBase):
    pass


class Cliente(Base):
    __tablename__ = 'clienti'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)

    def __str__(self):
        return f"<Cliente(id={self.id}, nome='{self.nome}', email='{self.email}')>"
    
class Ticket(Base):
    __tablename__ = 'ticket'

    id = Column(Integer, primary_key=True)
    titolo = Column(String(100), nullable=False)
    stato = Column(String(20), nullable=False)
    data_creazione = Column(Date, default=datetime.now())
    cliente_id = Column(Integer, ForeignKey('clienti.id'), nullable=False)

    def __str__(self):
        return f"<Ticket(id={self.id}, titolo='{self.titolo}', stato='{self.stato}', data_creazione='{self.data_creazione}', cliente_id={self.cliente_id})>"
    
class Commento(Base):
    __tablename__ = 'commenti'

    id = Column(Integer, primary_key=True)
    testo = Column(Text, nullable=False)
    data_creazione = Column(Date, default=datetime.now())
    ticket_id = Column(Integer, ForeignKey('ticket.id'), nullable=False)


    def __str__(self):
        return f"<Commento(id={self.id}, testo='{self.testo}', data_creazione='{self.data_creazione}', ticket_id={self.ticket_id})>"