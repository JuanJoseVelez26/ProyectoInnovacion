import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

class Config:
    """Configuración principal del proyecto en Flask"""

    # Seguridad
    SECRET_KEY = os.getenv('SECRET_KEY', 'clave_por_defecto')

    # Debug
    DEBUG = os.getenv('DEBUG', 'True') == 'True'

    # Rutas base
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Base de datos (Usando SQLite por defecto, pero adaptable)
    DATABASE_ENGINE = os.getenv('DATABASE_ENGINE', 'sqlite')
    if DATABASE_ENGINE == 'sqlite':
        SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "db.sqlite3")}'
    elif DATABASE_ENGINE == 'postgresql':
        SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', '')
    else:
        raise ValueError("Base de datos no soportada")

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuración de Archivos Estáticos y Media
    STATIC_FOLDER = os.path.join(BASE_DIR, 'static')
    MEDIA_FOLDER = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'

    # Internacionalización
    LANGUAGE_CODE = 'es'
    TIME_ZONE = 'UTC'

    # URL de API externa
    API_URL = os.getenv('API_URL', "http://190.217.58.246:5186/api/SGV/procedures/execute")
    LOCAL = os.getenv('LOCAL_URL', "http://127.0.0.1:6186/proyectos/")

    # Flask-Login (manejo de sesiones)
    SESSION_TYPE = 'filesystem'
    SESSION_PERMANENT = False

    # Lista de hosts permitidos (Flask no tiene una configuración nativa como `ALLOWED_HOSTS` de Django)
    ALLOWED_HOSTS = ["*"]  # Flask no necesita esto a menos que uses ProxyFix

    # Autenticación (Flask usa Flask-Login en lugar de `AUTHENTICATION_BACKENDS`)
    AUTH_USER_MODEL = 'User'  # Este debe coincidir con el modelo que uses en Flask

    # Archivos estáticos
    STATIC_URL = 'static/'
    STATICFILES_DIRS = [STATIC_FOLDER]