from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, Date
from sqlalchemy.orm import Session, DeclarativeBase
import os
from datetime import datetime
from classi import Base, Cliente, Ticket, Commento

engine = create_engine('postgresql://its_user:its_password@localhost:5432/its_database')
Base.metadata.create_all(engine)

with Session(engine) as session:
    print("\n--- Sistema di Gestione Ticket ---")
    print("\nAccedi al sistema inserendo nome e password.")
    nome = input("Nome: ")
    password = input("Password: ")
    cliente = session.query(Cliente).filter_by(nome=nome, password=password).first()
    if cliente:
        print(f"\nBenvenuto, {cliente.nome}!")
        scelta = ""
    else:
        print("\nCredenziali non valide. Uscita dal sistema.")
        exit()

    while scelta != "exit":
        print("\nScegli un'opzione:")
        print("1. Crea un nuovo ticket")
        print("2. Visualizza i tuoi ticket")
        print("3. Scegli un ticket da aggiornare o commentare")
        print("0. Esci")

        scelta = input("Inserisci il numero dell'opzione: ")

        if scelta == "1":
            os.system("clear")
            titolo = input("Inserisci il titolo del ticket: ")
            stato = input("Inserisci lo stato del ticket: ")
            nuovo_ticket = Ticket(titolo=titolo, stato=stato, cliente_id=cliente.id)
            session.add(nuovo_ticket)
            session.commit()
            print(f"Ticket '{titolo}' creato con successo.")
        elif scelta == "2":
            os.system("clear")
            tickets = session.query(Ticket).filter_by(cliente_id=cliente.id).all()
            print(f"\n--- I tuoi Ticket ---")
            for ticket in tickets:
                print(ticket)
        elif scelta == "3":
            os.system("clear")
            ticket_id = int(input("Inserisci l'ID del ticket da aggiornare o commentare: "))
            ticket = session.query(Ticket).filter_by(id=ticket_id, cliente_id=cliente.id).first()
            if ticket:
                print(f"\n--- Dettagli del Ticket ID {ticket_id} ---")
                print(ticket)
                print("\nScegli un'opzione:")
                print("1. Aggiorna un commento")
                print("2. Aggiungi un commento al ticket")
                print("0. Torna al menu principale")

                scelta_ticket = input("Inserisci il numero dell'opzione: ")

                if scelta_ticket == "1":
                    commenti = session.query(Commento).filter_by(ticket_id=ticket_id).all()
                    print(f"\n--- Commenti del Ticket ID {ticket_id} ---")
                    for commento in commenti:
                        print(commento)
                    commento_id = int(input("Inserisci l'ID del commento da aggiornare: "))
                    commento_da_aggiornare = session.query(Commento).filter_by(id=commento_id, ticket_id=ticket_id).first()
                    if commento_da_aggiornare:
                        nuovo_testo = input("Inserisci il nuovo testo del commento: ")
                        commento_da_aggiornare.testo = nuovo_testo
                        session.commit()
                        print(f"Commento ID {commento_id} aggiornato con successo.")
                    else:
                        print(f"\nCommento ID {commento_id} non trovato per il ticket ID {ticket_id}.")
                elif scelta_ticket == "2":
                    testo_commento = input("Inserisci il testo del commento: ")
                    nuovo_commento = Commento(testo=testo_commento, ticket_id=ticket.id)
                    session.add(nuovo_commento)
                    session.commit()
                    print(f"Commento aggiunto al ticket ID {ticket_id} con successo.")
            else:
                print(f"\nTicket ID {ticket_id} non trovato o non appartiene a te.")