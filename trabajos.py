TRABAJOS = [
    {"id": 1, "titulo": "Auditoria de Ciberseguridad", "estado": "en progreso", "responsable": "Natali"},
    {"id": 2, "titulo": "Plataforma HydroSafe", "estado": "completado", "responsable": "Equipo"},
    {"id": 3, "titulo": "Ejercicio CI/CD", "estado": "en revision", "responsable": "Natali"},
]

def obtener_trabajos():
    return TRABAJOS

def obtener_trabajo_por_id(trabajo_id):
    return next((t for t in TRABAJOS if t["id"] == trabajo_id), None)