# FastAPI MongoDB

This is a RESTful API built using Python and FastAPI. The application leverages Docker for containerization, MongoDB as the database, pyenv, poetry for managing Python versions, and Swagger for API documentation and testing.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Steps](#steps)
    - [Database](#database)
    - [Docker](#docker)
    - [Swagger](#swagger)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Linting and Formatting](#linting-and-formatting)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This REST API serves as a robust backend solution using FastAPI and MongoDB. It facilitates key functionalities including CRUD operations, user authentication, data validation, and seamless interaction between the FastAPI framework and MongoDB database.

## Installation

### Prerequisites

- Python version 3.12.x (LTS)
- MongoDB
- [Poetry](https://python-poetry.org/)
- Docker
- Docker Compose
- [Pyenv](https://github.com/pyenv/pyenv) (optional, for managing Python versions)

### Steps

Follow these steps to set up and run the application:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/pashamakhilkumarreddy/fastapi-mongodb
   ```

2. **Change into the project directory:**

   ```bash
   cd fastapi-mongodb
   ```

3. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows, use `venv\Scripts\activate`
   ```

   or 

   ```bash
   pyenv local 3.12.4
   poetry shell
   ```

4. **Create a `.env` file in the project root directory and add the required environment variables (see `.env.example` as a reference):**

   ```bash
   cp .env.example .env
   ```

5. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```
   or

   ```bash
   poetry install
   ```

6. **Install pre-commit hooks:**

 - Install `pre-commit`: https://pre-commit.com/ (should be installed globally)

 - Install pre-commit hooks:

   `make install-git-hooks`

7. **Run the application:**

   ```bash
   uvicorn app.main:app --reload
   ```

8. For additional details, please refer to the [Makefile](Makefile) for this project. It includes various commands to manage the setup, running, and maintenance of the application.

#### Database

This application uses [MongoDB](https://www.mongodb.com/) as its database. Follow these steps to set up and configure the database for the FastAPI project:

- Ensure that you have MongoDB installed on your machine. You can download it from [MongoDB Downloads](https://www.mongodb.com/try/download/community).
- Start the MongoDB server by running the following command:

  ```bash
  mongod
  ```

- Connect to MongoDB and create a new database and user for the FastAPI project. You can run these commands in the MongoDB shell (`mongo`):

  ```bash
  # Connect to MongoDB shell
  mongo

  # Switch to the new database (it will be created if it doesn't exist)
  use fs-mongo;

  # Create a new user with roles
  db.createUser({
    user: "admin",
    pwd: "your_password",
    roles: [{ role: "readWrite", db: "fs-mongo" }]
  });

  # Exit the MongoDB shell
  exit;
  ```

This setup will create a MongoDB database named `fs-mongo` and a user named `admin` with read and write privileges on the `fs-mongo` database.

#### Docker

This project includes Docker Compose files for production and staging environments. Before using Docker, ensure you have the required environment variables set in the corresponding `.env` files (see `.env.example` as a reference).

To build and run Docker containers:

1. Ensure Docker is installed and running on your system.

2. **Build and run the MongoDB Docker image:**

   ```bash
   docker run -it -p 27017:27017 -d mongo
   ```

3. **Build and run the API using Docker Compose:**

   ```bash
   docker-compose up
   ```

4. **To stop and clean Docker containers, use the following command:**

   ```bash
   docker-compose down
   ```

#### Swagger

Access the Swagger UI at [Swagger API Docs](http://localhost:8000/api-docs).

## Project Structure

```bash
├── .github
├── nginx
├── app
│ ├── config
│ ├── helpers
│ ├── models
│ ├── routes
│ ├── schemas
│ ├── services
│ ├── main.py
├── .commitlintrc.json
├── .dockerignore
├── .editorconfig
├── .env
├── .env.example
├── .pre-commit-config.yaml
├── .secrets.baseline
├── CONTRIBUTING.md
├── docker-compose.yml
├── Dockerfile
├── LICENSE
├── Makefile
├── poetry.lock
├── pyproject.toml
├── README.md
├── requirements.txt
```

This repository follows a structured organization to facilitate clarity, maintainability, and scalability. Below is an overview of the key directories and files:

- `nginx`: Configuration files for NGINX, if applicable.
- `app`: The main source code directory containing the application's codebase.
  - `config`: Contains additional configuration files for the application.
  - `helpers`: Helper functions and utilities.
  - `models`: Database entities representing data models.
  - `routes`: FastAPI route definitions.
  - `schemas`: Pydantic schemas for data validation.
  - `services`: Service layer for business logic.
  - `main.py`: The entry point of the application.
- `static`: Static files such as images, if applicable.
- `tests`: Unit and integration tests for the application.
- `.commitlintrc.json`: Configuration file for Commitlint.
- `.dockerignore`: Files and directories to be ignored when building Docker images.
- `.editorconfig`: Configuration for maintaining consistent coding styles across different editors.
- `.env` and `.env.example`: Environment variables configuration.
- `.gitignore`: Files and directories to be ignored by Git.
- `.pre-commit-config.yaml`: Configuration for pre-commit hooks.
- `CONTRIBUTING.md`: Guidelines for contributing to the project.
- `docker-compose.yml`: Docker Compose files for production and development.
- `Dockerfile`: Dockerfile for building Docker images.
- `Makefile`: Contains various commands for setting up, building, and managing the project.
- `poetry.lock`: Poetry lock file that locks the dependencies to specific versions.
- `pyproject.toml`: Configuration file for Poetry, specifying project dependencies and metadata.
- `README.md`: This file contains information about the project and instructions on how to use it.
- `requirements.txt`: List of dependencies for the project, used by pip for installing the necessary packages.

## Testing

To run tests, use the following command:

```bash
poetry run pytest
```

## Linting and Formatting

To run ESLint, use the following command:

```bash
poetry run blue .
```

### Pre-commit Hook

Linting and formatting are enforced through the pre-commit hook using Husky and lint-staged. Make sure to address any issues reported by the hook. If you want to temporarily disable pre-commit hooks, you can use the `--no-verify` or `-n` option with your Git commit command. This option skips the pre-commit and commit-msg hooks for that specific commit.

```bash
git commit --no-verify -m "Your commit message"
```

## Contributing

We welcome contributions to enhance the functionality of this API. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Implement your changes.
4. Test your changes thoroughly.
5. Commit your changes (`git commit -am 'Add some feature'`).
6. Push to the branch (`git push origin feature/your-feature`).
7. Create a new Pull Request.

For additional contributing guidelines, see the [Contributing guide](./CONTRIBUTING.md).

## License

This project is licensed under the [License Name]. See the [LICENSE](LICENSE) file for details.
