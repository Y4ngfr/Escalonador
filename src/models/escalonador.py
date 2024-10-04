class Escalonador:
    def __init__(self) -> None:
        self.fila_processos = []
        self.fila_espera = []
        self.algoritmo = ""

    def atualiza_fila_processos(self):
        if len(self.fila_processos) > 0:

            aux = self.fila_processos[0]
            self.fila_processos.pop(0)
            self.fila_processos.append(aux)

            for i, processo in enumerate(self.fila_processos):
                if processo.getEstado() == "ESPERANDO": 
                    self.fila_espera.append(processo)
                    self.fila_processos.pop(i)
                if processo.getEstado() == "TERMINADO":
                    self.fila_processos.pop(i)

    def atualiza_fila_espera(self):
        if len(self.fila_espera) > 0:
            
            aux = self.fila_espera[0]
            self.fila_espera.pop(0)
            self.fila_espera.append(aux)

            for i, processo in enumerate(self.fila_espera):
                if processo.getEstado() == "PRONTO":
                    self.fila_processos.append(processo)
                    self.fila_espera.pop(i)

    def inserir_entrada(self):
        if len(self.fila_espera) > 0:
            self.fila_espera[0].tempo_espera -= 1
            if self.fila_espera[0].tempo_espera == 0:
                self.fila_espera[0].setEstado("PRONTO")

    def add_fila_processo(self, processo):
        if(self.algoritmo == "FIFO"):
            self.fila_processos.append(processo)

    def setAlgoritmo(self, algoritmo):
        if algoritmo != "FIFO":
            print("Algoritmo inválido")
            return -1
        self.algoritmo = algoritmo
        return 0