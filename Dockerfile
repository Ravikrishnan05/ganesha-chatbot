# Dockerfile

# Stage 1: Use an official Python runtime as a parent image
FROM python:3.11-slim

# Stage 2: Install system dependencies, including build tools for C extensions
RUN apt-get update && apt-get install -y \
    ffmpeg \
    build-essential \
    portaudio19-dev \
    && rm -rf /var/lib/apt/lists/*

# Stage 3: Set the working directory
WORKDIR /app

# Stage 4: Copy requirements file
COPY requirements.txt .

# Stage 5: Install Python dependencies
# This step will now succeed because the required build tools are present.
RUN pip install --no-cache-dir -r requirements.txt

# Stage 6: Copy the rest of your application code
COPY . .

# Stage 7: Expose the Streamlit port
EXPOSE 8501

# Stage 8: The command to run your application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]