
# Use Python as the base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port 5001
EXPOSE 5001

# Start User Service
CMD ["python", "appu.py"]
