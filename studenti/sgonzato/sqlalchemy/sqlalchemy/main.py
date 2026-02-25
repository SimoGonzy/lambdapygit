from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Session, DeclarativeBase
import datetime, os, time
from classi import Base, Cliente, Ticket, Commento

engine = create_engine('postgresql://its_user:its_password@localhost:5432/its_database')
#Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

with Session(engine) as session:
    scelta = ""

    while scelta != "0":
        os.system("clear")
        print("\n--- Sistema di Gestione dei Ticket ---")
        print("\nScegli un'opzione:")
        print("1. Crea un nuovo cliente")
        print("2. Crea un nuovo ticket")
        print("3. Visualizza i ticket")
        print("4. Cerca ticket per ID o titolo")
        print("5. Aggiorna lo stato di un ticket")
        print("6. Visualizza tutti i commenti")
        print("0. Esci")

        scelta = input("Inserisci il numero dell'opzione: ")

        if scelta == "1":
            os.system("clear")
            nome = input("\nInserisci il nome del cliente: ")
            email = input("Inserisci l'email del cliente: ")
            password = input("Inserisci la password del cliente: ")
            nuovo_cliente = Cliente(nome=nome, email=email, password=password)


            session.add(nuovo_cliente)
            session.commit()

            all_clienti = session.query(Cliente).all()
            for cliente in all_clienti:
                print("\n" + str(cliente))

            print(f"\nCliente '{nome}' creato con successo.")
            time.sleep(2.5)

        if scelta == "2":
            os.system("clear")
            titolo = input("Inserisci il titolo del ticket: ")
            stato = input("Inserisci lo stato del ticket: ")
            cliente_id = int(input("Inserisci l'ID del cliente associato al ticket: "))
            nuovo_ticket = Ticket(titolo=titolo, stato=stato, cliente_id=cliente_id)

            session.add(nuovo_ticket)
            session.commit()

            print(f"\nTicket '{titolo}' creato con successo.")
            time.sleep(2.5)

        if scelta == "3":
            os.system("clear")
            ticket_chiusi = session.query(Ticket).filter(Ticket.stato == "Chiuso").all()

            print("\n--- Ticket Chiusi ---")
            for ticket in ticket_chiusi:
                print("\n" + str(ticket))

            ticket_aperti = session.query(Ticket).filter(Ticket.stato == "Aperto").all()

            print("\n--- Ticket Aperti ---")
            for ticket in ticket_aperti:
                print("\n" + str(ticket))

            time.sleep(2.5)

        if scelta == "4":
            os.system("clear")
            criterio = input("\nCerca per (1) ID o (2) Titolo: ")

            if criterio == "1":
                ticket_id = int(input("Inserisci l'ID del ticket: "))
                ticket = session.query(Ticket).filter(Ticket.id == ticket_id).first()
                if ticket:
                    print("\n" + str(ticket))
                else:
                    print("\nNessun ticket trovato con l'ID specificato.")
            elif criterio == "2":
                titolo = input("Inserisci il titolo del ticket: ")
                tickets = session.query(Ticket).filter(Ticket.titolo.ilike(f"%{titolo}%")).all()

                if tickets:
                    for ticket in tickets:
                        print("\n" + str(ticket))
                else:
                    print("\nNessun ticket trovato con il titolo specificato.")
            time.sleep(2.5)


        if scelta == "5":
            os.system("clear")
            ticket_id = int(input("\nInserisci l'ID del ticket da aggiornare: "))
            criterio = input("Aggiornare (1) Stato o (2) Commento: ")

            if criterio == "1":
                nuovo_stato = input("Inserisci il nuovo stato del ticket: ")
                ticket = session.query(Ticket).filter(Ticket.id == ticket_id).first()
                if ticket:
                    ticket.stato = nuovo_stato
                    session.commit()

                    print(f"\nStato del ticket ID {ticket_id} aggiornato a '{nuovo_stato}'.")
                else:
                    print("\nNessun ticket trovato con l'ID specificato.")

            elif criterio == "2":
                testo_commento = input("Inserisci il testo del commento: ")
                nuovo_commento = Commento(testo=testo_commento, ticket_id=ticket_id)
                session.add(nuovo_commento)
                session.commit()

                print(f"\nCommento aggiunto al ticket ID {ticket_id}.")
            time.sleep(2.5)

        if scelta == "6":
            os.system("clear")

            print("\n--- Tutti i Commenti ---")
            all_commento = session.query(Commento).all()
            for commento in all_commento:
                print("\n" + str(commento))

            time.sleep(2.5)

        if scelta == "0":
            print("\nUscita in corso...")
            time.sleep(5)
            break

print("\nGrazie per aver utilizzato il sistema di gestione dei ticket!")