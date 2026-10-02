# Portal Universitario CI/CD

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.3-black)
![Docker](https://img.shields.io/badge/Docker-ready-2496ED)

> **Una plataforma universitaria que se despliega en minutos, no en semanas.**

## Problema
Las instituciones educativas gestionan trabajos, proyectos y el estado de sus
sistemas mediante herramientas dispersas, difíciles de desplegar y de mantener.

## Solución
Portal Universitario CI/CD centraliza en una sola aplicación:

- **Monitoreo del estado del sistema** en tiempo real (`/api/status`)
- **Gestión de trabajos y proyectos** con listado y detalle (`/trabajos`)
- **Despliegue con un solo comando** mediante Docker, sin configuración manual

## Ventajas competitivas
- **Listo para producción:** contenerizado y reproducible en cualquier entorno.
- **Ligero y escalable:** construido sobre Flask, con facilidad para incorporar nuevos módulos.
- **Desarrollo profesional:** control de versiones, pull requests y prácticas CI/CD desde el inicio.

## Inicio rápido
```bash
git clone https://github.com/NatalIs20/ejercicio-ci-cd.git
cd ejercicio-ci-cd
docker build -t ejercicio-ci-cd .
docker run -d -p 5000:5000 --name portal ejercicio-ci-cd
```
La aplicación estará disponible en http://localhost:5000.

Instalación sin Docker: `pip install -r requirements.txt` y `python app.py`.

## Endpoints disponibles
| Ruta | Método | Descripción |
|------|--------|-------------|
| `/` | GET | Página principal de bienvenida |
| `/api/status` | GET | Estado del sistema |
| `/trabajos` | GET | Lista de trabajos registrados |
| `/trabajos/<id>` | GET | Detalle de un trabajo por ID |

## Hoja de ruta
- [ ] Autenticación de estudiantes y docentes
- [ ] Panel de administración
- [ ] Integración con base de datos
- [ ] Pipeline de despliegue automatizado (GitHub Actions)

## Tecnologías
Python 3.10 · Flask 3.0.3 · Docker · Git/GitHub

## Autora
Natali Isabel Chavez Alpizar — Ingeniería en Redes y Ciberseguridad, UTTT
