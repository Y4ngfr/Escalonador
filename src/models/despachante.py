import time
import random
import processo
import escalonador

class Despachante:
    def executar_processo(self, processo: processo.Processo):
        while(processo.estado == "EXECUTANDO"):
            
            if processo.tempo_execucao == 0:
                processo.estado = "TERMINADO"
                break

            processo.verificacao_entra_saida()

            if processo.estado == "ESPERANDO":
                break
            
            processo.executa()
            time.sleep(1)
