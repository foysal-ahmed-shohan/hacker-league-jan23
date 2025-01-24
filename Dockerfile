FROM python:3.10-slim

WORKDIR /app

# Install poetry
RUN pip install poetry

# Copy project files
COPY pyproject.toml poetry.lock* ./
COPY src ./src

# Configure poetry to not create virtual environment
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --only main

# Expose the port
EXPOSE 8000

# Run the application
CMD ["poetry", "run", "python", "-m", "src.sparc_demo.main"]
