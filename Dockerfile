# step 1: Use a lightweight Python 3.12 image
FROM python:3.12-slim

# step 2: set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV HF_HOME="/app/model_cache"

# step 3: set work directory
WORKDIR /app

# step 4: install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# step 5: copy requirements file
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# step 6: copy project
COPY ./app ./app

# Step 7: Create the cache directory for the model
RUN mkdir -p /app/model_cache

# step 8: expose port
EXPOSE 8000


# step 9: run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]