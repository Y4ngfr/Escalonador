import random

class Processo:
    id_estatico = 0
    def __init__(self):
        self.id = Processo.id_estatico
        Processo.id_estatico += 1
        self.tempo_execucao = random.randint(1, 30)
        self.estado = "PRONTO"
        self.tempo_espera = 0
        # a ideia é quanto maior o numero da prioridade, mais prioritario ele é
        self.prioridade = 30 - self.tempo_execucao # Atributo desconsiderado no FIFO
        
    def executa(self):
        if self.tempo_execucao > 0:
            self.tempo_execucao -= 1

    # def verifica_entrada_saida(self):
    #     if self.estado != "TERMINADO" and random.randint(1, 100) <= 10:
    #         self.estado = "ESPERANDO"
    #         self.tempo_espera = random.randint(1, 3)
    
    def getId(self):
        return self.id

    def getEstado(self):
        return self.estado

    def setEstado(self, estado):
        if estado != "EXECUTANDO" and estado != "ESPERANDO" and estado != "TERMINADO" and estado != "PRONTO":
            print("Estado de processo inválido")
            return -1
        self.estado = estado
        return 0
    
    def getTempoExecucao(self):
        return self.tempo_execucao
    
    def setTempoExecucao(self, tempo_execucao):
        self.tempo_execucao = tempo_execucao

    def getTempoEspera(self):
        return self.tempo_espera
    
    def getPrioridade(self):
        return self.prioridade
    
    def setPrioridade(self, prioridade):
        self.prioridade =  prioridade
        