# src/task_manager.py

class Task:
    """Representa a entidade de uma Tarefa de logística."""
    def __init__(self, task_id, title, description, priority="Média"):
        self.id = task_id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = "A Fazer"  # Status inicial obrigatório no Kanban

class TaskManager:
    """Gerencia o ciclo de vida das tarefas."""
    def __init__(self):
        self.tasks = []

    def create_task(self, title, description, priority="Média"):
        """
        Lógica para criar uma nova tarefa.
        Inclui validação básica conforme as boas práticas de Engenharia de Software.
        """
        # Validação: O título não pode ser vazio
        if not title or title.strip() == "":
            return {"success": False, "message": "Erro: O título da tarefa é obrigatório."}

        # Geração de ID incremental simplificada
        new_id = len(self.tasks) + 1
        
        # Instanciação da classe Task
        new_task = Task(new_id, title, description, priority)
        
        # Armazenamento na lista (simulando banco de dados)
        self.tasks.append(new_task)
        
        return {
            "success": True, 
            "message": "Tarefa criada com sucesso!", 
            "task": vars(new_task)
        }