import os

ARQUIVO_TAREFAS = "tarefas.txt"

def carregar_tarefas():
    if not os.path.exists(ARQUIVO_TAREFAS):
        return []
    with open(ARQUIVO_TAREFAS, "r") as arquivo:
        return [linha.strip() for linha in arquivo.readlines()]

def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, "w") as arquivo:
        for tarefa in tarefas:
            arquivo.write(tarefa + "\n")

def mostrar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        print("\nLista de Tarefas:")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")
    print()

def adicionar_tarefa(tarefas):
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa adicionada!\n")

def remover_tarefa(tarefas):
    mostrar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa para remover: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefas.pop(indice)
            salvar_tarefas(tarefas)
            print("Tarefa removida!\n")
        else:
            print("Número inválido.\n")
    except ValueError:
        print("Entrada inválida.\n")

def main():
    tarefas = carregar_tarefas()
    while True:
        print("1. Mostrar tarefas")
        print("2. Adicionar tarefa")
        print("3. Remover tarefa")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            mostrar_tarefas(tarefas)
        elif escolha == "2":
            adicionar_tarefa(tarefas)
        elif escolha == "3"
            remover_tarefa(tarefas)
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida.\n")

main()
