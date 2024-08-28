FROM python:3.9-slim

WORKDIR /app

# Créer et activer un environnement virtuel
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Installer debugpy pour le débogage distant
RUN pip install debugpy

COPY . .

# Exposer le port pour Django et le port pour le débogage
EXPOSE 8000
EXPOSE 9229

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
