# Imagen oficial de MongoDB
FROM mongo:7.0

# Carpeta de trabajo
WORKDIR /data

# Copiamos el CSV
COPY ./data/* .

# Copiamos los scripts de inicialización
COPY ./init/* /docker-entrypoint-initdb.d/

# MongoDB arranca automáticamente al levantar el contenedor
