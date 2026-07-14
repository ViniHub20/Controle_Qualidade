tarefas = []

def adicionar_tarefa(nome):
    tarefas.append(nome)

def listar_tarefas():
    return tarefas

def editar_tarefa(indice, novo_nome):
    if 0 <= indice < len(tarefas):
        tarefas[indice] = novo_nome
        return True
    return False

def remover_tarefa(indice):
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
        return True
    return False