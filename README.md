# Backend_PY_Django
  # To download Django
     python3 -m venv myenv
     source  env/bin/activate
     pip install django
     django-admin startproject myproject
     cd myproject
     python3 manage.py runserver


# to dockerize with postgres sql
  # dockerizing with postgres

    install docker 
    docker version
    docker pull postgres (in terminal)
    docker images
    docker run --name my-postgres -e POSTGRES_PASSWORD=mypassword -d postgres
    docker ps (To be able to see that the PostgreSQL container is actually running, type)
    docker stop my-postgres

    ALLOWED_HOSTS = [‘*’] (# For development purpose only myproject/settings.py in your editor:)


# Create a Dockerfile and copy the below settings
 # Use the official Python image from the DockerHub
    FROM python:3.10-slim

    # Set the working directory in docker
    WORKDIR /app

    # Copy the dependencies file to the working directory
    COPY requirements.txt .

    # Install any dependencies
    RUN pip install --no-cache-dir -r requirements.txt

    # Copy the content of the local src directory to the working directory
    COPY . .

    # Specify the command to run on container start
    CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# AFTER DOCKERFILE
    # pip freeze > requirements.txt
    # docker build -t mydjangoapp . --> (Build the Docker Image:)
    # Run the Django App in a Docker Container:
    --> docker run -d -p 8000:8000 mydjangoapp

    # psycopg2-binary>=2.9 -> In requirements.txt
    # pip install -r requirements.txt

# Approach 1: Docker Networking

    Step 1: Creating a Custom Docker Network
    First, let’s create a custom Docker network:

    1. docker network create mynetwork
    2. docker network ls


# Testing:
    To run your Django migrations manually, you need to run these commands:
    docker ps

    1. docker exec -it <container id> bash
    2. python manage.py makemigrations
    3. python manage.py migrate

    You can easily test if it’s working by creating a super user and navigating to the Django admin interface.

    Create a super user with this command in the bash shell in the /app directory inside the container:
    4. python manage.py createsuperuser

# admin run 
    admin->password->mypassword->sakshyam
    http://127.0.0.1:8000/admin 