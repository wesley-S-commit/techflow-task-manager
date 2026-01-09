# tests/test_task_manager.py

def test_create_task_without_title():
    """
    Testa se o sistema impede a criação de uma tarefa com título vazio.
    Garante que a regra de negócio de 'campo obrigatório' seja respeitada.
    """
    manager = TaskManager()
    
    # Tentativa 1: Título vazio
    resultado_vazio = manager.create_task("", "Descrição qualquer")
    
    # Tentativa 2: Título apenas com espaços em branco
    resultado_espacos = manager.create_task("   ", "Descrição qualquer")
    
    # Verificações (Asserções)
    assert resultado_vazio["success"] is False
    assert resultado_vazio["message"] == "Erro: O título da tarefa é obrigatório."
    
    assert resultado_espacos["success"] is False
    assert len(manager.get_all_tasks()) == 0