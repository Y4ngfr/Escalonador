# ESTADOS DO PROCESSO -> EXECUTANDO -> ESPERANDO -> TERMINADO
import time
from src.models.processo import Processo
from src.models.escalonador import Escalonador
from src.models.despachante import Despachante

if __name__ == "__main__":
    algoritimo_vez = "FIFO"
    escalonador = Escalonador()
    despachante = Despachante()
    while(True):
        time.sleep(3)
        processo = Processo()
        escalonador.add_fila_processo(processo=processo, tipo_algoritimo=algoritimo_vez)
