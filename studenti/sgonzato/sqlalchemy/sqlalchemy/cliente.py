from classi import Base, Cliente, Ticket, Commento
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Session, DeclarativeBase
import datetime, os, time

engine = create_engine('postgresql://its_user:its_password@localhost:5432/its_database')
Base.metadata.create_all(engine)

with Session(engine) as session:
    print("\nAccedi al sistema di gestione dei ticket")
    nome = input("\nInserisci il nome del cliente: ")
    password = input("Inserisci la password del cliente: ")

    cliente = session.query(Cliente).filter(Cliente.nome == nome, Cliente.password == password).first()
    if cliente:
        print(f"\nBenvenuto, {cliente.nome}!")
    else:
        print("\nCredenziali non valide. Accesso negato.")

    scelta = ""

    while scelta != "0":
        os.system("clear")
        print("\n--- Sistema di Gestione dei Ticket ---")
        print("\nScegli un'opzione:")
        print("1. Crea un nuovo ticket")
        print("2. Visualizza i tuoi ticket")
        print("3. Inserisci un commento in un ticket")
        print("0. Esci")

        scelta = input("\nInserisci il numero dell'opzione: ")
        if scelta == "1":
            os.system("clear")
            titolo = input("Inserisci il titolo del ticket: ")
            stato = input("Inserisci lo stato del ticket: ")
            nuovo_ticket = Ticket(titolo=titolo, stato=stato, cliente_id=cliente.id)

            session.add(nuovo_ticket)
            session.commit()

            print(f"\nTicket '{titolo}' creato con successo.")
            time.sleep(2.5)

        if scelta == "2":
            os.system("clear")
            tuoi_ticket = session.query(Ticket).filter(Ticket.cliente_id == cliente.id).all()
            if tuoi_ticket:
                print("\nI tuoi ticket:")
                for ticket in tuoi_ticket:
                    print("\n" + str(ticket))
            else:
                print("\nNon hai ancora creato alcun ticket.")
            time.sleep(2.5)

        if scelta == "3":
            os.system("clear")
            ticket_id = int(input("Inserisci l'ID del ticket a cui vuoi aggiungere un commento: "))
            testo = input("Inserisci il testo del commento: ")
            
            nuovo_commento = Commento(testo=testo, ticket_id=ticket_id)
            session.add(nuovo_commento)
            session.commit()

            print(f"\nCommento aggiunto al ticket ID {ticket_id}.")
            time.sleep(2.5)

        if scelta == "0":
            print("\nArrivederci!")
            time.sleep(2.5)

print("\nSistema di gestione dei ticket chiuso.")