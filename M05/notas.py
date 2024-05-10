turma={
    123:{"M01":10,"M02":15,"M03":8},
    124:{"M01":10,"M02":15,"M03":18},
    125:{"M01":12,"M02":11,"M03":10}
}
#mostrar as notas dos alunos
for chave,valor in turma.items():
    print (f"nr de processo: {chave}")
    for modulo,nota in valor.items():
        print (f"{modulo=}-{nota=}")
    print ("- - "*20)


#calcular e mostrar as médias de cada aluno e caluclar o aluno com a maior média~
"""
for chave,valor in turma.items():
    média = 0
    print (f"nr de processo: {chave}")
    for modulo,nota in valor.items():
        média += nota
    print (f"a média das notas é {média/(len(valor)):0.2f}")
    print ("- - "*20)
"""
melhor_media = 0
for chave, valor in turma.items():
    notas_aluno=valor.values()
    média=sum(notas_aluno)/len(notas_aluno)
    if média > melhor_media:
        melhor_media = média
        melhor_aluno = chave
    print (f"{chave} - média = {média:.2f}")



#calcular negativas e positivas
for chave,valor in turma.items():
    negativas = 0
    positivas = 0
    print (f"nr de processo: {chave}")
    for modulo,nota in valor.items():
        if nota >= 10:
            positivas += 1
    print (f"teve {positivas} positivas e {len(nota)-positivas} negativas")
    print ("- - "*20)

print (f"a melhor média foi {melhor_media:0.2f} do aluno: {melhor_aluno}")
