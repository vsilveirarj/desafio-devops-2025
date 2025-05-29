# Desafio DevOps 2025 🚀

## 📦 Descrição

Dois microsserviços em linguagens diferentes (Python e Node.js), com cache Redis, observabilidade (Prometheus e Grafana) e infraestrutura orquestrada via Docker Compose.

## 🚀 Executando o Projeto

```bash
docker-compose up -d


🌐 Endpoints
App 1 (FastAPI):

http://localhost:8000/ping
http://localhost:8000/time

App 2 (Node.js):

http://localhost:3000/ping
http://localhost:3000/time


📊 Observabilidade

Prometheus: http://localhost:9090
Grafana: http://localhost:3001
Login padrão: admin/admin

🔧 Componentes

App 1: Python + FastAPI
App 2: Node.js + Express
Redis: Cache
Prometheus: Métricas
Grafana: Dashboards

🚩 Melhorias Futuras

Deploy em Kubernetes.
CI/CD via GitHub Actions.
Adicionar Loki para logs e Tempo para traces.
Redis Cluster para alta disponibilidade.