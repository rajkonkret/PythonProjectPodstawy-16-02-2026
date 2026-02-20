import folium

# tworzenie obiektu na mapie
mapa = folium.Map(location=[52.2297, 21.0122], zoom_start=13)

folium.Marker(location=[52.2297, 21.0122], popup="Warszawa").add_to(mapa)

mapa.save('mapa.html')
