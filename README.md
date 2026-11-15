

# Building Microservices and a CI/CD Pipeline with AWS

## Project Description

This project demonstrates how to transform a monolithic

application into two independent microservices and deploy

them using AWS.

## Technologies Used

- Python

- Flask

- Docker

- Git

- GitHub

- Amazon ECR

- Amazon ECS

- AWS Fargate

- Application Load Balancer

- AWS CodeDeploy

- AWS CodePipeline

- AWS CodeBuild

## Microservices

### 1. User Service

Handles user-related information.

### 2. Product Service

Handles product-related information.

## Project Phases

1. Planning the design and estimating cost.

2. Analysing the monolithic application.

3. Creating the development environment and Git repository.

4. Converting the application into two microservices.

5. Creating ECR repositories and ECS infrastructure.

6. Creating target groups and an Application Load Balancer.

7. Creating two Amazon ECS services.

8. Configuring CodeDeploy and CodePipeline.

9. Modifying code to trigger the pipeline again.

## Deployment Architecture

GitHub -> CodePipeline -> CodeBuild -> ECR

-> ECS -> CodeDeploy

Users -> Application Load Balancer -> Microservices