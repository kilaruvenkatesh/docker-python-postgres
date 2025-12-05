# Docker Python + PostgreSQL Beginner Project

This project is a simple introduction to Docker. It shows how to run a Python application and a PostgreSQL database in separate containers and connect them through a custom Docker network.

The Python app connects to PostgreSQL, creates a table, inserts one row, and prints the data.

## 1. Requirements
- Docker Desktop
- Visual Studio Code
- Docker extension for VS Code

## 2. Python Application
The Python script connects to the database, creates a table, inserts one record, and prints all rows.

## 3. Dockerfile
A Dockerfile was created to build a Python image and install dependencies needed to connect to PostgreSQL.

## 4. Create Docker Network

docker network create mynetwork


<img width="777" height="117" alt="image" src="https://github.com/user-attachments/assets/00cfe1a5-d55e-49fa-bad9-814d30e39851" />


## 5. Run PostgreSQL Container

docker run -d
--name my-postgres
--network mynetwork
-e POSTGRES_USER=user
-e POSTGRES_PASSWORD=pass
-e POSTGRES_DB=mydb
postgres

<img width="1212" height="677" alt="image" src="https://github.com/user-attachments/assets/795fd4a4-c030-4e7e-b923-98e2a1837773" />


## 6. Build and Run the Python App

docker build -t my-python-app .

docker run --rm --network mynetwork my-python-app


## 7. Expected Output
Inserted Row ID: 1  
Rows: [(1, 'Hello this venkatesh from PostgreSQL!')]

<img width="628" height="139" alt="image" src="https://github.com/user-attachments/assets/91b4b91f-ae1b-45eb-9793-3e7e8ac58908" />

## my docker hub link 
https://hub.docker.com/repository/docker/kilaruvenkatesh/my-python-app/general

## 8. Summary
This project demonstrates basic containerization and database connectivity using Docker.




