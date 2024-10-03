import time
import random
from models.processo import Processo
from models.escalonador import Escalonador
from models.despachante import Despachante

if __name__ == "__main__":
    algoritmo_vez = "FIFO"
    print(f"Algoritmo: {algoritmo_vez}", end="\n\n")
    escalonador = Escalonador()
    despachante = Despachante()
    while(True):
        time.sleep(2)
        chance = random.randint(1, 100)

        if chance > 21:
            pass
        else:
            processo = Processo()
            #print(f"Novo processo: (Id:{processo.getId()}[{processo.getTempoExecucao()}]) adicionando na fila...")
            #input()
            escalonador.add_fila_processo(processo=processo, tipo_algoritimo=algoritmo_vez)
            
        print("Fila de processos:")
        for processo in reversed(escalonador.fila_processos):
            if processo == escalonador.fila_processos[0]:
                print(f"(Id:{processo.getId()})[{processo.getTempoExecucao()}]({processo.getEstado()})")
            else:
                print(f"(Id:{processo.getId()})[{processo.getTempoExecucao()}]({processo.getEstado()}) -> ", end="")
        #input()
        #print(f"Executando primeiro da fila: (Id:{processo.getId()})[{processo.getTempoExecucao()}] ...", end="\n\n")
        escalonador.chamar_despachante(despachante)
        escalonador.atualiza_fila_processos()
        escalonador.atualiza_fila_espera()