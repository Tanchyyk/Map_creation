import folium
from distance_counting import find_the_closest_points
from distance_counting import find_the_furthermost_points


def put_points_on_map(lat: float, lon: float, year: int):
    map = folium.Map(tiles="Stamen Terrain", location=[lat, lon], zoom_start=6)
    map.add_child(folium.CircleMarker(location=[lat, lon],
                                      radius=10,
                                      popup='my current location',
                                      color='green',
                                      fill_opacity=0.5))

    for coordinates in find_the_closest_points(lat, lon, year):
        map.add_child(folium.Marker(location=[coordinates[0], coordinates[1]],
                                    popup="closest location",
                                    icon=folium.Icon()))

    for coordinates in find_the_furthermost_points(lat, lon, year):
        map.add_child(folium.CircleMarker(location=[coordinates[0], coordinates[1]],
                                          radius=10,
                                          popup='furthermost location',
                                          color='red',
                                          fill_opacity=0.5))

    map.save('My_Map.html')
    return "Check map!"
