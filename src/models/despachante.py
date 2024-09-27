import time
import random
import processo
class Despachante:
    def executar_processo(self, processo: processo.Processo):
        while(processo.estado == "EXECUTANDO"):
            
            if processo.tempo_execucao == 0:
                processo.estado = "TERMINADO"
                break

            processo.verificacao_entra_saida()
            
            processo.tempo_execucao -= 1
            time.sleep(1)
