import mysql.connector
import socket as sock
#import mariadb

# mysql.connector.connect --> mariadb.connect
def db_get():
    conn = mysql.connector.connect(
        host="10.10.0.10",
        user="dario_benzi",
        password="benzi1234",
        database="5ATepsit",
        port=3306, # voi qui mettete la porta 3306!! quella di default per mySQL, io ho dovuto mettere la 3307 perche la mia 3306 era gia occupata dal database SQL sul mio PC!
        )

    cur = conn.cursor()

    # si chiama una funzione di libreria passando i parametri di ricerca dell'utente. esempio controlla_caratteri(nome)
    query = "SELECT * FROM dipendenti_dario_benzi"
    cur.execute(query)
    dati = cur.fetchall()
    print(dati)
    return dati

#creazione server socket
if __name__ == '__main__':
    db_get()