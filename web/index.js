// server.js
const express = require('express');
const path = require('path');
const { MongoClient } = require('mongodb');

const app = express();
const PORT = 3000;

// --- 🔧 Configuración MongoDB (hardcode temporal) ---
const MONGO_URI = "mongodb://admin:secret123@mongo:27017/mi_basedatos?authSource=admin"; //Mirar lo último q es
const DB_NAME = "mi_basedatos";
const COLLECTION_NAME = "mi_coleccion";

// --- 📦 Conexión a Mongo ---
let collection;
async function connectMongo() {
  try {
    const client = new MongoClient(MONGO_URI);
    await client.connect();
    console.log("✅ Conectado a MongoDB");
    const db = client.db(DB_NAME);
    collection = db.collection(COLLECTION_NAME);
  } catch (err) {
    console.error("❌ Error al conectar a MongoDB:", err);
  }
}
connectMongo();

// --- 🖼️ Servir archivos estáticos ---
app.use(express.static(path.join(__dirname, 'public')));

// --- 📄 Rutas HTML ---
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'views', 'index.html'));
});

app.get('/items', (req, res) => {
  res.sendFile(path.join(__dirname, 'views', 'items.html'));
});

// --- 🌐 API: devolver items desde MongoDB ---
app.get('/api/items', async (req, res) => {
  try {
    const items = await collection.find({}).toArray();
    res.json(items);
  } catch (err) {
    console.error("❌ Error al obtener items:", err);
    res.status(500).json({ error: "Error al obtener items" });
  }
});

// --- 🚀 Iniciar servidor ---
app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
