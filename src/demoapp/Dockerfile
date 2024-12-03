# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Copy all necessary CSV files into the container
COPY *.csv /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for Streamlit
EXPOSE 5000

# Run Streamlit when the container launches
CMD ["streamlit", "run", "main.py"]