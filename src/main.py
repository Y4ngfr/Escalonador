from factory.algoritmoFactory import AlgoritmoFactory
from models.processo import Processo
from models.SO import SO
import signal
import time

def handle_sigint(signum, frame):
        print("\nEncerrando sistema...")
        exit(0)

if __name__ == "__main__":
    try:
        print("-"*14)
        print("| algoritmos |")
        print("| FCFS - SJF |")
        print("-"*14)
        
        algoritmo = input("Insira o Algoritmo: ")
        algoritmo = AlgoritmoFactory.defineAlgoritimo(algoritmo=algoritmo)
        
        round_robin = int(input("Insira o round robin: ")) 
        if round_robin <= 0: 
            round_robin = 1
    except Exception as e:
        print(e)
        exit()
        
    so = SO(algoritmo=algoritmo, round_robin=round_robin)
    so.escalonador.setAlgoritmo()
    
    print(f"Algoritmo selecionado: {so.escalonador.getAlgoritmo()}", end="\n\n")

    signal.signal(signal.SIGINT, handle_sigint)

    while(True):
        # time.sleep(1)
        input()
        so.step()