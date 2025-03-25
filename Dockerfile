# Utilisez une image de base avec Python et Spark
FROM openjdk:8-jdk-alpine

# Installer Python, pip et dépendances nécessaires
RUN apk add --no-cache python3 py3-pip

# Installer Spark et Hadoop (si nécessaire)
#RUN apk add --no-cache wget && \
#    wget -q https://archive.apache.org/dist/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz && \
#    tar -xzf spark-3.1.2-bin-hadoop3.2.tgz && \
#    mv spark-3.1.2-bin-hadoop3.2 /usr/local/spark

# Installer les bibliothèques Python nécessaires
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copier le code de l'application Databricks dans le conteneur
COPY . /app/

# Définir le répertoire de travail
WORKDIR /app

# Commande pour démarrer l'application
CMD ["python", "app.py"]
