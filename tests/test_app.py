import sys
import os

sys.path.append(os.path.abspath("src"))

from tarefas import *

def test_adicionar_tarefa():
    tarefas.clear()
    adicionar_tarefa("Estudar Python")
    assert len(tarefas) == 1
    assert tarefas[0] == "Estudar Python"

def test_editar_tarefa():
    tarefas.clear()
    adicionar_tarefa("Tarefa Antiga")
    editar_tarefa(0, "Tarefa Nova")
    assert tarefas[0] == "Tarefa Nova"

def test_remover_tarefa():
    tarefas.clear()
    adicionar_tarefa("Excluir")
    remover_tarefa(0)
    assert len(tarefas) == 0