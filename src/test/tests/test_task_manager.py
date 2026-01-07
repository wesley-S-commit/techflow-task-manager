# tests/test_task_manager.py (Adicionar este teste)

def test_update_task_status():
    manager = TaskManager()
    manager.create_task("Entrega Setor Sul", "Carga de eletrônicos")
    
    # Simula a movimentação da tarefa para 'Em Progresso'
    resultado = manager.update_task_status(1, "Em Progresso")
    
    assert resultado["success"] is True
    assert resultado["task"]["status"] == "Em Progresso"

def test_update_status_invalid():
    manager = TaskManager()
    manager.create_task("Teste", "Desc")
    # Tenta atualizar para um status não previsto no Kanban
    resultado = manager.update_task_status(1, "Aguardando")
    assert resultado["success"] is False