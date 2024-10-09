from models.despachante import Despachante
from models.processo import Processo
import random

class SO:
    def __init__(self, algoritmo, round_robin):
        self.despachante = Despachante(round_robin)
        self.escalonador = algoritmo()
        # self.i =0
    
    def step(self):
        if random.randint(1, 100) < 70:
        # if self.i < 5:
            processo = Processo()
            # processo.tempo_execucao = self.i*3 + 7
            self.escalonador.add_fila_processo(processo=processo)
        # self.i += 1

        print("Filas:")

        self.printa_fila(self.escalonador.fila_processos, nome_fila="Processos")
        self.printa_fila(self.escalonador.fila_espera, nome_fila="Espera")
        
        if len(self.escalonador.fila_processos) > 0:
            self.despachante.executar_processo(self.escalonador.fila_processos[0])
        
        self.escalonador.inserir_entrada()
        self.escalonador.atualiza_fila_processos()
        self.escalonador.atualiza_fila_espera()

    def printa_fila(self, fila, nome_fila):
        print(f"{nome_fila}: ", end="")
        
        if len(fila) == 0:
            print("<Fila vazia>")
            return
        
        for processo in reversed(fila):
            if processo != fila[0]:
                print(f"({processo.getId()})({processo.getPrioridade()})[{processo.getTempoExecucao()}][{processo.getTempoEspera()}]({processo.getEstado()}) -> ", end="")
                continue
            print(f"({processo.getId()})({processo.getPrioridade()})[{processo.getTempoExecucao()}][{processo.getTempoEspera()}]({processo.getEstado()})")