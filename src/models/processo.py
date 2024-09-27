import random

class Processo:
    def __init__(self):
        self.id = 0
        self.tempo_execucao = 0 # segundos, pq nosso pc é ruim
        self.estado = ""
        self.tempo_espera = 0 #milesegundos

    def verificacao_entra_saida(self):
        chance = random.randint(1, 100)

        if(chance <= 30):
            self.estado = "ESPERANDO"
            self.tempo_espera = random.randint(1, 10)
    
    def getId(self):
        return self.id
    def setId(self, id):
        self.id = id
    
    def getTempoExecucao(self):
        return self.tempo_execucao
    
    def setTempoExecucao(self, tempo_execucao):
        self.tempo_execucao = tempo_execucao
    

    