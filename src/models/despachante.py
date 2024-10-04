import time
import random

class Despachante:
    def __init__(self):
        self.round_robin = 5

    def executar_processo(self, processo):
        processo.setEstado("EXECUTANDO")
        tempo = 0

        while(  
            processo.estado == "EXECUTANDO" and
            tempo < self.round_robin
        ):
            processo.executa()
            processo.atualiza_estado()
            processo.verifica_entrada_saida()
            tempo += 1
