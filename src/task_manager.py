# src/task_manager.py (Continuação)

    def get_all_tasks(self):
        """
        Retorna a lista completa de tarefas.
        Atende ao requisito de 'acompanhar o fluxo de trabalho'.
        """
        # Retornamos uma lista de dicionários para facilitar a exibição
        return [vars(task) for task in self.tasks]

    def delete_task(self, task_id):
        """
        Remove uma tarefa do sistema pelo ID.
        Retorna True se deletado com sucesso, ou False se o ID não existir.
        """
        original_count = len(self.tasks)
        # Filtra a lista mantendo apenas tarefas com ID diferente do informado
        self.tasks = [task for task in self.tasks if task.id != task_id]
        
        if len(self.tasks) < original_count:
            return {"success": True, "message": f"Tarefa {task_id} removida."}
        
        return {"success": False, "message": "Erro: Tarefa não encontrada."}

#atualização de testes automatizados#

# tests/test_task_manager.py (Adicionar estes testes)

def test_list_tasks():
    manager = TaskManager()
    manager.create_task("Carga A", "Entrega urgente")
    manager.create_task("Carga B", "Entrega normal")
    lista = manager.get_all_tasks()
    assert len(lista) == 2 [cite: 51]
    assert lista[0]["title"] == "Carga A"

def test_delete_task_success():
    manager = TaskManager()
    manager.create_task("Remover", "Esta tarefa será apagada")
    # O ID da primeira tarefa será 1
    resultado = manager.delete_task(1)
    assert resultado["success"] is True [cite: 51]
    assert len(manager.get_all_tasks()) == 0

def test_delete_non_existent_task():
    manager = TaskManager()
    resultado = manager.delete_task(999)
    assert resultado["success"] is False [cite: 51]