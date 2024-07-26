## BentoML

BentoML is an open-source model serving library for building performant and scalable AI applications with Python.
It comes with everything you need for serving optimization, model packaging, and production deployment.

1. 🍱 BentoML: The Unified Model Serving Framework
2. 🦾 OpenLLM: Self-hosting Large Language Models Made Easy
3. ☁️ BentoCloud: Inference Platform for fast-moving AI teams

### Why BentoML?
BentoML’s comprehensive toolkit for AI application development provides a unified distribution format, which features a simplified AI architecture and supports deployment anywhere.

### Benefits:
### -- Streamline distribution with a unified format
### -- Build applications with any AI models
### -- Inference optimization for AI applications
### -- Build once. Deploy anywhere

### The following is the basic workflow of using the BentoML framework.

### 1. Model registration
To get started, you can save your model in the BentoML Model Store, a centralized repository for managing all local models. BentoML is compatible with a variety of models, including pre-trained models from Hugging Face or custom models trained on your custom datasets. The Model Store simplifies the process of iterating and evaluating different model versions, providing an efficient way to track and manage your ML assets.

Note that for simple use cases, you can skip this step and use pre-trained models directly when creating your BentoML Service.

### 2. Service creation
You create BentoML Services by defining a service.py file, where you outline your model’s serving logic through class-based Services. In this file, you can define multiple Services for specific tasks like data preprocessing or model predictions if necessary. Each Service can be customized to handle its own input and output logic. You can test model serving and inference by running Services locally. During deploying, each Service can be independently scaled and separately deployed for better resolution utilization.

### 3. Deployment
Before deploying your AI application, you create a bentofile.yaml file, detailing all necessary build configurations such as Python dependencies and Docker settings. After that, you can choose either of the following ways to deploy your application.

With a single command, you deploy your application to BentoCloud. In this approach, your project is automatically packaged into a Bento, the standard distribution format for BentoML Services, uploaded and deployed on BentoCloud. This serverless platform offers scalable and hardware-optimized solutions for running AI applications.

You can manually package your project into a Bento and containerize it as a Docker image. This Docker image can then be deployed to any Docker-compatible environment, such as Kubernetes. This method provides more flexibility in deployment and is suitable for integration into your existing container orchestration system.
