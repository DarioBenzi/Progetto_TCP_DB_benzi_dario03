import socket

HOST = 'localhost'          # Il nodo remoto, qui metti il tuo indirizzo IP per provare connessione server e client dalla tua macchina alla tua macchina
PORT = 50010                # La stessa porta usata dal server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    data = s.recv(1024).decode()      #richiesta inserimento operazioni CRUD
    #FINIRE CONTROLLO PASSWORD (se più 3 errori server manda messaggio uscita programma poi break)
    print("Received:", data)
    if data == "Uscita dal programma...":
        break
    mess = input("Inserisci: ").encode()
    s.send(mess)

s.close()