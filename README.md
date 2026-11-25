# Banking Cloud Platform

End-to-end AWS DevOps project for a banking microservices platform. It covers infrastructure as code, CI/CD, containers, Kubernetes and monitoring.

## Tech stack

AWS, Terraform, Jenkins, Docker, Amazon EKS, SonarQube, Prometheus, Grafana, Bash, GitHub

## Project structure

| Folder | Purpose |
|---|---|
| `services/` | Banking microservices (account-service, transaction-service) |
| `terraform/` | AWS infrastructure as code (modules and dev/staging/prod environments) |
| `jenkins/` | CI/CD pipeline files |
| `k8s/` | Kubernetes manifests |
| `monitoring/` | Prometheus and Grafana configuration |
| `scripts/` | Bash automation scripts |
| `docs/` | Notes and incident write-ups |

## Scripts

| Script | What it does |
|---|---|
| `scripts/setup-tools-server.sh` | Checks and installs the tools needed on a fresh server |
| `scripts/health-check.sh` | Checks disk, memory and service health. Exit code 0 is healthy, 1 is a problem |
| `scripts/deploy.sh <dev\|staging\|prod>` | Pulls the latest code, restarts the service and verifies health |

## Services

**account-service** (port 5001): runs as a systemd service with automatic restart.
- `GET /health` returns the service status
- `GET /accounts/1001` returns a demo account

## Progress

- [x] Day 1: Linux server setup, Git workflow, Bash automation, first service
- [ ] Day 2: Terraform (AWS network and environments)
- [ ] Day 3: IAM least privilege
- [ ] Day 4: Jenkins CI/CD and SonarQube
- [ ] Day 5: Docker
- [ ] Day 6 and later: Amazon EKS, Kubernetes, monitoring, production readiness
