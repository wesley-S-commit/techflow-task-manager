# src/task_manager.py (Adicione este método à classe TaskManager)

    def update_task_status(self, task_id, new_status):
        """
        Atualiza o status de uma tarefa para refletir o quadro Kanban.
        Os status permitidos são: 'A Fazer', 'Em Progresso' ou 'Concluído'.
        """
        valid_status = ["A Fazer", "Em Progresso", "Concluído"] # Colunas obrigatórias [cite: 13]
        
        if new_status not in valid_status:
            return {"success": False, "message": "Status inválido."}

        for task in self.tasks:
            if task.id == task_id:
                task.status = new_status
                return {
                    "success": True, 
                    "message": f"Status da tarefa {task_id} atualizado para {new_status}.",
                    "task": vars(task)
                }
        
        return {"success": False, "message": "Erro: Tarefa não encontrada."}