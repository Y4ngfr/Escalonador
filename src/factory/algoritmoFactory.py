from models.escalonadorFCFS import EscalonadorFCFS
from models.escalonadorSJF import EscalonadorSJF

class AlgoritmoFactory: 
    def defineAlgoritimo(algoritmo):
        algoritmo = algoritmo.upper()
        if algoritmo == "FCFS":
            return EscalonadorFCFS
        if algoritmo == "SJF":
            return EscalonadorSJF
        
        raise Exception("O algoritmo inserido é invalido.")
        