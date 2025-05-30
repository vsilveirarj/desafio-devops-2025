# Desafio DevOps 2025 - Vagner Costa

## Descrição

Este projeto é composto por dois microsserviços desenvolvidos em linguagens distintas (Python + FastAPI e Node.js + Express), utilizando Redis para cache, e com uma stack completa de Observabilidade (Logs, Métricas e Traces/Opentelemetry) provisionada automaticamente.

O ambiente é completamente orquestrado via Docker Compose, com provisionamento automático de dashboards no Grafana e armazenamento persistente dos dados de logs e traces.

## Stack de Serviços

| Serviço     | Tecnologia                     | Função                     |
|--------------|-------------------------------|----------------------------|
| **App 1**    | Python + FastAPI               | API com cache de 10s       |
| **App 2**    | Node.js + Express              | API com cache de 60s       |
| **Redis**    | Redis 7                        | Cache                      |
| **Prometheus**| Prometheus                    | Coleta de Métricas         |
| **Grafana**  | Grafana                        | Dashboards                 |
| **Loki**     | Grafana Loki                   | Logs                       |
| **Tempo**    | Grafana Tempo                  | Traces distribuídos        |

---

## Diagrama da Arquitetura

![Diagrama da Arquitetura](diagrama.png)

---

## Executando o Projeto

### Pré-requisitos
- Docker
- Docker Compose

## Endpoints das Aplicações

| Serviço | Endpoint                  | Função                            |
|---------|----------------------------|------------------------------------|
| **App 1** | `http://localhost:8000/ping` | Healthcheck                       |
|          | `http://localhost:8000/time` | Retorna horário (cache 10 segundos)|
| **App 2** | `http://localhost:3000/ping` | Healthcheck                       |
|          | `http://localhost:3000/time` | Retorna horário (cache 60 segundos)|

---

## Acesso aos Serviços

| Serviço       | URL                                     | Login            |
|----------------|-----------------------------------------|------------------|
| **Grafana**    | [http://localhost:3001](http://localhost:3001) | admin / admin   |
| **Prometheus** | [http://localhost:9090](http://localhost:9090) | -               |
| **Loki**       | Acesso via Grafana → Explore → Loki    | -               |
| **Tempo**      | Acesso via Grafana → Explore → Tempo   | -               |

---

## Volumes Persistentes

| Serviço | Caminho Local | Caminho no Container     | Descrição            |
|---------|----------------|---------------------------|-----------------------|
| **Loki** | `./loki-data` | `/var/loki`               | Logs Persistentes     |
| **Tempo**| `./tempo-data`| `/var/tempo/traces`       | Traces Persistentes   |

---

## Comandos Úteis

| Ação                          | Comando                                  |
|-------------------------------|-------------------------------------------|
| Clonar o projeto              | `git clone git@github.com:SEU-USUARIO/NOME-REPO.git` |
| Acessar a pasta               | `cd NOME-REPO`                           |
| Subir o ambiente              | `docker-compose up -d`                   |
| Ver status dos containers     | `docker ps`                              |
| Acompanhar logs               | `docker-compose logs -f`                 |
| Acessar terminal de um container | `docker exec -it <container> /bin/sh`  |
| Derrubar os containers        | `docker-compose down`                    |
| Derrubar containers + volumes | `docker-compose down -v`                 |

---

## Melhorias Futuras

- [ ] Deploy em ambiente Kubernetes (EKS, GKE, AKS).
- [ ] Pipeline CI/CD com GitHub Actions ou GitLab CI.
- [ ] Automatizar a infraestrutura como código com o Terraform.
- [ ] Alertas configurados no Grafana (Slack, Discord, Telegram, etc.).
- [ ] Logs estruturados com enriquecimento (contexto dos apps).
- [ ] Uso de Redis Cluster para alta disponibilidade.
- [ ] Utilizar Object Storage (S3, MinIO, GCS) para armazenar logs e traces em produção.
- [ ] Escalabilidade horizontal das aplicações.
- [ ] Implementação de observabilidade mais avançada com métricas personalizadas e tracing detalhado.

---

## Passos para Baixar e Executar o Projeto via GitHub

1. **Clone o repositório:**

```bash
#via HTTPS
git clone https://github.com/vsilveirarj/desafio-devops-2025.git

#Comandos para subir o ambiente:
docker-compose up -d
