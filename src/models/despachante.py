import time
import random

class Despachante:
    def __init__(self):
        self.round_robin = 5

    def executar_processo(self, processo):
        tempo = 0
        while(processo.estado == "EXECUTANDO" and tempo < self.round_robin):

            if processo.tempo_execucao == 0:
                processo.estado = "TERMINADO"
                break

            # processo.verificacao_entra_saida()

            if processo.estado == "ESPERANDO":
                break

            processo.executa()
            tempo += 1
