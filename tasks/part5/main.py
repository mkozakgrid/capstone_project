import os
import parsing_serialization as ps
from typing import List

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def main():
    cities: List[str] = [
        'Barcelona', 'Logrono', 'Madrid', 'Merida', 'Murcia', 'Oviedo', 'Palma', 'Pamplona', 'santa_cruz_de_tenerife',
        'Santander', 'santiago_de_compostela', 'Seville', 'Toledo', 'Valencia', 'Valladolid', 'Vitoria-Gasteiz', 'Zaragoza'
    ]
    mean_temp: float = 0
    mean_wind_speed: float = 0
    coldest_temperature: float = 100000
    warmest_temperature: float = -1
    maximum_wind_speed: float = 0
    coldest_place: str = ''
    warmest_place: str = ''
    windiest_place: str = ''
    total_summary: dict = {}
    all_cities_summaries: List = []
    
    for city in cities:
        json_path = os.path.join(BASE_DIR, 'source_data', city, '2021_09_25.json')
        data = ps.parse_json(json_path)
        city_summary = ps.calculate_city_summary(data, city)
        all_cities_summaries.append(city_summary)

        mean_temp += city_summary[0]['mean_temp']
        mean_wind_speed += city_summary[0]['mean_wind_speed']

        if city_summary[0]['coldest_place'] < coldest_temperature:
            coldest_temperature = city_summary[0]['coldest_place']
            coldest_place = city_summary[0]['city']
        if city_summary[0]['warmest_place'] > warmest_temperature:
            warmest_temperature = city_summary[0]['warmest_place']
            warmest_place = city_summary[0]['city']
        if city_summary[0]['windiest_place'] > maximum_wind_speed:
            maximum_wind_speed = city_summary[0]['windiest_place']
            windiest_place = city_summary[0]['city']
        
    total_summary = {
        'mean_temp': round((mean_temp / 17), 2),
        'mean_wind_speed': round((mean_wind_speed / 17), 2),
        'coldest_place': coldest_place,
        'warmest_place': warmest_place,
        'windiest_place': windiest_place
    }

    output_path = os.path.join(BASE_DIR, 'result.xml')
    ps.serialize_to_xml(all_cities_summaries, total_summary, output_path)

if __name__ == "__main__":
    main()