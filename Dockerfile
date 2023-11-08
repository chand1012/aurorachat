# Use the official Python image as the base image
FROM python:3.11-slim-buster 

# Set the working directory in the container
WORKDIR /app

# Copy poetry.lock* and pyproject.toml
COPY poetry.lock* pyproject.toml ./

# Install poetry
RUN pip install poetry

# Install dependencies
RUN poetry install --no-root

# Copy the application code
COPY . .

# Run gunicorn
CMD ["python", "bot.py"]
