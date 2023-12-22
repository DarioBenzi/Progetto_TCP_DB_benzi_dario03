import threading 
import socket
import mysql.connector
import facilities
comunicazioni = ["",""]
PASSWORD = "CIAO"

def insert(conn, data, cur, db):
    conn.send("In quale tabella vuoi inserire: D=dipendenti, Z=zone_di_lavoro".encode()) #selezione tabella
    data = conn.recv(1024).decode()
    if data == "D": #caso dipendenti
        conn.send("Inserisci i dati di nome, cognome, data nascita, posizione lavorativa, data assunzione, turno: ".encode()) #inserimento per aggiunta
        data = conn.recv(1024).decode()
        #dizionario = facilities.bytes_to_dict(data) #richiamo a facilities per operazioni con dizionari
        lista = data.split(" ")
        dizionario = {
            "nome": lista[0],
            "cognome": lista[1],
            "posizione_lavorativa": lista[2],
            "data_assunzione": lista[3],
            "data_nascita": lista[4],
            "turno": lista[5]
        }
        cur.execute(f"INSERT INTO dipendenti_benzi_dario (nome, cognome, posizione_lavorativa, data_assunzione, data_nascita, turno) VALUES ('{dizionario['nome']}', '{dizionario['cognome']}', '{dizionario['posizione_lavorativa']}', '{dizionario['data_assunzione']}', '{dizionario['data_nascita']}', '{dizionario['turno']}')") #operazione insert
        db.commit() #salvataggio modifiche
        conn.send("Dati inseriti.".encode())
    elif data == "Z": #caso zone lavoro
        conn.send("Inserisci i dati di nome zona, numero clienti, id dipendente, aperture: ".encode())
        data = conn.recv(1024).decode()
        lista = data.split(" ")
        dizionario = {
            "nome_zona": lista[0],
            "numero_clienti": lista[1],
            "id_dipendente": lista[2],
            "aperture": lista[3],
        }
        cur.execute(f"INSERT INTO zone_di_lavoro_benzi_dario (nome_zona, numero_clienti, id_dipendente, aperture) VALUES ('{dizionario['nome_zona']}', '{dizionario['numero_clienti']}', '{dizionario['id_dipendente']}', '{dizionario['aperture']}')")
        db.commit()
        conn.send("Dati inseriti.".encode())
    else: #caso errore inserimento
        conn.send("inserimento errato. Reinserisci".encode())

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def update(conn, data, cur, db):
    conn.send("Quale tabella vuoi aggiornare: D=dipendenti, Z=zone_di_lavoro".encode()) #selezione tabella
    data = conn.recv(1024).decode()
    if data == "D": #caso dipendenti
        conn.send("Inserisci l'id che vuoi modifcare, e i dati di nome, cognome, posizione lavorativa, data assunzione, data nascita, turno: ".encode())  #inserimento per modifica di tutta riga
        data = conn.recv(1024).decode()
        lista = data.split(" ")
        dizionario = {
            "id": lista[0],
            "nome": lista[1],
            "cognome": lista[2],
            "posizione_lavorativa": lista[3],
            "data_assunzione": lista[4],
            "data_nascita": lista[5],
            "turno": lista[6]
        }
        cur.execute(f"UPDATE dipendenti_benzi_dario SET nome='{dizionario['nome']}', cognome='{dizionario['cognome']}', posizione_lavorativa='{dizionario['posizione_lavorativa']}', data_assunzione='{dizionario['data_assunzione']}', data_nascita='{dizionario['data_nascita']}', turno='{dizionario['turno']}' WHERE id={dizionario['id']}") #operazione update
        db.commit() #salvataggio modifiche
        conn.send("Dati modificati.".encode())
    elif data == "Z": #caso zone lavoro
        conn.send("Inserisci il nome_zona che vuoi modifcare, e i dati di numero clienti, id dipendente, aperture: ".encode())
        data = conn.recv(1024).decode()
        lista = data.split(" ")
        dizionario = {
            "nome_zona": lista[0],
            "numero_clienti": lista[1],
            "id_dipendente": lista[2],
            "aperture": lista[3],
        }
        cur.execute(f"UPDATE zone_di_lavoro_benzi_dario SET numero_clienti='{dizionario['numero_clienti']}', id_dipendente='{dizionario['id_dipendente']}', aperture='{dizionario['aperture']}' WHERE nome_zona='{dizionario['nome_zona']}'")
        db.commit()
        conn.send("Dati modificati.".encode())
    else: #caso errore inserimento
        conn.send("inserimento errato. Reinserisci".encode())

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def read(conn, data, cur):
    conn.send("Quale tabella vuoi visualizzare: D=dipendenti, Z=zone_di_lavoro".encode()) #selezione tabella
    data = conn.recv(1024).decode()
    if data == "D": #caso dipendenti
        cur.execute(f"SELECT * FROM dipendenti_benzi_dario") #lettura intera tabella
        data = cur.fetchall()
        listToStr = ' '.join([str(elem) for elem in data])  #Data risultava una tupla, list comprehension per fare una join e creare una stringa
        conn.send(listToStr.encode())
    elif data == "Z": #caso zone lavoro
        cur.execute(f"SELECT * FROM zone_di_lavoro_benzi_dario")
        data = cur.fetchall()
        listToStr = ' '.join([str(elem) for elem in data])
        conn.send(listToStr.encode())
    else: #caso errore inserimento
        conn.send("inserimento errato. Reinserisci".encode())

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def delete(conn, data, cur, db):
    conn.send("Quale tabella vuoi aggiornare: D=dipendenti, Z=zone_di_lavoro".encode()) #selezione tabella
    data = conn.recv(1024).decode()
    if data == "D": #caso dipendenti
        conn.send("Inserire la riga da eliminare tramite l'id del dipendente:".encode()) #selezione id per eliminazione
        data = conn.recv(1024).decode()
        cur.execute(f"DELETE FROM dipendenti_benzi_dario WHERE id={data}") #operazione delete
        db.commit() #salvataggio modifiche
        conn.send("Dati modificati.".encode())
    elif data == "Z": #caso zone lavoro
        conn.send("Inserire la riga da eliminare tramite il nome della zona:".encode())
        data = conn.recv(1024).decode()
        cur.execute(f"DELETE FROM zone_di_lavoro_benzi_dario WHERE nome_zona='{data}'")
        db.commit()
        conn.send("Dati modificati.".encode())
    else: #caso errore inserimento
        conn.send("inserimento errato. Reinserisci".encode())

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
def search(conn, data, cur):
    data = conn.recv(1024).decode()
    if data == "D": #caso dipendenti
        conn.send("Inserisci parametri da filtrare (*campo*:*attributo*). Per fermarti inserisci 'STOP':".encode()) #inserimento clausole per ricerca
        data = conn.recv(1024).decode()
        while data != "STOP": #ciclo per più inserimenti
            conn.send("Inserisci parametri da filtrare (*campo*:*attributo*). Per fermarti inserisci 'STOP':".encode())
            data = conn.recv(1024).decode()
        clausole = ""
        for key,value in parametri.items(): #aggiunta clausole in sintassi inserimento
            clausole = clausole + f"and {key} = '{value}'"
        cur.execute(f"SELECT * FROM dipendenti_dario_benzi WHERE 1=1 {clausole}") #aggiunta possibili clausole per filtri ricerca
        data = cur.fetchall()
        print(data) #stampa a video
    elif data == "Z":
        conn.send("Inserisci parametri da filtrare (*campo*:*attributo*). Per fermarti inserisci 'STOP':".encode())
        data = conn.recv(1024).decode()
        while data != "STOP":
            conn.send("Inserisci parametri da filtrare (*campo*:*attributo*). Per fermarti inserisci 'STOP':".encode())
            data = conn.recv(1024).decode()
        clausole = ""
        for key,value in parametri.items():
            clausole = clausole + f"and {key} = '{value}'"
        cur.execute(f"SELECT * FROM zone_di_lavoro_dario_benzi WHERE 1=1 {clausole}")
        data = cur.fetchall()
        print(data)
    else: #caso errore inserimento
        conn.send("inserimento errato. Reinserisci".encode())
