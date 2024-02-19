DROP TABLE IF EXISTS productos;

CREATE TABLE IF NOT EXISTS productos (
    id_productos INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(200) NOT NULL,
    descripcion TEXT NOT NULL,
    precio REAL NOT NULL,
    existencias INTEGER NOT NULL
);

INSERT INTO productos(nombre, descripcion, precio, existencias) VALUES ('Apuntador', 'Apuntador Laser', 100, 10);
INSERT INTO productos(nombre, descripcion, precio, existencias) VALUES ('Mouse', 'Mouse HP', 150, 5);
