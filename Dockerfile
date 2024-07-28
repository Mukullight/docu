# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /docs

# Copy the current directory contents into the container at /docs
COPY . /docs

# Copy the requirements.txt file into the container at /docs
COPY requirements.txt /docs/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the MkDocs server
EXPOSE 8000

# Run mkdocs serve when the container launches
CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8000"]
