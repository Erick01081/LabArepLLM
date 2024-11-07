# Servicio de Traducción con FastAPI

Un servicio de traducción simple construido con FastAPI y LangChain que utiliza los modelos de lenguaje de OpenAI para realizar traducciones de texto a varios idiomas.

## Descripción del Proyecto

Este servicio proporciona un endpoint REST API que puede traducir texto a diferentes idiomas utilizando los modelos de lenguaje de OpenAI. Utiliza FastAPI como framework web y LangChain para la gestión de prompts y cadenas de procesamiento.

## Arquitectura

El servicio sigue una arquitectura simple:
1. Un servidor FastAPI expone el endpoint de traducción
2. LangChain gestiona el flujo de trabajo de traducción
3. La API de OpenAI realiza la traducción real
4. Se puede acceder al servicio tanto a través de la API HTTP como mediante un cliente Python

## Primeros Pasos

### Requisitos Previos

- Python 3.8 o superior
- Clave API de OpenAI
- pip (gestor de paquetes de Python)

### Paquetes Necesarios

```bash
fastapi
langchain
langchain-openai
langserve
uvicorn
```

### Instalación

1. Clona el repositorio:
```bash
git clone <url-del-repositorio>
cd servicio-traduccion
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Configura tu clave API de OpenAI:
```bash
export OPENAI_API_KEY='tu-clave-api-aqui'
```

### Ejecutando el Servicio

1. Inicia el servidor FastAPI:
```bash
python main.py
```

El servidor se iniciará en `http://localhost:8000`

2. Usa el cliente:
```python
from langserve import RemoteRunnable
remote_chain = RemoteRunnable("http://localhost:8000/chain/")
response = remote_chain.invoke({"language": "italian", "text": "hola"})
print(response)
```

## Uso de la API

### Endpoint de Traducción

**Endpoint:** `/chain/`

**Método:** POST

**Cuerpo de la Petición:**
```json
{
    "language": "string",  // Idioma objetivo para la traducción
    "text": "string"      // Texto a traducir
}
```

**Ejemplo de Petición:**
```bash
curl -X POST "http://localhost:8000/chain/" \
     -H "Content-Type: application/json" \
     -d '{"language": "italian", "text": "hola"}'
```

## Desarrollo

### Estructura del Proyecto
```
.
├── main.py              # Aplicación FastAPI y definición de la cadena
├── requirements.txt     # Dependencias del proyecto
└── README.md           # Este archivo
```

### Agregando Nuevas Funcionalidades

Para extender el servicio de traducción, puedes:
1. Modificar la plantilla de prompt en `main.py`
2. Agregar nuevos endpoints en la aplicación FastAPI
3. Mejorar la cadena de LangChain con pasos adicionales

## Contribuir

1. Haz un fork del repositorio
2. Crea tu rama de función (`git checkout -b feature/nueva-funcion`)
3. Realiza tus cambios (`git commit -m 'Agregar nueva función'`)
4. Sube la rama (`git push origin feature/nueva-funcion`)
5. Abre un Pull Request

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.

## Agradecimientos

* FastAPI por el excelente framework web
* LangChain por las herramientas de gestión de cadenas
* OpenAI por la API del modelo de lenguaje
