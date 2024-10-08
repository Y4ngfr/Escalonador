from abc import ABC, abstractmethod

class Escalonador(ABC):
    def __init__(self) -> None:
        self.fila_processos = []
        self.fila_espera = []
        self.algoritmo = ""
        
    def getAlgoritmo(self):
        return self.algoritmo    

    def atualiza_fila_processos(self):
        if self._verifica_fila_sem_item(self.fila_processos):
            return
        
        aux = self.fila_processos[0]

        if aux.getEstado() != "EXECUTANDO":
            self.fila_processos.pop(0)
            self.fila_processos.append(aux)

        for i, processo in enumerate(self.fila_processos):
            if processo.getEstado() == "ESPERANDO": 
                self.fila_espera.append(processo)
                self.fila_processos.pop(i)
                
            if processo.getEstado() == "TERMINADO":
                self.fila_processos.pop(i)

    def atualiza_fila_espera(self):
        if self._verifica_fila_sem_item(self.fila_espera):
            return
        
        aux = self.fila_espera[0]
        self.fila_espera.pop(0)
        self.fila_espera.append(aux)
        
        for i, processo in enumerate(self.fila_espera):
            if processo.getEstado() == "PRONTO":
                self.add_fila_processo(processo=processo)
                self.fila_espera.pop(i)

    def inserir_entrada(self):
        if self._verifica_fila_sem_item(self.fila_espera):
            return 
        
        self.fila_espera[0].tempo_espera -= 1
        if self.fila_espera[0].tempo_espera == 0:
            self.fila_espera[0].setEstado("PRONTO")

    def _verifica_fila_sem_item(self, fila):
        return len(fila) <= 0

    @abstractmethod
    def setAlgoritmo(self):
        pass
    
    @abstractmethod
    def add_fila_processo(self, processo):
        pass