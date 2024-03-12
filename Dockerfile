FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy and install the Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project code into the container
COPY . .

ENV GOOGLE_APPLICATION_CREDENTIALS="./application_default_credentials.json"

# Run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
