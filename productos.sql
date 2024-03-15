DROP TABLE IF EXISTS productos;

CREATE TABLE IF NOT EXISTS productos (
    id_productos INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(200) NOT NULL UNIQUE,
    descripcion TEXT NOT NULL,
    imagen BLOB NOT NULL,
    extension VARCHAR(10) NOT NULL,
    precio REAL NOT NULL,
    existencias INTEGER NOT NULL,
    hash TEXT NOT NULL
);
