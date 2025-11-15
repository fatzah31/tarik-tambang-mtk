# Gunakan Python image
FROM python:3.10-slim

# Set dir kerja
WORKDIR /app

# Copy file aplikasi
COPY requirements.txt requirements.txt

# Install dependensi
RUN pip install --no-cache-dir -r requirements.txt

COPY. .
# Expose port Flask
EXPOSE 5000

# Jalankan Flask
CMD ["python", "app.py"]
