def limpiar_datos_clinicos(pacientes):
    # Simulamos que procesa los datos y devuelve la lista limpia
    pacientes_limpios = []
    for paciente in pacientes:
        if paciente != "":  # Filtramos espacios vacíos
            pacientes_limpios.append(paciente)
    return pacientes_limpios
