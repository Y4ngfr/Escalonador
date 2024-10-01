import random

class Processo:
    def __init__(self):
        self.id = 0
        self.tempo_execucao = 0 # milissegundos
        self.estado = "" # EXECUTANDO, ESPERANDO ou TERMINADO
        self.tempo_espera = 0 # milissegundos

    def executa(self):
        if self.tempo_execucao > 0:
            self.tempo_execucao -= 1

    def verificacao_entrada_saida(self):
        chance = random.randint(1, 100)
        if(chance <= 30):
            self.estado = "ESPERANDO"
            self.tempo_espera = random.randint(1, 10)
    
    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def setEstado(self, estado):
        if estado != "EXECUTANDO" and estado != "ESPERANDO" and estado != "TERMINADO":
            print("Estado de processo inválido")
        else:
            self.estado = estado
    
    def getTempoExecucao(self):
        return self.tempo_execucao
    
    def setTempoExecucao(self, tempo_execucao):
        self.tempo_execucao = tempo_execucao