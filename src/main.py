from models.processo import Processo
from models.escalonador import Escalonador
from models.despachante import Despachante
from models.SO import SO
import sys
import signal

def handle_sigint(signum, frame):
        print("Encerrando sistema...")
        exit(0)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        so = SO(sys.argv[1])
    else:
        so = SO("FIFO")

    print(f"Algoritmo: {so.escalonador.algoritmo}", end="\n\n")

    signal.signal(signal.SIGINT, handle_sigint)

    while(True):
        input()
        so.step()