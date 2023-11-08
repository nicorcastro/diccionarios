# Lista de estudiantes
estudiantes = [
    {
        'nombre': 'Alejandro',
        'apellido': 'Garcia',
        'promedio': 3.78,
        'nivelProg': 2,
        'edad': 21,
        'estadoCivil': 'soltero'
    }
    ,
    {
        'nombre': 'Sandra',
        'apellido': 'Junco',
        'promedio': 4.39,
        'nivelProg': 2,
        'edad': 23,
        'estadoCivil': 'soltero'
    }
    ,
    {
        'nombre': 'Brayan',
        'apellido': 'Ortiz',
        'promedio': 3.09,
        'nivelProg': 2,
        'edad': 20,
        'estadoCivil': 'soltero'
    }
    ,
    {
        'nombre': 'Jhon',
        'apellido': 'Neva',
        'promedio': 3.5,
        'nivelProg': 2,
        'edad': 20,
        'estadoCivil': 'soltero'
    }    
    ,
    {
        'nombre': 'Nicolas',
        'apellido': 'Rojas',
        'promedio': 4.2,
        'nivelProg': 2,
        'edad': 26,
        'estadoCivil': 'soltero'
    }
    ,
    {
        'nombre': 'Luisa',
        'apellido': 'Betancourt',
        'promedio': 3.5,
        'nivelProg': 3,
        'edad': 19,
        'estadoCivil': 'soltero'
    }
    ,
    {
        'nombre': 'Linda',
        'apellido': 'Ramos',
        'promedio': 3.61,
        'nivelProg': 2,
        'edad': 25,
        'estadoCivil': 'union'
    }
    ,
    {
        'nombre': 'Maria',
        'apellido': 'Pardo',
        'promedio': 3.8,
        'nivelProg': 2,
        'edad': 23,
        'estadoCivil': 'union'
    }
    ,
    {
        'nombre': 'Diana',
        'apellido': 'Soto',
        'promedio': 3.6,
        'nivelProg': 2,
        'edad': 20,
        'estadoCivil': 'union'
    }
    ,
    {
        'nombre': 'Johan',
        'apellido': 'Galindo',
        'promedio': 3.38,
        'nivelProg': 2,
        'edad': 22,
        'estadoCivil': 'soltero'
    }
    ,
    {
        'nombre': 'Angel',
        'apellido': 'Molano',
        'promedio': 3.6,
        'nivelProg': 3,
        'edad': 21,
        'estadoCivil': 'soltero'
    }
    ,
    {
        'nombre': 'Andres',
        'apellido': 'Segura',
        'promedio': 4.1,
        'nivelProg': 3,
        'edad': 24,
        'estadoCivil': 'comprometido'
    }
    ,
    {
        'nombre': 'Nikole',
        'apellido': 'Florez',
        'promedio': 4.19,
        'nivelProg': 3,
        'edad': 21,
        'estadoCivil': 'soltero'
    }
    ,
    {
        'nombre': 'Ruth',
        'apellido': 'Duran',
        'promedio': 4.0,
        'nivelProg': 3,
        'edad': 22,
        'estadoCivil': 'union'
    }
]

# Inicializamos algunas variables para los cálculos
promedioEdad = 0
numSolteros = 0
mayorPromedio = None
menorNivelProg = float('inf')
numApellidoC = 0

# Recorremos la lista de estudiantes
for estudiante in estudiantes:
    promedioEdad += estudiante['edad']
    if estudiante['estadoCivil'] == 'soltero':
        numSolteros += 1
    if mayorPromedio is None or estudiante['promedio'] > mayorPromedio['promedio']:
        mayorPromedio = estudiante
    if estudiante['nivelProg'] < menorNivelProg:
        menorNivelProg = estudiante['nivelProg']
    if estudiante['apellido'][0].upper() == 'C':
        numApellidoC += 1

# Calculamos el promedio de edad
promedioEdad /= len(estudiantes)

# Imprimimos los resultados
print(f"Promedio de edad de los estudiantes: {promedioEdad:.2f} años")
print(f"Número de estudiantes solteros: {numSolteros}")
print(f"Estudiante con el mayor promedio: {mayorPromedio['nombre']} {mayorPromedio['apellido']} (Promedio: {mayorPromedio['promedio']})")
print(f"Estudiante con el menor nivel de programación: {menorNivelProg}")
print(f"Número de estudiantes cuyo apellido inicia con 'C': {numApellidoC}")
