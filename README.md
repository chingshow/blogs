# ReadItAgain

## Installation and Setup

### For Docker Deployment

1. **Building the Environment:**
   To set up your Docker environment, run the following command:

2. **Stopping and Removing Containers:**
To stop and remove the Docker containers, execute:

3. **Executing Commands in a Running Container:**
For example, to run SQL commands in the database:

*Note: Ensure that in `backend/app/config.py`, the line `os.environ['DATABASE_URL'] = ...` remains commented when deploying with Docker.*

### For Local Development

1. **Setting Up the Local Environment:**
To set up your project for local development, follow these steps:

- Ensure you have all the necessary local dependencies installed.
- Configure your local environment settings.

2. **Database Configuration:**
For local development, uncomment the following line in `backend/app/config.py`: 

This will configure the application to use your local database settings.

3. **Starting the Local Server:**
Navigate to the backend directory and start the local development server with the following command: 

If you need hot reloading, add `--reload` to the command:

*Note: Remember to revert the `os.environ['DATABASE_URL'] = ...` line back to its original commented state when switching back to Docker deployment.*
