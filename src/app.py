from tarefas import *

while True:
    print("\n===== GERENCIADOR DE TAREFAS =====")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Editar tarefa")
    print("4 - Remover tarefa")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome da tarefa: ")
        adicionar_tarefa(nome)
        print("Tarefa adicionada com sucesso!")

    elif opcao == "2":
        lista = listar_tarefas()

        if not lista:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\nLista de tarefas:")
            for i, tarefa in enumerate(lista, start=1):
                print(f"{i}. {tarefa}")

    elif opcao == "3":
        lista = listar_tarefas()

        for i, tarefa in enumerate(lista, start=1):
            print(f"{i}. {tarefa}")

        indice = int(input("Número da tarefa: ")) - 1
        novo_nome = input("Novo nome: ")

        if editar_tarefa(indice, novo_nome):
            print("Tarefa atualizada com sucesso!")
        else:
            print("Tarefa não encontrada.")

    elif opcao == "4":
        lista = listar_tarefas()

        for i, tarefa in enumerate(lista, start=1):
            print(f"{i}. {tarefa}")

        indice = int(input("Número da tarefa: ")) - 1

        if remover_tarefa(indice):
            print("Tarefa removida com sucesso!")
        else:
            print("Tarefa não encontrada.")

    elif opcao == "5":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")