# ENTREVISTA COM CLIENTE

## oBJETIVO DO DOCUMENTO
Registra as respostas do cliente que deram origem aos requisitos e as Issues do projeto

📌 Requisitos Funcionais

Cadastro de Usuários
O sistema deve permitir o cadastro de usuários com, no mínimo, nome, e-mail e senha.

Autenticação de Usuários
O sistema deve permitir que usuários façam login utilizando e-mail e senha válidos.

Criação de Tarefas
O usuário deve ser capaz de criar novas tarefas informando título, descrição, prioridade e status.

Listagem de Tarefas
O sistema deve exibir todas as tarefas cadastradas, permitindo visualização geral ou por usuário.

Atualização de Tarefas
O usuário deve poder editar informações de uma tarefa existente (status, prioridade ou descrição).

Exclusão de Tarefas
O sistema deve permitir a exclusão de tarefas previamente cadastradas.

Classificação por Status (Kanban)
As tarefas devem possuir status compatíveis com o Kanban: A Fazer, Em Progresso e Concluído.

📌 Requisitos Não Funcionais

Linguagem e Estrutura do Projeto
O sistema deve ser desenvolvido em Python, com organização clara de pastas (/src, /tests, /docs).

Testes Automatizados
O projeto deve possuir testes automatizados utilizando PyTest, cobrindo pelo menos as funcionalidades principais.

Integração Contínua (CI)
O repositório deve conter um pipeline configurado no GitHub Actions para executar os testes automaticamente a cada commit ou pull request