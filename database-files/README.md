# `database-files` Folder

How It Works

Project Structure: Briefly outline the key components of the application.

Backend: Responsible for handling business logic and API calls.

Frontend: User interface built using [Streamlit].

Database: Stores all project data using [MySQL].

Dependencies: Python, MySQL, Docker, Flask, Streamlit, Streamlit_Extras, Logging.

Starting the Containers:

Build the docker containers using [docker compose build].

Use [docker-compose up] to restart the application containers.

Open Datagrip for MySQL and run the SQL file on port [3200].

Workflow:
Describe the main flow of the application from user interaction to database operations.

Re-Bootstrap the Database: This involves resetting it to its initial state. Useful for testing major data and resolving majro data inconsistencies. This process will delete all existing data.

Steps:

Stop the Application and ensure it is not actively interacting with the database.

Use the docker-compose down to stop the application

Open Datagrip for MySQL and rerun the SQL file. 

- Use DROP DATABASE [NUconnect]; to drop the existing database. 

- Use CREATE DATABASE [NUconnect]; to recreate the Database

Use docker-compose up to restart the application

For troubleshooting, check the logs for the docker containers