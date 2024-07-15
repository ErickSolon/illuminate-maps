import sys

from geopy.geocoders import Nominatim
from geopy.distance import geodesic

geolocator = Nominatim(user_agent="olho que tudo vê")
# exemplo: rua dos malucos 666, Fortaleza, Ceará, Brazil
de_onde = sys.argv[1]
# exemplo: mercado, Fortaleza, Ceará, Brazil
oq_procurar = sys.argv[2]
location_rua = geolocator.geocode(de_onde)
location_cem = geolocator.geocode(oq_procurar, exactly_one=False)

if location_cem:
    cem_list = []
    print("Resultados:\n\n")

    for cem in location_cem:
        proximos = geodesic((location_rua.latitude, location_rua.longitude),
                            (cem.latitude, cem.longitude)).km
        cem_list.append((proximos, cem))

    locais_ordenados = sorted(cem_list, key=lambda x: x[0])
    for contador, (prox, cem) in enumerate(locais_ordenados):
        print(
            f"{contador + 1}º: distância: {prox:.2f} km, coordenadas: {cem.latitude}, {cem.longitude}")
else:
    print("Nada Encontrado!")
