# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables for Python to run in unbuffered mode
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /code

# Copy the current directory contents into the container at /code
COPY . /code/

# Install dependencies in a virtual environment
RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install --no-cache-dir -r /code/requirements.txt

# Activate the virtual environment
ENV PATH="/venv/bin:$PATH"

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the command to start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]