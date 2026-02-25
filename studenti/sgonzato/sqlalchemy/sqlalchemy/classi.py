from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Session, DeclarativeBase
import datetime, os, time


class Base(DeclarativeBase):
    pass

class Cliente(Base):
    __tablename__ = 'clienti'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String)
    password = Column(String)
    
    def __str__(self):
        return f"Id: {self.id}, Nome: {self.nome}, Email: {self.email}, Password: {self.password}"

class Ticket(Base):
    __tablename__ = 'ticket'
    
    id = Column(Integer, primary_key=True)
    titolo = Column(String)
    stato = Column(String)
    data = Column(DateTime, default=datetime.datetime.utcnow)
    cliente_id = Column(Integer, ForeignKey('clienti.id'))
    
    def __str__(self):
        return f"Id: {self.id}, Titolo: {self.titolo}, Stato: {self.stato}, Data Creazione: {self.data}"

class Commento(Base):
    __tablename__ = 'commenti'
    
    id = Column(Integer, primary_key=True)
    testo = Column(String)
    data = Column(DateTime, default=datetime.datetime.utcnow)
    ticket_id = Column(Integer, ForeignKey('ticket.id'))
    
    def __str__(self):
        return f"Id Ticket: {self.ticket_id}, Testo: {self.testo}, Data Creazione: {self.data}"