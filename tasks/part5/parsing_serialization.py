import json
from lxml import etree
from typing import List


def parse_json(json_path: str):
    with open(json_path, 'r') as file:
        data = json.load(file)
    return data

def calculate_city_summary(data: dict, city: str):
    city_summary: List = []
    mean_temp: float = round(sum([hour['temp'] for hour in data['hourly']]) / len(data['hourly']), 2)
    mean_wind_speed: float = round(sum([hour['wind_speed'] for hour in data['hourly']]) / len(data['hourly']), 2)
    min_temp: float = round(min(data['hourly'], key=lambda x: x['temp'])['temp'], 2)
    max_temp: float = round(max(data['hourly'], key=lambda x: x['temp'])['temp'], 2)
    max_wind_speed: float = round(max(data['hourly'], key=lambda x: x['wind_speed'])['wind_speed'], 2)
    
    city_summary.append({
        'city': city,
        'mean_temp': mean_temp,
        'mean_wind_speed': mean_wind_speed,
        'coldest_place': min_temp,
        'warmest_place': max_temp,
        'windiest_place': max_wind_speed
    })
    return city_summary

def serialize_to_xml(city_summary: List, total_summary: dict, output_path: str):
    root = etree.Element('weather')
    root.set('country', 'Spain')
    root.set('date', '2021-09-25')
    summary = etree.SubElement(root, 'summary')
    summary.set('mean_temp', str(total_summary['mean_temp']))
    summary.set('mean_wind_speed', str(total_summary['mean_wind_speed']))
    summary.set('coldest_place', str(total_summary['coldest_place']))
    summary.set('warmest_place', str(total_summary['warmest_place']))
    summary.set('windiest_place', str(total_summary['windiest_place']))
    cities = etree.SubElement(root, 'cities')
    for city_list in city_summary:
        city = city_list[0]
        city_element = etree.SubElement(cities, city['city'])
        city_element.set('mean_temp', str(city['mean_temp']))
        city_element.set('mean_wind_speed', str(city['mean_wind_speed']))
        city_element.set('coldest_place', str(city['coldest_place']))
        city_element.set('warmest_place', str(city['warmest_place']))
        city_element.set('windiest_place', str(city['windiest_place']))
    tree = etree.ElementTree(root)
    tree.write(output_path, pretty_print=True, xml_declaration=True, encoding='UTF-8')