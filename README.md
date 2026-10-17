# Azure Enterprise DevOps Platform

## Project Overview

This project aims to build an enterprise-style, cloud-native application platform on Microsoft Azure using Infrastructure as Code, containerization, CI/CD automation, and Kubernetes.

The platform will follow practical DevOps workflows, including automated builds, testing, container image publishing, deployment, monitoring, and security.

## Project Objectives

- Provision Azure infrastructure using Terraform.
- Build and containerize an application using Docker.
- Store container images in Azure Container Registry (ACR).
- Deploy the application to Azure Kubernetes Service (AKS).
- Automate CI/CD using GitHub Actions.
- Implement monitoring, logging, and security best practices.
- Document deployment procedures and troubleshooting.

## Technology Stack

- **Cloud:** Microsoft Azure
- **Operating System:** Ubuntu 24.04 (WSL)
- **Infrastructure as Code:** Terraform
- **Version Control:** Git and GitHub
- **CI/CD:** GitHub Actions
- **Containers:** Docker
- **Container Registry:** Azure Container Registry
- **Orchestration:** Azure Kubernetes Service
- **Monitoring:** Azure Monitor and Container Insights

## Repository Structure

```text
azure-enterprise-devops/
├── app/
├── infra/
│   └── terraform/
├── .github/
│   └── workflows/
├── k8s/
├── docs/
├── scripts/
└── README.md
```

## Implementation Status

- [x] Azure subscription verified
- [x] Project resource group created
- [x] Local project structure initialized
- [x] Git repository initialized
- [ ] Application development
- [ ] Terraform infrastructure configuration
- [ ] CI/CD pipeline implementation
- [ ] Container registry integration
- [ ] Kubernetes deployment
- [ ] Monitoring and security validation

## Cost Management

Azure resources will be created only after reviewing quotas, estimated costs, and available subscription credits. Resources that incur charges will be monitored and removed when no longer required.

## Disclaimer

This is a hands-on learning project designed to demonstrate enterprise-style DevOps practices. Production readiness will require additional security, reliability, governance, and performance validation.
