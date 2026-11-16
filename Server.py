import socket as sck

from BWT import BWT

with sck.socket(sck.AF_INET, sck.SOCK_STREAM) as server:
    IP="127.0.0.1" 
    PORTA=5000
    server.bind((IP, PORTA))
    server.listen()
    print("Server in ascolto su", IP, "porta", PORTA)
    with server.accept()[0] as connessione:
     dati = connessione.recv(1024)
     messaggio = dati.decode("utf-8")
     risultato_bwt = BWT(messaggio)
     connessione.sendall(risultato_bwt.encode("utf-8"))

print("server terminato")