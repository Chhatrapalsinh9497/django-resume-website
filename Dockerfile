FROM python:3.7-alpine

# Set working directory
WORKDIR /app

# Copy the project files to the working directory
COPY . /app

# Install system dependencies
RUN apk update && \
    apk add --no-cache \
        zlib-dev \
        jpeg-dev \
        build-base \
        musl-dev \
        libffi-dev

# Install Python dependencies
RUN pip install -r requirements.txt

# Install requests module
RUN pip install requests

RUN pip install openai



# Expose port 8000
EXPOSE 8002

# Start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]
