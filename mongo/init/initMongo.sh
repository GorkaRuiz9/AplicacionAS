#!/bin/bash
set -e

echo "Importando CSV a MongoDB..."

# Variables
DB_NAME=${MONGO_INITDB_DATABASE:-mi_basedatos}
COLLECTION_NAME=mi_coleccion
DATA_DIR=/data
USER=${MONGO_INITDB_ROOT_USERNAME:-admin}
PASS=${MONGO_INITDB_ROOT_PASSWORD:-secret123}

# Recorrer todos los CSV del directorio
for CSV_FILE in "$DATA_DIR"/*.csv; do
  echo "Importando $CSV_FILE..."
  
  mongoimport --host localhost --port 27017 \
    --username "$USER" --password "$PASS" \
    --authenticationDatabase "admin" \
    --db "$DB_NAME" --collection "$COLLECTION_NAME" \
    --type csv --headerline --file "$CSV_FILE"
done

echo "Importación de todos los CSV completada."
