"""Тестовый файл"""

import pytest

from src.masks import get_mask_card_number
from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Счет 64886864736788947795", "Счет  **7795"),
        ("", "Неверно заполнены данные"),
        ("Visa Platinum 7000792289606361", "Visa Platinum  7000 79** **** 6361"),
        ("asdfasdfasfqwerqfasdva", "Неверно заполнены данные"),
    ],
)
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


@pytest.mark.parametrize(
    "value_date, expected_date",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("", "Данные введены не корректно"),
        ("24.04.2024", "Данные введены не корректно"),
    ],
)
def test_get_date(value_date, expected_date):
    assert get_date(value_date) == expected_date


@pytest.mark.parametrize(
    "value_card, expected_card",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("ffasfdasfasdvav", "Номер карты введен не корректно"),
        ("", "Номер карты введен не корректно"),
        ("70007922896061", "Номер карты введен не корректно"),
    ],
)
def test_mask_number_card(value_card, expected_card):
    assert get_mask_card_number(value_card) == expected_card
