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
        print("Processos: ", end="")

        if len(self.escalonador.fila_processos) > 0:
            for processo in reversed(self.escalonador.fila_processos):
                if processo != self.escalonador.fila_processos[0]:
                    print(f"(Id:{processo.getId()})[{processo.getTempoExecucao()}][{processo.getTempoEspera()}]({processo.getEstado()}) -> ", end="")
                else:
                    print(f"(Id:{processo.getId()})[{processo.getTempoExecucao()}][{processo.getTempoEspera()}](EXECUTANDO)")
        else:
            print("<Fila vazia>")
        
        print("Espera: ", end="")
        if len(self.escalonador.fila_espera) > 0:
            for processo in reversed(self.escalonador.fila_espera):
                if processo != self.escalonador.fila_espera[0]:
                    print(f"(Id:{processo.getId()})[{processo.getTempoExecucao()}][{processo.getTempoEspera()}]({processo.getEstado()}) -> ", end="")
                else:
                    print(f"(Id:{processo.getId()})[{processo.getTempoExecucao()}][{processo.getTempoEspera()}]({processo.getEstado()})")
        else:
            print("<Fila vazia>")
        
        if len(self.escalonador.fila_processos) > 0:
            self.despachante.executar_processo(self.escalonador.fila_processos[0])
        
        self.escalonador.inserir_entrada()
        self.escalonador.atualiza_fila_processos()
        self.escalonador.atualiza_fila_espera()