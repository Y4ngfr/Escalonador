from abstratos.EscalonadorAbstrato import Escalonador

class EscalonadorFIFO(Escalonador):
    def __init__(self):
        super().__init__()
        self.setAlgoritmo()
    
    def add_fila_processo(self, processo):
        self.fila_processos.append(processo)
    
    def setAlgoritmo(self):
        self.algoritmo = "FIFO"