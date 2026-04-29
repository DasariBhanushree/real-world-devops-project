# real-world-devops-project

# real-world-devops-project

## Overview

I built this project to understand how a real DevOps workflow works from code to deployment.

The goal was to take a simple application, containerize it, automate the build process, and deploy it on Kubernetes using AWS EKS.

---

## What I did

* Wrote a simple Python application
* Created a Docker image and pushed it to Docker Hub
* Set up a CI pipeline using GitHub Actions to build and push the image
* Deployed the application to AWS EKS using Kubernetes manifests
* Added probes, resource limits, and scaling
* Exposed the application using a LoadBalancer

---

## Flow

Code → GitHub → CI/CD → Docker Hub → AWS EKS → LoadBalancer

---

## Kubernetes (EKS)

* Deployed application on AWS EKS cluster
* Used Deployment with replicas, readiness and liveness probes
* Added CPU and memory limits
* Exposed service using LoadBalancer
* AWS created an ELB and provided external access

---

## Application URL

http://a3cdab83d0d2f4aa98cb20a53bf4e5a7-108641135.us-east-1.elb.amazonaws.com/

## Commands I used

kubectl get pods
kubectl get svc
kubectl describe pod
kubectl scale deployment my-app --replicas=4
