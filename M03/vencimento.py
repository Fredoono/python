"""
Programa para calcular o vencimento de um trabalhador.
O programa deve começar por solicitar ao trabalhador que indique o seu nome , quantas horas trabalhou por dia,
e quanto ganha por hora. Caso o trabalho tenho mais do que 8 horas de trabalho deve receber,
por cada hora extra recebe mais 25%. Caso tenho trabalho mais do que 10 horas por dia deve receber 50% por cada hora além das 10 horas.
"""

def PedirNomeTrabalhador():
    """Esta função deve pedir o nome do trabalhador. O nome deve ter pelo menos 3 letras."""
    while True:
        nome = input("insira o seu nome: ")
        if len(nome) >= 3:
            return nome

def PedirHorasTrabalho():
    """Esta função pede ao utilizador quantas horas trabalho no dia. O nº de horas deve ser superior a zero."""
    while True:
        horas = int(input("insira as horas em que trabalha por dia: "))
        if horas > 0:
            return horas

def PedirOrdenado():
    """Esta função pede ao utilizado quanto ganha por cada hora de trabalho"""
    
    ganho = float(input("insira o quanto ganha por hora: "))
    return ganho

def MostrarVencimento(nome,horas,ordenado_por_hora):
    """Esta função deve mostrar o nome do trabalhador e quanto é que deve receber pela dia de trabalho"""
    print (nome)
    
    if horas <= 8:
        print (horas * ordenado_por_hora)
    if horas > 8 and horas <= 10:
        horasEX = horas - 8
        if horasEX > 2:
            horasEX == 2
        print (horas * ordenado_por_hora + horasEX *0.25 * ordenado_por_hora)
    else:
        horasEX = horas - 8
        if horasEX > 2:
            horasEX == 2
        horasEXEX = horas - 10
        print (horas * ordenado_por_hora + (horasEX * ordenado_por_hora * 0.25) + (ordenado_por_hora * horasEXEX *0.50))

def main():
    nome=PedirNomeTrabalhador()
    horas=PedirHorasTrabalho()
    ordenado_por_hora=PedirOrdenado()
    MostrarVencimento(nome,horas,ordenado_por_hora)

if __name__ == "__main__":
    main()
