import folium
from distance_counting import find_the_closest_points


def put_closest_points_on_map(lat: float, lon: float, year: int):
    map = folium.Map(tiles="Stamen Terrain", location=[49.842957, 24.031111], zoom_start=6)
    map.add_child(folium.Marker(location=[lat, lon],
                                popup="my location",
                                icon=folium.Icon()))

    for coordinates in find_the_closest_points(lat, lon, year):
        map.add_child(folium.Marker(location=[coordinates[0], coordinates[1]],
                                    popup="film location",
                                    icon=folium.Icon()))
    map.save('My_Map.html')
    return "Check map!"
