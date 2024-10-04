from models.processo import Processo
from models.escalonador import Escalonador
from models.despachante import Despachante
from models.SO import SO
import sys
import signal
import time

def handle_sigint(signum, frame):
        print("\nEncerrando sistema...")
        exit(0)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        so = SO(sys.argv[1])
    else:
        so = SO("FIFO")

    print(f"Algoritmo: {so.escalonador.algoritmo}", end="\n\n")

    signal.signal(signal.SIGINT, handle_sigint)

    while(True):
        time.sleep(1)
        so.step()