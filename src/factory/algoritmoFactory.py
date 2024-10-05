from models.escalonadorFIFO import EscalonadorFIFO
from models.escalonadorSJF import EscalonadorSJF

class AlgoritmoFactory: 
    def defineAlgoritimo(algoritmo):
        algoritmo = algoritmo.upper()
        if algoritmo == "FIFO":
            return EscalonadorFIFO
        if algoritmo == "SJF":
            return EscalonadorSJF
        
        raise Exception("O algoritmo inserido é invalido.")
        