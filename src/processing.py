from typing import Dict, List


def filter_by_state(list_of_dictionaries: [list], state: str = "EXECUTED") -> List[Dict]:
    """Функция сортировки по ключу state"""
    return [item for item in list_of_dictionaries if item.get("state") == state]


def sort_by_date(list_of_dictionaries: list) -> List[Dict]:
    """Функция сортировки даты"""
    return sorted(list_of_dictionaries, key=lambda item: item.get("state"), reverse=True)
