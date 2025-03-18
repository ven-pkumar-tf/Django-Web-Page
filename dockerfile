# Step 1: Use the official Python image as the base image
FROM python:3.9-slim

# Step 2: Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Step 3: Set the working directory inside the container
WORKDIR /app

# Step 4: Copy the requirements file into the container
COPY requirements.txt .

# Step 5: Install the required Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Copy the entire project into the container
COPY . .

# Step 7: Collect static files (if using Django's static file management)
RUN python manage.py collectstatic --noinput

# Step 8: Expose the port that Django will run on
EXPOSE 8000

# Step 9: Command to run Django's development server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "tamil_class_web_page.wsgi:application"]
