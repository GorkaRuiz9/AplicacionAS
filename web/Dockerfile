# Imagen base
FROM node:20-alpine

# Carpeta de trabajo dentro del contenedor
WORKDIR /web

# Copiar solo package.json y package-lock.json primero (para cache de npm install)
COPY package*.json .

# Instalar dependencias desde el package.json??? CONFIRMAR
RUN npm install

# Copiar todo el código de la app
COPY . .

# Puerto donde corre la app
EXPOSE 3000

# Comando para iniciar la app
CMD ["node", "index.js"]
