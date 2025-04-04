from datetime import datetime


def mask_account_card(type_card_or_account: str) -> str:
    """"Функция маскировки номера карты или банковского счета"""
    digit_number = ''
    str_symbols = ''
    for symbols in type_card_or_account:
        if symbols.isdigit():
            digit_number += symbols
        else:
            str_symbols += symbols

    if len(digit_number) == 16:
        digit_number = (
            f"{str_symbols} {digit_number[:4]} {digit_number[4:6]}** "
            f"**** {digit_number[-4:]}"
        )
    elif 16 < len(digit_number) < 20 or len(digit_number) < 16:
        return 'Номер карты введен не корректно'

    elif len(digit_number) == 20:
        digit_number = f"{str_symbols} **{digit_number[-4:]}"

    else:
        return 'Номер счета введен не корректно'

    return digit_number


def get_date(date_string: str) -> str:
    """Функция преобразования даты"""
    date_object = datetime.fromisoformat(date_string)
    formate_date = date_object.strftime("%d.%m.%Y")

    return formate_date





