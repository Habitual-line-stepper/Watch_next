# Start from a base image with Python 3.9
FROM python:3.9-slim-buster

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install spacy && python -m spacy download en_core_web_md

# Copy the code into the container
WORKDIR /app
COPY watch_next.py .
COPY movies.txt .
COPY . .

# Run the code
CMD ["python", "watch_next.py"]
