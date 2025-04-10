from typing import Dict


def filter_by_state(list_of_dictionaries: [list], state: str = 'EXECUTED') -> list[Dict]:
    return [item for item in list_of_dictionaries if item.get('state') == state]


def sort_by_date(list_of_dictionaries: list) -> list:
    return sorted(list_of_dictionaries, key=lambda item: item['state'], reverse=True)
