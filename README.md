# DevOps API

API desenvolvida com **FastAPI** para demonstrar práticas DevOps em um ambiente containerizado com pipeline CI/CD automatizado.

##  Stack

- **Python 3.12** + **FastAPI**
- **Docker** + **Docker Compose**
- **GitHub Actions** — pipeline CI/CD
- **Render** — deploy em nuvem

##  Pipeline CI/CD

A cada push na branch main:
1. GitHub Actions instala dependências
2. Roda os testes com pytest
3. Se passar, faz deploy automático no Render

##  Como rodar localmente

    git clone https://github.com/suportehanks2026/devops-api.git
    cd devops-api
    docker compose up --build

Acesse: http://localhost:9000

##  Rodar testes

    pip install -r requirements.txt
    pytest test_main.py -v

##  Endpoints

| Método | Rota | Descrição |
|---|---|---|
| GET | / | Retorna status da API |
| GET | /health | Health check |

##  Deploy

API disponível em: https://devops-api-kta8.onrender.com
