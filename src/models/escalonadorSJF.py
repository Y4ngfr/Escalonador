from abstratos.EscalonadorAbstrato import Escalonador

"""
 // Baseado com o que está escrito no pdf no moodle
 // toda vez que for definir / um processo executado, decrementa o valor de todos e reorganiza o vetor
 // toda vez que um processo é colocado na fila, organiza a list pelo menor tempo e atualiza as prioridades

"""

class EscalonadorSJF(Escalonador):
    def __init__(self):
        super().__init__()
    def organiza_fila_processos(self):
        executando = None
        for i, processo in enumerate(self.fila_processos):
            processo.setPrioridade(processo.getPrioridade()+1)
            self.fila_processos[i] = processo
            # verifica se um processo esta executando, para jogar de volta para primeiro (não-preemptivo)
            if processo.getEstado() == "EXECUTANDO":
                executando = processo
                self.fila_processos.pop(i)
                
        self.fila_processos = sorted(self.fila_processos, key=lambda processo: processo.getPrioridade(), reverse=True)
        if executando != None:
            self.fila_processos.insert(0,executando) # joga pro inicio da lista para continuar executando
            
    def add_fila_processo(self, processo):
        self.fila_processos.append(processo)
        self.organiza_fila_processos()
    
    def setAlgoritmo(self):
        self.algoritmo = "SJF"
        
    