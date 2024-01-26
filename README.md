# Backend_PY_Django
# python3 -m venv myenv
# source  env/bin/activate
# pip install django
# django-admin startproject myproject
# cd myproject
# python3 manage.py runserver


# to dockerize with postgres sql
-- install docker 
-- docker version
-- docker pull postgres (in terminal)
-- docker images
-- docker run --name my-postgres -e POSTGRES_PASSWORD=mypassword -d postgres
-- docker ps (To be able to see that the PostgreSQL container is actually running, type)
-- docker stop my-postgres
-- ALLOWED_HOSTS = [‘*’] (# For development purpose only myproject/settings.py in your editor:)
--


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


# pip freeze > requirements.txt
# docker build -t mydjangoapp . --> (Build the Docker Image:)
# Run the Django App in a Docker Container:
 --> docker run -d -p 8000:8000 mydjangoapp