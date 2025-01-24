FROM python:3.12-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create recordings directory
RUN mkdir -p recordings

# Expose the port
EXPOSE 8000

# Command to run the application
CMD ["python", "-m", "main"]
