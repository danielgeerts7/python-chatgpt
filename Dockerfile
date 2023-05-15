FROM python:3.9-slim

# setup app
WORKDIR /app

# Update to latest
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy files
COPY ./main.py /app
COPY ./env /app
COPY /src /app/src

# Run the application
CMD ["python3", "main.py"]