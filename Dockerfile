FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install required dependencies (Flask in this case)
RUN pip install --no-cache-dir -r requirements.txt

# Run the Python script
CMD ["python", "data.py"]
