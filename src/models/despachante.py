import time
import random

class Despachante:
    def __init__(self, round_robin):
        self.round_robin = round_robin
        self.tempo = 0

    def executar_processo(self, processo):
        # if random.randint(1, 100) <= 30:
        #     processo.setEstado("ESPERANDO")
        #     processo.tempo_espera = random.randint(1, 3)
        #     self.tempo = 0
        # else:
        processo.setEstado("EXECUTANDO")

        if(  
            processo.getEstado() == "EXECUTANDO" and
            self.tempo < self.round_robin
        ):
            processo.executa()
            self.tempo += 1

        if processo.getTempoExecucao() == 0:
            processo.setEstado("TERMINADO")
            self.tempo = 0

        elif self.tempo == self.round_robin:
            processo.setEstado("PRONTO")
            self.tempo = 0