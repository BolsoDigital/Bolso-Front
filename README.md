# 💻 Bolso Digital - Frontend (Django)

![Python](https://img.shields.io/badge/python-3.13+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.2.6-092E20?logo=django)


---

## 📝 Descrição

O **Bolso Digital Frontend** é a interface web do projeto **Bolso Digital**, desenvolvida com **Django**.  
Ele permite que usuários façam upload, visualização, edição e exclusão de **comprovantes de pagamento**, interagindo com a **API principal** (desenvolvida em **FastAPI + IA**).

Este módulo atua como **frontend** do sistema, consumindo os endpoints da API para exibir e manipular os dados de despesas de forma intuitiva e responsiva.

---

## 🚀 Funcionalidades

- 📤 Upload de comprovantes (imagem ou PDF)  
- 🧾 Listagem detalhada de pagamentos e despesas  
- ✏️ Edição de informações da despesa (descrição, valor, categoria, método)  
- ❌ Exclusão com confirmação  
- 🌗 Suporte a modo claro/escuro (dark mode)  
- 🔒 Login obrigatório para acesso às despesas  
- 🔗 Comunicação direta com a API FastAPI  

---

## 🛠️ Tecnologias Utilizadas

- [Python 3.13+](https://www.python.org/)
- [Django 5.2.6](https://www.djangoproject.com/)
- [Requests](https://pypi.org/project/requests/) (para comunicação com a API)
- [Bootstrap](https://getbootstrap.com/) + CSS Customizado
- [SQLite](https://www.sqlite.org/) (para dados locais e cache)
- [HTML5](https://developer.mozilla.org/pt-BR/docs/Web/HTML) + [Jinja2 Templates](https://jinja.palletsprojects.com/)

---

## 📋 Pré-requisitos

- Python 3.13+
- Git
- API do **Bolso Digital** rodando localmente (`http://localhost:8000`)

---

## ⚙️ Instalação e Configuração

1. Clone o repositório:
    ```bash
    git clone https://github.com/BolsoDigital/bolso-digital-frontend.git
    cd bolso-digital-frontend
    ```

2. Crie o ambiente virtual e ative:
    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    # ou
    venv\Scripts\activate      # Windows
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Rode as migrações:
    ```bash
    python manage.py migrate
    ```

5. Crie um superusuário:
    ```bash
    python manage.py createsuperuser
    ```

6. Inicie o servidor Django:
    ```bash
    python manage.py runserver 8001
    ```

Acesse o sistema:  
👉 [http://127.0.0.1:8001/bolsoDigital/expenses/](http://127.0.0.1:8001/bolsoDigital/expenses/)

---
