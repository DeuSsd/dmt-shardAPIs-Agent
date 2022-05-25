# # The first instruction is what image we want to base our container on
# # We Use an official Python runtime as a parent image
# FROM python:3

# # The enviroment variable ensures that the python output is set straight
# # to the terminal with out buffering it first
# ENV PYTHONUNBUFFERED 1

# # create root directory for our project in the container
# RUN mkdir /src

# # Set the working directory to /music_service
# WORKDIR /src

# # Copy the current directory contents into the container at /music_service
# ADD . /src/

# # Install any needed packages specified in requirements.txt
# RUN pip install -r requirements.txt


# FROM python:3.8.3-slim
# COPY . /src
# WORKDIR /src
# # RUN python3 -m venv /opt/venv
# RUN pip install -r requirements.txt
# WORKDIR /app/src

FROM python:3.9

ENV PYTHONUNBUFFERED=1

WORKDIR /src

COPY ./requirements.txt .

RUN pip install -r ./requirements.txt

COPY ./src/agentAPI .

CMD [ "cd ./src/agentAPI" ]
# EXPOSE 8000

# ENTRYPOINT ["python", "manage.py", "runserver"]


#   command: bash -c "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"


