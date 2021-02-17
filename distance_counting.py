from geopy import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import math
from data_filter import make_film_lst


def get_coordinates(film_lst: list) -> list:
    result = []
    for film in film_lst:
        try:
            geolocator = Nominatim(user_agent="location_find")
            geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1, max_retries=1)
            location = geolocator.geocode(film[-1])
            film.append((location.latitude, location.longitude))
            result.append(film)
        except:
            continue

    return result


def count_distance(points1: tuple, points2: tuple) -> float:
    lat1 = points1[0]
    lat2 = points2[0]
    lon1 = points1[1]
    lon2 = points2[1]
    earth_radius = 6.371 * (10 ** 3)
    fi_1 = lat1 * math.pi / 180
    fi_2 = lat2 * math.pi / 180
    del_fi = (lat2 - lat1) * math.pi / 180
    del_alf = (lon2 - lon1) * math.pi / 180
    a = math.sin(del_fi / 2) * math.sin(del_fi / 2) \
        + math.cos(fi_1) * math.cos(fi_2) \
        * math.sin(del_alf / 2) * math.sin(del_alf / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return int(earth_radius * c)


def find_the_closest_points(lat: float, lon: float, year: int):

    dict_of_distances = dict()
    films = get_coordinates(make_film_lst("reduced_data.list"))
    points = []
    for film in films:
        if str(year)[:2] == str(film[1])[:2]:
            points.append(film[-1])
    for coordinates in points:
        dict_of_distances[count_distance((lat, lon), coordinates)] = coordinates

    distances = sorted(dict_of_distances.keys())[:5] if len(dict_of_distances.keys()) > 5 \
        else sorted(dict_of_distances.keys())
    result = []
    for key, value in dict_of_distances.items():
        if key in distances:
            result.append(value)

    return result
