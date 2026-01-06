# src/task_manager.py

class TaskManager:
    def __init__(self):
        # Lista para armazenar as tarefas (simulando um banco de dados)
        self.tasks = []

    def create_task(self, title, description, priority="Média"):
        """Adiciona uma nova tarefa ao sistema."""
        if not title:
            return "Erro: Título é obrigatório"
        
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "description": description,
            "priority": priority,
            "status": "A Fazer"
        }
        self.tasks.append(task)
        return task

    def get_all_tasks(self):
        """Retorna todas as tarefas."""
        return self.tasks

    def update_task_status(self, task_id, new_status):
        """Atualiza o status de uma tarefa específica."""
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = new_status
                return task
        return None

    def delete_task(self, task_id):
        """Remove uma tarefa pelo ID."""
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                return self.tasks.pop(i)
        return None