FROM python:3.11-slim

# Set work directory inside the container
WORKDIR /app

# ⛔️ Clear any proxy environment variables
ENV http_proxy=""
ENV https_proxy=""
ENV proxies=""


# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Start Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
