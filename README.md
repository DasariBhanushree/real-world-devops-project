# real-world-devops-project

## Overview

Built an end-to-end DevOps workflow to understand how applications move from code to production.

The project covers containerization, CI/CD automation, and deployment on Kubernetes using AWS EKS.

---

## What I did

- Created a simple Python application  
- Containerized the app using Docker  
- Initially pushed images to Docker Hub, later migrated to AWS ECR  
- Set up CI/CD using GitHub Actions to build and push images  
- Deployed the application to AWS EKS using Kubernetes manifests  
- Configured Ingress for routing traffic  
- Implemented Horizontal Pod Autoscaler (HPA) for auto scaling  
- Added readiness/liveness probes and resource limits  

---

## Flow

Code → GitHub → CI/CD → ECR → EKS → Ingress → HPA → Live Application

---

## Kubernetes (EKS)

- Deployed application on AWS EKS cluster  
- Used Deployment with replicas, readiness, and liveness probes  
- Configured Service (ClusterIP) for internal communication  
- Used NGINX Ingress Controller to expose the application  
- Implemented HPA for scaling based on CPU usage  

---

## Container Registry (Docker Hub → AWS ECR)

- Started with Docker Hub for storing images  
- Migrated to AWS ECR for better integration with AWS  
- Updated CI/CD pipeline to push images to ECR  
- Used ECR images for Kubernetes deployment  

---

## CI/CD Pipeline

- Triggered on code push to GitHub  
- Builds Docker image  
- Pushes image to AWS ECR  
- Updates Kubernetes deployment automatically  

---

## Application Access

Application is exposed using Kubernetes Ingress (via AWS ELB).

---

## Commands Used

```bash
kubectl get pods
kubectl get svc
kubectl get ingress
kubectl get hpa
kubectl top pods
kubectl describe pod <pod-name>

## Architecture

GitHub → GitHub Actions → Docker Build → Push to ECR → Deploy to EKS → Ingress → LoadBalancer → Users

- Code is pushed to GitHub
- CI/CD pipeline builds Docker image
- Image pushed to AWS ECR
- Kubernetes (EKS) deploys the app
- Ingress exposes the service
- HPA handles auto-scaling

[GitHub] → [GitHub Actions] → [Docker] → [ECR] → [EKS]
                                         ↓
                                    [Ingress]
                                         ↓
                                      [Users]


trigger pipeline
