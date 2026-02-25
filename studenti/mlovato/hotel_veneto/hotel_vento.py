import csv
import sqlite3

lista_tipologia = ""
lista_tipologie_secondarie = ""
lista_classificazioni = ""

with sqlite3.connect("db_strutture_turistiche_veneto.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tipologie")
    lista_tipologia = cursor.fetchall()
    cursor.execute("SELECT * from tipologie_secondarie")
    lista_tipologie_secondarie = cursor.fetchall()
    cursor.execute("SELECT * FROM classificazioni")
    lista_classificazioni = cursor.fetchall()
    conn.commit()

with open("Strutture-Turistiche-Veneto.csv", newline="\n") as f:
    reader = csv.reader(f, delimiter=";")
    header = next(reader)
    for index, column in enumerate(header):
        print(index, column)
    #province = set()
    #tipologie = set()
    #tipologie_secondarie = set()
    #province_comuni = set()
    #classificazioni = set()
    #indirizzi = list()
    #strutture = list()
    #servizi = list()
    tipo_struttura = list()


    i = 1
    for row in reader:
        #province.add(row[0].lower())
        #province_comuni.add((row[0].lower(), row[1].lower().replace("�", "ù").replace("�", "à")))
        #tipologie.add(row[3].replace("�", "ù").lower())
        #tipologie_secondarie.add(row[4].replace("�", "à").lower())
        #if row[9] != "":
            #classificazioni.add(row[9].lower())
        #strutture.append((row[5], row[6], row[7], row[8], row[14], row[15], row[16], row[17],))
        """temp = row[18:]
        row_bool = list()
        row_bool.append(i)
        for x in temp:
            if x.upper() == "SI":
                row_bool.append(1)
            elif x.upper() == "NO":
                row_bool.append(0)
        servizi.append(tuple(row_bool))
        i = i + 1"""

        # aggiunge indirizzi con chiave esterna a comune e a struttura
        """indirizzo = list()
        indirizzo.append(i)
        indirizzo.append(row[10].lower().replace("�", "à").replace("�", "ù"))
        indirizzo.append(row[11])
        indirizzo.append(row[13] if row[13] != "" else None)
        for comune in lista_comuni:
            if comune[1].lower() == row[1].lower().replace("�", "à").replace("�", "ù"):
                indirizzo.append(int(comune[0]))
                break
        if len(indirizzo) < 5:
            indirizzo.append(None)
        indirizzi.append(tuple(indirizzo))
        i = i + 1"""

        tipo = list()
        tipo.append(i)
        for tipologia in lista_tipologia:
            if row[3].lower().replace("�", "ù") == tipologia[1]:
                tipo.append(tipologia[0])
        if len(tipo) < 2:
            tipo.append(None)
        
        for tipologia_secondaria in lista_tipologie_secondarie:
            if row[4].lower().replace("�", "à") == tipologia_secondaria[1]:
                tipo.append(tipologia_secondaria[0])
        if len(tipo) < 3:
            tipo.append(None)
        if row[9] == "":
            tipo.append(None)
        else:
            for classificazione in lista_classificazioni:
                if row[9].lower() == classificazione[1]:
                    tipo.append(classificazione[0])
        i = i + 1
        tipo_struttura.append(tuple(tipo))


    with sqlite3.connect("db_strutture_turistiche_veneto.db") as conn:
        cursor = conn.cursor()
        """
        aggiunge tutte le province al DB

        for provincia in province:
            cursor.execute("INSERT INTO PROVINCE(provincia) values(?)", (provincia,))
        """
        """
        aggiunge i comuni con chiave esterna alla provincia

        cursor.execute("SELECT * FROM PROVINCE")
        rows = cursor.fetchall()
        for provincia_comune in province_comuni:
            for provincia in rows:
                if provincia_comune[0] in provincia:
                    cursor.execute("INSERT INTO comuni(provincia_id, comune) VALUES(?,?)", (provincia[0], provincia_comune[1]))
        """

        """
        aggiunge le tipologie

        for tipologia in tipologie:
            cursor.execute("INSERT INTO tipologie(tipologia) values (?)", (tipologia,))
        """

        """
        inserisce le tipologie secondarie
        
        for tipologia_secondaria in tipologie_secondarie:
            cursor.execute("INSERT into tipologie_secondarie(tipologia_secondaria) values (?)", (tipologia_secondaria,))
        """

        """
        aggiungo le classificazioni 1 stella 2 stelle 2 leoni etc
        
        for classificazione in sorted(list(classificazioni)):
            cursor.execute("INSERT INTO classificazioni(classificazione) values(?)", (classificazione,))
        """

        """
        inserisci tutti gli indirizzi
        
        for indirizzo in indirizzi:
            cursor.execute("INSERT INTO indirizzi(indirizzo, numero_civico, interno, cap, comune_id) values (?,?,?,?,?)", (indirizzo[0], indirizzo[1], indirizzo[2], indirizzo[3], indirizzo[4]))
            """

        """
        Aggiunge tutte le strutture (con anche i contatti)
        
        for struttura in strutture:
            cursor.execute("INSERT INTO strutture (struttura, codice_cin, camere, posti_letto, telefono, fax, email, sito_web) values (?,?,?,?,?,?,?,?)", (struttura[0], struttura[1], struttura[2], struttura[3], struttura[4], struttura[5], struttura[6], struttura[7]))
        """

        # cursor.executemany("INSERT INTO servizi (id_struttura, piscina, piscina_coperta, campo_da_tennis, ristorante, parcheggio_non_custodito, parcheggio_custodito, sala_conferenze, aria_condizionata, sauna, solarium, area_fitness, animali_ammessi, servizio_navetta, vicinanza_mezzi_pubblici, noleggio_biciclette, inglese, francese, tedesco, spagnolo, russo, cinese, portoghese, chiusura_temporanea) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", servizi)

        #cursor.executemany("INSERT INTO indirizzi (id_struttura, indirizzo, numero_civico, cap, id_comune) values (?,?,?,?,?)", indirizzi)

        #cursor.executemany("INSERT INTO tipologie_strutture (id_struttura, id_tipologia, id_tipologia_secondaria, id_classificazione) values (?,?,?,?)", tipo_struttura)

        conn.commit() # commit dei comandi sql
