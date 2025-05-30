# Desafio DevOps 2025 - 

## Descrição

Este projeto é composto por dois microsserviços desenvolvidos em linguagens distintas (Python + FastAPI e Node.js + Express), utilizando Redis para cache, e com uma stack completa de Observabilidade (Logs, Métricas e Traces/Opentelemetry) provisionada automaticamente.

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

![Diagrama da Arquitetura](diagram.png)

---

## Executando o Projeto

### Pré-requisitos
- Docker
- Docker Compose

### Comandos para subir o ambiente:

```bash
docker-compose up -d

### Comandos para parar o ambiente:

```bash
docker-compose down

## Endpoints das Aplicações

| Serviço   | Endpoint                     | Função                      |
| --------- | ---------------------------- | --------------------------- |
| **App 1** | `http://localhost:8000/ping` | Healthcheck                 |
|           | `http://localhost:8000/time` | Retorna horário (cache 10s) |
| **App 2** | `http://localhost:3000/ping` | Healthcheck                 |
|           | `http://localhost:3000/time` | Retorna horário (cache 60s) |


## Acesso aos Serviços

| Serviço        | URL                                            | Login       |
| -------------- | ---------------------------------------------- | ----------- |
| **Grafana**    | [http://localhost:3001](http://localhost:3001) | admin/admin |
| **Prometheus** | [http://localhost:9090](http://localhost:9090) | -           |
| **Loki**       | Logs via Grafana (Explore → Loki)              | -           |
| **Tempo**      | Traces via Grafana (Explore → Tempo)           | -           |

## Volumes Persistentes

| Serviço   | Caminho Local  | Caminho no Container | Função              |
| --------- | -------------- | -------------------- | ------------------- |
| **Loki**  | `./loki-data`  | `/var/loki`          | Logs Persistentes   |
| **Tempo** | `./tempo-data` | `/var/tempo/traces`  | Traces Persistentes |


## Comandos Úteis

| Ação                         | Comando                               |
| ---------------------------- | ------------------------------------- |
| Subir o ambiente             | `docker-compose up -d`                |
| Ver status dos serviços      | `docker ps`                           |
| Acompanhar logs              | `docker-compose logs -f`              |
| Acessar bash de um container | `docker exec -it <container> /bin/sh` |
| Derrubar o ambiente          | `docker-compose down`                 |
| Derrubar e remover volumes   | `docker-compose down -v`              |


## Melhorias Futuras

 Deploy em Kubernetes (EKS, GKE, AKS).
 CI/CD com GitHub Actions ou GitLab CI.
 Automação com o Terraform.
 Escalabilidade horizontal dos apps.
 Monitoramento mais avançado com alertas no Grafana.
 Logs estruturados com enriquecimento.
 Implementação de Redis Cluster para alta disponibilidade.