'''
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def gestisci_comunicazione(conn):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="5atepsit",
        port=3306
    )
    cur = db.cursor() #cursore
    conn.send("Benvenuto, inserisci password: ".encode())
    data = conn.recv(1024).decode()
    while data != PASSWORD and i<2: #errore password
        conn.send(f"Password ERRATA, reinserisci password: tentativi rimasti {2-i}".encode())
        data = conn.recv(1024).decode()

    if(data != PASSWORD): #errore e uscita
        conn.send(f"Password ERRATA troppe volte, chiusura del programma".encode())
        conn.close()
        return

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    while True: #password giusta e selezione
        conn.send("Benvenuto cosa vuoi fare: C=insert, U=update, R=read, D=delete, E=exit".encode())
        data = conn.recv(1024).decode()
        print(data)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        if data == "C": #caso insert
            insert(conn, data, cur, db)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        elif data == "U": #caso update
            update(conn, data, cur, db)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        elif data == "R": #caso read
            read(conn, data, cur)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        elif data == "D": #caso delete
            delete(conn, data, cur, db)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#       elif data = "S":
#           search(conn, data, cur)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        elif data == "E":
            conn.send("Uscita dal programma...".encode())
            break
        else:
            conn.send("Inserimento errato.".encode())
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    return

def db_get():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="5atepsit",
        port=3306, # voi qui mettete la porta 3306!! quella di default per mySQL, io ho dovuto mettere la 3307 perche la mia 3306 era gia occupata dal database SQL sul mio PC!
        )
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    cur = conn.cursor()

    # si chiama una funzione di libreria passando i parametri di ricerca dell'utente. esempio controlla_caratteri(nome)
    query = "SELECT * FROM dipendenti_benzi_dario"
    cur.execute(query)
    dati = cur.fetchall()
    print(dati)
    return dati

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("server in ascolto: ")
lock = threading.Lock()
HOST = ''                 # Nome simbolico che rappresenta il nodo locale, ci va l'indirizzo IP
PORT = 50010            # Porta non privilegiata arbitraria
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)
thread = []
lista_connessioni = []
i=0

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

while True:
    lista_connessioni.append( s.accept() ) #connessione = s.accept()
    print('Connected by', lista_connessioni[i][1]) # print(connessione[0])
    thread.append(threading.Thread(target=gestisci_comunicazione, args = (lista_connessioni[i][0],) ))
    thread[i].start()
    i+=1