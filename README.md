# Portal Universitario CI/CD

Aplicación web desarrollada con **Flask** que simula el portal universitario de la UTTT, incluyendo un módulo de estado del sistema y un módulo de gestión de trabajos/proyectos.

## Descripción

Este proyecto fue creado como práctica de **Integración y Despliegue Continuo (CI/CD)** utilizando Git, GitHub y Docker. Incluye:

- Página principal con mensaje de bienvenida
- Endpoint de estado del sistema (`/api/status`)
- Módulo de trabajos con listado y detalle (`/trabajos`)

## Instalación

Clona el repositorio:

```bash
git clone https://github.com/NatalIs20/ejercicio-ci-cd.git
cd ejercicio-ci-cd
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

Ejecuta la aplicación:

```bash
python app.py
```

## 🐳 Uso con Docker

```bash
docker build -t ejercicio-ci-cd .
docker run -d -p 5000:5000 --name portal ejercicio-ci-cd
```

La aplicación estará disponible en `http://localhost:5000`.

## Endpoints disponibles

| Ruta | Método | Descripción |
|------|--------|-------------|
| `/` | GET | Página principal de bienvenida |
| `/api/status` | GET | Estado del sistema |
| `/trabajos` | GET | Lista de trabajos registrados |
| `/trabajos/<id>` | GET | Detalle de un trabajo por ID |

## Tecnologías utilizadas

- Python 3.10
- Flask 3.0.3
- Docker

## Autora

Natali Isabel Chavez Alpizar — UTTT, Ingeniería en Redes y Ciberseguridad