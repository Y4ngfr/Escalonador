from factory.algoritmoFactory import AlgoritmoFactory
from models.processo import Processo
from models.SO import SO
import sys
import signal
import time

def handle_sigint(signum, frame):
        print("\nEncerrando sistema...")
        exit(0)

if __name__ == "__main__":
    try:
        algoritmo = input("Insira o Algoritmo: ")
        algoritmo = AlgoritmoFactory.defineAlgoritimo(algoritmo=algoritmo)
    except Exception as e:
        print(e)
        exit()
        
    so = SO(algoritmo=algoritmo)
    
    so.escalonador.setAlgoritmo()
    
    print(f"Algoritmo: {so.escalonador.getAlgoritmo()}", end="\n\n")

    signal.signal(signal.SIGINT, handle_sigint)

    while(True):
        time.sleep(1)
        so.step()