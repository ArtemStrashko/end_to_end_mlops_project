# Use an official Python runtime as a base image
FROM python:3.11-slim-buster

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.5.1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

# Install Poetry and other dependencies
RUN apt-get update && apt-get install -y curl git && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Set the working directory in the container
WORKDIR /app

# Copy the project files (including pyproject.toml and poetry.lock)
COPY pyproject.toml poetry.lock ./

# Install dependencies via Poetry
RUN poetry install --no-root

# Copy the rest of the app's source code
COPY . .

# Expose the port the app will run on
EXPOSE 8080

# Run the Flask app
CMD ["python", "app.py"]
