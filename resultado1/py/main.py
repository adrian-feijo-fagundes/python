import database


database.criar_tabela()

while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        descricao = input("Descrição: ")
        database.adicionar_tarefa(descricao)

    elif opcao == "2":
        tarefas = database.listar_tarefas()

        for tarefa in tarefas:
            print(tarefa)

    elif opcao == "3":
        break

    else:
        print("Opção inválida")