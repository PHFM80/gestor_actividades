from geo.models import Localidad, Pais, Provincia


def seed_initial_data():
    paises = [
        {'nombre': 'Argentina', 'codigo': 'AR'},
    ]
    provincias = [
        {'nombre': 'Mendoza', 'pais': 'Argentina'},
    ]
    localidades = [
        {'nombre': 'Capital', 'provincia': 'Mendoza'},
        {'nombre': 'Godoy Cruz', 'provincia': 'Mendoza'},
        {'nombre': 'Guaymallén', 'provincia': 'Mendoza'},
        {'nombre': 'Maipú', 'provincia': 'Mendoza'},
        {'nombre': 'Luján de Cuyo', 'provincia': 'Mendoza'},
        {'nombre': 'Las Heras', 'provincia': 'Mendoza'},
        {'nombre': 'San Martín', 'provincia': 'Mendoza'},
        {'nombre': 'Rivadavia', 'provincia': 'Mendoza'},
        {'nombre': 'Junín', 'provincia': 'Mendoza'},
        {'nombre': 'Tunuyán', 'provincia': 'Mendoza'},
        {'nombre': 'Tupungato', 'provincia': 'Mendoza'},
        {'nombre': 'San Carlos', 'provincia': 'Mendoza'},
        {'nombre': 'San Rafael', 'provincia': 'Mendoza'},
        {'nombre': 'General Alvear', 'provincia': 'Mendoza'},
        {'nombre': 'Malargüe', 'provincia': 'Mendoza'},
    ]

    pais_map = {}
    for data in paises:
        pais, _ = Pais.objects.get_or_create(
            nombre=data['nombre'],
            defaults={'codigo': data.get('codigo')},
        )
        if data.get('codigo') and pais.codigo != data['codigo']:
            pais.codigo = data['codigo']
            pais.save(update_fields=['codigo'])
        pais_map[data['nombre']] = pais

    provincia_map = {}
    for data in provincias:
        pais = pais_map[data['pais']]
        provincia, _ = Provincia.objects.get_or_create(
            nombre=data['nombre'],
            pais=pais,
        )
        provincia_map[data['nombre']] = provincia

    for data in localidades:
        provincia = provincia_map[data['provincia']]
        Localidad.objects.get_or_create(
            nombre=data['nombre'],
            provincia=provincia,
        )
