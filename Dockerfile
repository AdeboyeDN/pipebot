# Use a specific version of Python
FROM python:3.11.0-slim AS base

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Create a non-root user to run the application
RUN useradd --create-home appuser
USER appuser

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container and build it
COPY . .
RUN python setup.py build

# Use a smaller image for the final build stage
FROM python:3.11.0-slim AS final

# Create a non-root user to run the application
RUN useradd --create-home appuser
USER appuser

# Set the working directory to /app
WORKDIR /app

# Copy the built application code from the previous stage
COPY --from=base /app .

# Start the bot
CMD ["python", "bot.py"]
