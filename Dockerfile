# Use the Python image
FROM python:3.8-alpine

# Install dependencies
RUN apk update && \
    apk add --no-cache build-base postgresql-dev libpq

# Set the working directory
WORKDIR /app

# Copy project files to the working directory
COPY requirements.txt /app/

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . /app

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Run the command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]