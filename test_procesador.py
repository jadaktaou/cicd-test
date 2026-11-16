from procesador import limpiar_datos_clinicos
import sys

# 1. Datos de entrada (Simulamos 3 pacientes reales de un hospital)
datos_entrada = ["Paciente A", "Paciente B", "Paciente C"]

# 2. Pasamos los datos por nuestro código
resultado = limpiar_datos_clinicos(datos_entrada)

# 3. EL TEST GxP: Verificamos que no se ha perdido nadie
try:
    assert len(resultado) == 3
    print("✅ TEST SUPERADO: Los 3 pacientes han sido procesados sin pérdida de datos.")
except AssertionError:
    print("❌ ERROR CRÍTICO: Pérdida de datos detectada. Abortando...")
    sys.exit(1) # Esto le dice a GitHub Actions que el pipeline debe explotar
