from models.escalonadorFIFO import EscalonadorFIFO

class AlgoritmoFactory: 
    def defineAlgoritimo(algoritmo):
        if algoritmo.upper() == "FIFO":
            return EscalonadorFIFO
        if algoritmo.upper() == "SJF":
            return "NOT IMPLEMENTADO!"
        
        raise Exception("O algoritmo inserido é invalido.")
        