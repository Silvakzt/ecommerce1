~ Projeto Ecommerce

mini mercado virtual online feito com Flask

📁 __init__.py

Função:

Cria a aplicação Flask

Configura o banco de dados SQL

Inicia o SQL

Importa as rotas do sistema

Responsável por:

Inicialização do sistema

Conexão com o banco

Estrutura principal da aplicação

📁 models.py

Função:

Define as tabelas do banco de dados

Define os campos de cada tabela

Define o relacionamento entre User e Item

Tabelas criadas:

User

Item

Também define regras como:

Campos únicos

Campos obrigatórios

Valor padrão do saldo (5000)

📁 routes.py

Função:

Define as rotas (URLs) do sistema

Controla qual página será exibida

Busca dados no banco para enviar aos templates

Atualmente possui:

Rota da Home

Rota de listagem de produtos

📁 templates/base.html

Função:

Template base do sistema

Define layout padrão

Contém navbar

Importa Bootstrap

Define blocos reutilizáveis

Serve como estrutura principal das páginas.

📁 templates/home.html

Função:

Página inicial do sistema

Estende base.html

Define título e conteúdo da home

📁 templates/produtos.html

Função:

Página que lista os produtos

Recebe dados do banco

Usa loop Jinja para mostrar os itens

Exibe tabela com produtos

Rota	Método	O que faz	Template usado

/	GET	Exibe a página inicial	home.html

/produtos	GET	Busca todos os itens no banco e exibe na tabela	produtos.html

✅ SEÇÃO 4 – BANCO DE DADOS

Banco utilizado:

mercado.db

Tipo:

SQLite

🔎 Quais tabelas existem?

Existem duas tabelas:

User

Item

🔑 Quais são as chaves primárias?

User

id (Integer, primary_key=True)

Item

id (Integer, primary_key=True)

🔗 Existe relacionamento? Qual?

Sim.

Relacionamento:

1 Usuário → Muitos Itens

Tipo:

One-to-Many (Um para Muitos)

Como funciona:

A tabela Item possui uma chave estrangeira:

dono = db.ForeignKey('user.id')

A tabela User possui:

itens = db.relationship('Item')

Isso significa que:

Um usuário pode possuir vários itens

Cada item pertence a apenas um usuário

✅ SEÇÃO 5 – TEMPLATES

❓ O que é extends?

extends é usado para herdar um template base.

Exemplo:

{% extends 'base.html' %}

Isso significa:

O arquivo herda toda estrutura de base.html

Apenas substitui os blocos definidos

❓ O que é block?

block define áreas substituíveis dentro do template.

Exemplo em base.html:

{% block conteudos %}{% endblock %}

Depois em outra página:

{% block conteudos %}

Conteúdo específico

{% endblock %}

Serve para:

Reutilizar layout

Evitar repetição de código

❓ Por que usamos base.html?

Para:

Centralizar layout

Manter padrão visual

Evitar repetir navbar em todas as páginas

Facilitar manutenção

Se precisar mudar o menu:

Altera apenas em base.html

Todas páginas atualizam automaticamente

✅ SEÇÃO 6 – COMO EXECUTAR O PROJETO

Banco utilizado:

mercado.db

🧪 1. Criar ambiente virtual

No terminal:

Windows:

python -m venv venv

venv\Scripts\activate

📦 2. Instalar dependências

Instalar Flask e Flask-SQLAlchemy:

pip install flask flask_sqlalchemy

🚀 3. Rodar o projeto

No terminal:

Windows:

set FLASK_APP=mercado

flask run

Depois acessar no navegador:
http://127.0.0.1:5000
