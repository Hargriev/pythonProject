from typing import Any


def filter_by_state(list_dicts: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция фильтрации словарей по значению ключа state"""
    filtered_list = []
    for key in list_dicts:
        if key.get("state") == state:
            filtered_list.append(key)
    return filtered_list


print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)


def sort_by_date(list_dicts: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Функция сортировки по убыванию даты"""
    sorted_date = sorted(list_dicts, key=lambda list_dicts: list_dicts["date"], reverse=reverse)
    return sorted_date


print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
