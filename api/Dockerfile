# Imagen base ligera con Python 3.11
FROM python:3.13.9-slim
# Evita crear archivos .pyc y usa stdout para logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Crea un usuario no root por seguridad
RUN useradd -m apiuser

# Crea el directorio de trabajo
WORKDIR /app

# Copia los requisitos e instálalos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . .

# Cambia al usuario no root
USER apiuser

# Expone el puerto
EXPOSE 8000

# Comando por defecto: lanzar FastAPI con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
