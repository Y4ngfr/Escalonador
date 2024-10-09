# Sobre

O **Escalonador** é um simulador de escalonador de processos de um sistema operacional.
Um escalonador de processos é um componente de sistemas operacionais modernos que gerencia uma fila de processos com base em algum método ou algoritmo.
Os principais são: 

- **First Come First Served (FCFS)**: a prioridade se dá de acordo com a ordem de chegada de cada processo, nesse caso, o primeiro a chegar é o primeiro a ser "servido".

- **Shortest Job First (SJF)**: a prioridade se dá de acordo com o tempo de execução total do processo, nesse caso, o processo com menor tempo de execução será o primeiro a executar.

- Shortest Remaining Time First (SRT)

- **Roud-robin**: O escalonador define um quantum (fatia de tempo) para cada processo. Quando o quantum termina, o processo deve ceder a CPU para outro.

- Randomic

O **Escalonador** implementa os algoritmos FCFS e SJF com round-robin.

# Pré-requisitos

Antes de executar o programa, é necessário garantir que o Python 3 esteja instalado em sua máquina. Para usuários Debian:
$
```
sudo apt install python3
```

Além disso, o Git também deve estar instalado para que o repositório seja clonado:
$
```
sudo apt install git
```

Clone o repositório do projeto com o comando:
$
```
git clone https://github.com/Y4ngfr/Escalonador.git
```

Após clonar o repositório, acesse a pasta do projeto e execute o arquivo main.py:
$
```
python3 src/main.py
```

# Funcionamento do Simulador

A cada passo na simulação, o programa realiza as seguintes operações:

+ Criação de um novo processo (com 69% de chance)
+ Adição do processo à fila de processos
+ Exibição das filas de processos e de espera
+ Execução do primeiro processo da fila, se disponível
+ Atualização das filas de processos e de espera

No inicio da execução do programa, deve-se selecionar o algoritmo desejado (entre FCFS e SJF) e o quantum (recomendado 30 para SJF). Após isso, pressione enter para avançar um passo na execução do programa.    

A impressão das filas segue o padrão:
(IdProcesso) (Prioridade) [TempoExecução] [TempoEspera] (Estado)

# Arquitetura do Sistema

A arquitetura do simulador é composta por quatro componentes principais: Escalonador, Processo, Sistema Operacional e Despachante

# Escalonador

O escalonador gerencia as filas de processos e de espera de acordo com o algoritmo selecionado. Ele é composto por três classes principais:

+ **EscalonadorAbstrato:** Define os atributos e métodos gerais que serão utilizados pelas classes derivadas.
+ **EscalonadorFCFS:** Implementa o algoritmo FCFS, onde os processos são adicionados à fila de acordo com a ordem de chegada.
+ **EscalonadorSJF:** Implementa o algoritmo SJF, onde os processos são ordenados na fila de acordo com o tempo de execução.

Na fila de espera o algoritmo implementado é o FCFS independentemente do algoritmo escolhido pelo usuário.

# Processos

Cada processo possui um identificador (ID), tempo de execução, estado (Pronto, Esperando, Executando ou Terminado), tempo de espera e prioridade. Quando um processo necessita de entrada do usuário, ele é movido para a fila de espera e quando um processo é terminado, ele é removido da fila de processos.

# Sistema Operacional

O Sistema Operacional centraliza e organiza as interações entre o escalonador, processos e o despachante, fornecendo modularidade ao projeto.
Ele é implementado na classe SO, e possui um escalonador e um despachante, que serão únicos durante todo o fluxo de execução do programa.

# Despachante

O Despachante é responsável por encapsular o contexto onde o processo é executado. Ele aloca o quantum para a execução de um processo e garante a sua execução dentro desse tempo. Ele recebe o processo escolhido pelo escalonador e o gerencia até que seu quantum termine.

# Estudo de Caso

Para demonstrar o desempenho dos algoritmos implementados, foi realizado um teste utilizando o seguinte conjunto de processos:

![alt text](tabela_processos.png)

Ao final das duas execuções os seguintes resultados foram obtidos:

# Resultado FCFS

![alt text](resultado_fcfs.png)

tempo médio de turnaround: 138.5

# Resultado SJF

![alt text](resultado_sjf.png)

tempo médio de turnaround: 96.6

## Análise dos resultados

Os testes revelam que o tempo médio de turnaround no algoritmo SJF é significativamente menor em comparação com o FCFS. Isso ocorre porque o SJF prioriza processos com menor tempo de execução, otimizando o uso da CPU. No entanto, o SJF pode causar starvation em processos com tempos de execução longos, que podem ficar indefinidamente na fila.

Uma solução para o problema de starvation é incrementar a prioridade de processos que esperam por muito tempo, embora isso adicione complexidade ao algoritmo.