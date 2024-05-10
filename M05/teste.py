animais = {("cão","pitbull"):{"idade":5,"dono":"joaquim"},
           ("gato","persa"):{"idade":6,"dono":"joaquim"},
           ("tartaruga","ninja"):{"idade":9,"dono":"ana"},
           ("priquito","preto"):{"idade":18,"dono":"joaquim"},
           ("priquito","pitbull"):{"idade":1,"dono":""},
           ("cão","ninja"):{"idade":10,"dono":"ana"},
           ("gato","preto"):{"idade":5,"dono":"joaquim"},
           }

animaisdojoaquim = "o joaquim tem "

maior_idade = -1

#listar quantaos animai á de cada raça
contagem = {}
for chaves in animais.keys():
    espécie = chaves[0]
    if espécie in contagem:
        contagem[espécie] += 1
    else:
        contagem[espécie] = 1
print (contagem)


#listar os animais do joaquim
for chave,valor in animais.items():
    if valor["dono"] == "joaquim":
        animaisdojoaquim += f"{chave[0]} {chave[1]}, "
    if valor["idade"] > maior_idade:
        maior_idade = valor["idade"]
        animal = chave

print (animaisdojoaquim)

#mostrar o animal mais velho por mim
print("o animal mais velho é {animal[0]} {animal[1]}")

#calcular a média das idades
contar = 0
for valor in animais.values():
    idade = valor["idade"]
    contar += idade
média = contar/len(animais)
print (f"a média das idades é é {média}")
acima_média = "os animais acima da média são "

for chave,valor in animais.items():
    idade = valor["idade"]
    if idade > média:
        acima_média += f"{chave[0], }"
print (acima_média)

total_animais = len(contagem)
for chave,valor in contagem.items():
    print(f"a percenteagem de {chave} é de {(valor/len(animais)*100)}")