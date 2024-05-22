def calcular_media(notas):
    """
    Função para calcular a média de uma lista de notas.
    :param notas: Lista de notas
    :return: Média das notas
    """
    return sum(notas) / len(notas)

# Lista para armazenar os nomes dos alunos e suas respectivas notas
alunos_notas = {}

# Loop para entrada de dados
while True:
    nome = input("Digite o nome do aluno (ou 'sair' para finalizar): ")
    if nome.lower() == 'sair':
        break

    notas = []
    while True:
        nota = input(f"Digite a nota do aluno {nome} (ou 'fim' para terminar as notas): ")
        if nota.lower() == 'fim':
            break
        try:
            nota = float(nota)
            notas.append(nota)
        except ValueError:
            print("Por favor, digite um valor numérico válido para a nota.")

    alunos_notas[nome] = notas

# Exibir a média de cada aluno
for aluno, notas in alunos_notas.items():
    if notas:
        media = calcular_media(notas)
        print(f"A média das notas do aluno {aluno} é: {media:.2f}")
    else:
        print(f"Não foram inseridas notas para o aluno {aluno}.")

# Mensagem final
print("Programa finalizado.")
