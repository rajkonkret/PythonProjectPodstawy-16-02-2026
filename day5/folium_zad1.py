import folium

coordinates = [
    (52.2297, 21.0122),
    (52.235, 21.045),
    (52.242, 21.073),
    (52.249, 21.105),
]
# tworzenie obiektu na mapie
mapa = folium.Map(location=[52.2297, 21.0122], zoom_start=13)

folium.Marker(location=[52.2297, 21.0122], popup="Warszawa").add_to(mapa)


folium.PolyLine(locations=coordinates, color='red').add_to(mapa)
mapa.save('mapa.html')
