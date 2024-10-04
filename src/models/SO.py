from models.escalonador import Escalonador
from models.despachante import Despachante
from models.processo import Processo
import random

class SO:
    def __init__(self, algoritmo):
        self.despachante = Despachante()
        self.escalonador = Escalonador()
        if self.escalonador.setAlgoritmo(algoritmo) < 0:
            self.escalonado.setAlgoritmo("FIFO")

    def step(self):
        if random.randint(1, 100) < 21:
            processo = Processo()
            self.escalonador.add_fila_processo(processo=processo)

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
                print(f"(Id:{processo.getId()})[{processo.getTempoExecucao()}][{processo.getTempoEspera()}]({processo.getEstado()}) -> ", end="")
                continue
            print(f"(Id:{processo.getId()})[{processo.getTempoExecucao()}][{processo.getTempoEspera()}]({processo.getEstado()})")