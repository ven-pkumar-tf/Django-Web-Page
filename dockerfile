# Step 1: Use the official Python image as the base image
FROM python:3.9-slim

# Step 2: Set environment variables
# This prevents Python from writing .pyc files to disc
ENV PYTHONUNBUFFERED 1

# Step 3: Set the working directory inside the container
WORKDIR /app

# Step 4: Copy the requirements file into the container
COPY requirements.txt /app/

# Step 5: Install the required Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Copy the entire project into the container
COPY . /app/

# Step 7: Expose the port that Django will run on (default is 8000)
EXPOSE 8000

# Step 8: Command to run Django's development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
