import socket as sck

with sck.socket(sck.AF_INET, sck.SOCK_STREAM) as server:
    IP="127.0.0.1" 
    PORTA=5000
    server.bind((IP, PORTA))
    print("Server in ascolto su", IP, "porta", PORTA)
    with server.accept()[0] as connessione:
