gabarito = ['A', 'B', 'C', 'D', 'B', 'A', 'B', 'A', 'C', 'B']
notas = []


while True:
    acertos = 0

    for i in range(10):
        resposta = input(f"Questão {i}: ")
        if resposta == gabarito[i]:
            acertos += 1

    print(f"voce acertou {acertos} questões")
    notas.append(acertos)

    continuar = input("Outro aluno vai fazer a prova (S/N): ")
    
    if continuar != "s":
        break


total_alunos = len(notas)
maior = max(notas)
menor = min(notas)
media = sum(notas) / total_alunos


print(f"Total de alunos: {total_alunos}")
print(f"Maior número de acertos: {maior}")
print(f"Menor número de acertos: {menor}")
print(f"Média da turma: {media:.2f}")



    

 
    
