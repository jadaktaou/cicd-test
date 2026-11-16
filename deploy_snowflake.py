import os
import snowflake.connector

# 1. El script recoge las llaves secretas que el Pipeline le va a inyectar
SF_ACCOUNT = os.getenv('SNOWFLAKE_ACCOUNT')
SF_USER = os.getenv('SNOWFLAKE_USER')
SF_PASSWORD = os.getenv('SNOWFLAKE_PASSWORD')

def conectar_y_desplegar():
    print("🔄 Conectando a Snowflake de forma segura...")
    
    try:
        # 2. Abrimos la conexión
        conn = snowflake.connector.connect(
            user=SF_USER,
            password=SF_PASSWORD,
            account=SF_ACCOUNT
        )
        cursor = conn.cursor()
        
        # 3. EL COMANDO ESTRELLA: Zero-Copy Cloning para entorno de QA
        # Clonamos la base de datos de manufactura en 1 segundo para hacer pruebas
        print("🧬 Ejecutando Zero-Copy Cloning para entorno de pruebas...")
        cursor.execute("CREATE DATABASE IF NOT EXISTS ROCHE_PT_QA CLONE ROCHE_PT_PROD;")
        
        print("✅ ¡Clonado exitoso! Entorno de QA listo para tests automáticos.")
        
    except Exception as e:
        print(f"❌ Error crítico de conexión o permisos: {e}")
        exit(1)
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    conectar_y_desplegar()
# Probando
