## 🚀 AplicaciónAS

Esta es la aplicación del proyecto de Administración de Sistemas. Trata sobre los objetos del juego "The Binding of Isaac. A continuación encontrarás instrucciones para ponerla en marcha utilizando Docker y Docker Compose.

---

🔧 Requisitos

Antes de comenzar, asegúrate de tener instalado en tu sistema:

- Docker: https://www.docker.com/
- Docker Compose: https://docs.docker.com/compose/

---

📥 Clonar el repositorio

Descarga el repositorio y entra en el directorio del proyecto:
```bash
git clone https://github.com/GorkaRuiz9/AplicacionAS
cd AplicacionAS/
```
---

⚙ Configuración

La aplicación requiere un archivo .env para almacenar variables de configuración. Se proporciona un ejemplo que puedes copiar y editar:
```bash
cp .env.example .env
```
Luego, abre el archivo .env con tu editor favorito y rellena los siguientes campos:
```text
MONGO_INITDB_ROOT_PASSWORD=
RABBIT_USER=
RABBIT_PASS=
MONGO_URI=mongodb://admin:<TU-CONTRASEÑA>@mongo:27017/isaac_db?authSource=admin
```
(Da bastante igual lo que pongas, ya que la aplicación no está pensada para que se usen desde fuera. Eso si, la contraseña de mongo debe coincidir con la contraseña a poner en la variable MONGO_URI)

⚠️ Si no estás ejecutando la aplicación localmente, descomenta la línea correspondiente y agrega tu IP:
```text
#API_URL=http://<TU-IP>:8000
```
---

▶️ Ejecutar la aplicación

Para levantar la aplicación, ejecuta:
```bash
docker compose up
```
Si quieres que la aplicación corra en segundo plano, agrega la opción -d:
```bash
docker compose up -d
```
La aplicación estará disponible en:  

- http://localhost:3000 (si estás en local)
- http://<TU-IP>:3000 (si estás accediendo desde otra máquina)

Para cerrar la aplicación, haga Ctrl + C en la terminal si no se estaba ejecutando en segundo plano. Sino, ejecute lo siguiente:
```bash
docker compose down
```
