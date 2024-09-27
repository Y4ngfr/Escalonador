class Escalonador:
    def __init__(self) -> None:
        self.fila_processos = []
        self.fila_espera = []
    
    def atualiza_fila(self):
        pass

    def chamar_despachante(self):
        
        

    def add_fila_processo(self, processo, tipo_algoritimo: str):
        if(tipo_algoritimo == "FIFO"):
            self.fila_processos.append(processo)
        
