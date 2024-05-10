from termcolor import colored

def imprimir_texto_cor(texto,cor="blue"):
    print(colored(texto,cor))
def Troco (pagar, dinheiro):
    if dinheiro <0:
        imprimir_texto_cor("nao tens dinheiro","red")
        return None
    else:
        dinheiro = dinheiro - pagar
        imprimir_texto_cor(f"pagou {pagar} e ficou com {dinheiro}", "green")
        return dinheiro
carteira = 100
carteira = Troco(50,carteira)
if carteira!=None:
    print(f"Tem na carteira {carteira}")
else:
    print("não tem dinheiro na carteira")