from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, Date
from sqlalchemy.orm import Session, DeclarativeBase
import os
from datetime import datetime
from classi import Base, Cliente, Ticket, Commento

engine = create_engine('postgresql://its_user:its_password@localhost:5432/its_database')
#Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


with Session(engine) as session:
    scelta = ""

    while scelta != "exit":
        print("\n--- Sistema di Gestione Ticket ---")
        print("\nScegli un'opzione:")
        print("1. Crea un nuovo cliente")
        print("2. Crea un nuovo ticket")
        print("3. Visualizza tutti i clienti")
        print("4. Visualizza tutti i ticket di un cliente")
        print("5. Visualizza tutti i ticket")
        print("6. Scegli un ticket da aggiornare o commentare")
        print("0. Esci")

        scelta = input("Inserisci il numero dell'opzione: ")

        if scelta == "1":
            os.system("clear")
            nome = input("Inserisci il nome del cliente: ")
            email = input("Inserisci l'email del cliente: ")
            password = input("Inserisci la password del cliente: ")
            nuovo_cliente = Cliente(nome=nome, email=email, password=password)
            session.add(nuovo_cliente)
            session.commit()
            print(f"Cliente '{nome}' creato con successo.")
        elif scelta == "2":
            os.system("clear")
            titolo = input("Inserisci il titolo del ticket: ")
            stato = input("Inserisci lo stato del ticket: ")
            cliente_id = int(input("Inserisci l'ID del cliente associato al ticket: "))
            nuovo_ticket = Ticket(titolo=titolo, stato=stato, cliente_id=cliente_id)
            session.add(nuovo_ticket)
            session.commit()
            print(f"Ticket '{titolo}' creato con successo.")
        elif scelta == "3":
            os.system("clear")
            clienti = session.query(Cliente).all()
            print("\n--- Elenco Clienti ---")
            for cliente in clienti:
                print(cliente)
        elif scelta == "4":
            os.system("clear")
            cliente_id = int(input("Inserisci l'ID del cliente per visualizzare i suoi ticket: "))
            tickets = session.query(Ticket).filter_by(cliente_id=cliente_id).all()
            print(f"\n--- Ticket del Cliente ID {cliente_id} ---")
            for ticket in tickets:
                print(ticket)
        elif scelta == "5":
            os.system("clear")
            stato = input("Inserisci lo stato del ticket da visualizzare: ")
            tickets = session.query(Ticket).filter_by(stato=stato).all()
            print(f"\n--- Ticket con stato '{stato}' ---")
            for ticket in tickets:
                print(ticket)
        elif scelta == "6":
            os.system("clear")
            ticket_id = int(input("Inserisci l'ID del ticket da aggiornare o commentare: "))
            ticket = session.query(Ticket).filter_by(id=ticket_id).first()
            if ticket:
                print(f"\n--- Dettagli del Ticket ID {ticket_id} ---")
                print(ticket)
                print("\nScegli un'opzione:")
                print("1. Aggiorna lo stato del ticket")
                print("2. Aggiungi un commento al ticket")
                sub_scelta = input("Inserisci il numero dell'opzione: ")
                if sub_scelta == "1":
                    nuovo_stato = input("Inserisci il nuovo stato del ticket: ")
                    ticket.stato = nuovo_stato
                    session.commit()
                    print(f"Stato del ticket ID {ticket_id} aggiornato a '{nuovo_stato}'.")
                elif sub_scelta == "2":
                    testo_commento = input("Inserisci il testo del commento: ")
                    nuovo_commento = Commento(testo=testo_commento, ticket_id=ticket_id)
                    session.add(nuovo_commento)
                    session.commit()
                    print(f"Commento aggiunto al ticket ID {ticket_id}.")
                else:
                    print("Opzione non valida. Riprova.")
            else:
                print(f"Ticket con ID {ticket_id} non trovato.")
        elif scelta == "0":
            print("Uscita...")
            break
        else:
            print("Opzione non valida. Riprova.")

