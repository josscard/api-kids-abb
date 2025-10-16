# api_kids_abb

Proyecto base con FastAPI + Pydantic para gestionar niños en un Árbol Binario de Búsqueda.

## Características
- ✅ **Arquitectura MVC**: Modelo, Vista (API), Controlador
- ✅ **ABB (Árbol Binario de Búsqueda)**: Implementación completa para gestión de niños
- ✅ **Operaciones CRUD**: Crear, leer, actualizar, eliminar niños
- ✅ **Recorrido inorder**: Lista ordenada de niños
- ✅ **Estadísticas**: Información sobre el árbol

## Requisitos
- Python 3.12+

## Configuración rápida
```bash
python3 -m venv .venv
source .venv/bin/activate  # En Windows usar: .venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecución
```bash
python3 -m venv .venv
source .venv/bin/activate  # En Windows usar: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn api_kids_abb.main:app --reload --app-dir "src"
```

El servidor estará disponible en: http://localhost:8000

## Documentación API
Una vez ejecutándose, visita: http://localhost:8000/docs

## Endpoints

### Salud
- **GET** `/health` → Estado del servicio

### Gestión de Niños
- **POST** `/api/v1/kids/add` → Agregar un nuevo niño
- **GET** `/api/v1/kids/{kid_id}` → Obtener un niño por ID
- **GET** `/api/v1/kids/list` → Listar todos los niños (ordenados)
- **DELETE** `/api/v1/kids/{kid_id}` → Eliminar un niño
- **GET** `/api/v1/kids/stats` → Estadísticas del árbol

### Ejemplo de uso

#### Agregar un niño
```bash
curl -X POST "http://localhost:8000/api/v1/kids/add" \
  -H "Content-Type: application/json" \
  -d '{"name": "Ana", "age": 8}'
```

#### Listar niños
```bash
curl http://localhost:8000/api/v1/kids/list
```

## Estructura del Proyecto
```
api_kids_abb/
├── src/
│   └── api_kids_abb/
│       ├── controller/     # Lógica de control (API endpoints)
│       ├── model/         # Modelos de datos (Kid, BST)
│       ├── service/       # Lógica de negocio
│       ├── schemas/       # Esquemas Pydantic
│       └── main.py       # Aplicación FastAPI
├── tests/                # Tests
├── requirements.txt      # Dependencias
└── README.md            # Documentación
```

## Desarrollo
- **Código limpio**: Sigue convenciones de Python
- **OOP**: Uso moderado de herencia y encapsulación
- **Nivel intermedio**: Código comprensible para estudiantes de 4to semestre
