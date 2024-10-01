import processo

class Escalonador:
    def __init__(self) -> None:
        self.fila_processos = []
        self.fila_espera = []
    
    def atualiza_fila_processos(self):
        if len(self.fila_processos) > 0:
            if self.fila_processos[0].estado == "ESPERANDO":
                # Se o processo tiver esperando, removemos da lista de processos e 
                # colocamos na lista de espera
                self.fila_espera.append(fila_processos[0])
                self.fila_processos.pop(0)

            if self.fila_processos[0].estado == "TERMINADO":
                # Se o processo tiver terminado, apenas o removemos da lista de 
                # processos
                self.fila_processos.pop(0)

    def atualiza_fila_espera(self):
        if len(self.fila_espera) > 0:
            self.fila_espera[0].tempo_espera -= 1

    def chamar_despachante(self):
        executar_processo(self.fila_processos[0])
        
    def add_fila_processo(self, processo, tipo_algoritimo: str):
        if(tipo_algoritimo == "FIFO"):
            self.fila_processos.append(processo)
        
