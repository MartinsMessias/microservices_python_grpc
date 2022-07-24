Project to study microservices and gRPC

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=MartinsMessias_microservices_python_grpc&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=MartinsMessias_microservices_python_grpc)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=MartinsMessias_microservices_python_grpc&metric=bugs)](https://sonarcloud.io/summary/new_code?id=MartinsMessias_microservices_python_grpc)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=MartinsMessias_microservices_python_grpc&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=MartinsMessias_microservices_python_grpc)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=MartinsMessias_microservices_python_grpc&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=MartinsMessias_microservices_python_grpc)

## Getting started

Microservices are a way to organize complex software systems. Instead of putting all your code into one app, you break your app into microservices that are deployed independently and communicate with each other. 

- Catalog will be a very minimal web app that displays a list of movies to the user.
- Recommendations will be a microservice that provides a list of movies in which the user may be interested.

![image info](https://drive.google.com/uc?id=1I8Lr9rN-AAg4vFTcXP1sAbrt1WJkBMXA)


Start the services in the background:

    docker-compose up -d
    

Open Homepage at <http://localhost:5000>.


To stop the services in the background:

    docker-compose down
 
 #
