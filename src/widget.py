from datetime import datetime

from masks import get_mask_account, get_mask_card_number


def mask_account_card(type_card_or_account: str) -> str:
    """ "Функция маскировки номера карты или банковского счета"""
    digit = ""
    letters = ""

    for symbols in type_card_or_account:
        if symbols.isdigit():
            digit += symbols
        else:
            letters += symbols
    if len(digit) != 16 and len(digit) != 20:
        return "Неверно заполнены данные"

    elif len(digit) == 16:
        mask_card = get_mask_card_number(digit)
        return f"{letters} {mask_card}"

    elif len(digit) == 20:
        mask_account = get_mask_account(digit)
        return f"{letters} {mask_account}"


def get_date(date_string: str) -> str:
    """Функция преобразования даты"""
    date_object = datetime.fromisoformat(date_string)
    formate_date = date_object.strftime("%d.%m.%Y")

    return formate_date


print(mask_account_card("Счет 646864736788947795"))
