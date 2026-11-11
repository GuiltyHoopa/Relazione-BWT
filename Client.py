import socket as sck

IP="127.0.0.1"
PORTA=5000

messaggio = input("inserisci parola per riceverne il risultato del BWT")
with sck.socket(sck.AF_INET, sck.SOCK_STREAM) as client:
    client.sendall(messaggio.encode())
    dati = client.recv(1024)

    print("risposta dal server: ", dati.decode())
print("Client terminato")