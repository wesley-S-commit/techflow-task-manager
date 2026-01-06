# tests/test_task_manager.py
from src.task_manager import TaskManager

def test_create_task():
    manager = TaskManager()
    task = manager.create_task("Entrega Rápida", "Entregar no setor A")
    assert task["title"] == "Entrega Rápida"
    assert len(manager.get_all_tasks()) == 1

def test_create_task_invalid():
    manager = TaskManager()
    result = manager.create_task("", "Sem título")
    assert result == "Erro: Título é obrigatório"

def test_delete_task():
    manager = TaskManager()
    manager.create_task("Teste", "Desc")
    manager.delete_task(1)
    assert len(manager.get_all_tasks()) == 0