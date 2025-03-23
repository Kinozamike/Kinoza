# Deployment Guide

## Cloud Deployment
1. **Build Docker Image**  
   ```bash
   docker build -t ai-fintech .
   ```

2. **Run Container**  
   ```bash
   docker run -p 5000:5000 ai-fintech
   ```

3. **Deploy on Kubernetes**  
   ```bash
   kubectl apply -f deployment/k8s.yaml
   ```
