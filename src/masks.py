def get_mask_card_number(card_number: str) -> str:
    """Маскировка номера карты"""
    card_number_without_spaces = card_number.replace(" ", "")
    if len(card_number_without_spaces) != 16:
        return "Номер карты введен не корректно"
    else:
        card_number_mask = (
            f"{card_number_without_spaces[:4]} {card_number_without_spaces[4:6]}** "
            f"**** {card_number_without_spaces[-4:]}"
        )
        return card_number_mask


# print(get_mask_card_number('ffasfdasfasdvav'))
def get_mask_account(account_number: str) -> str:
    """Маскировка номера счета"""
    if len(account_number) != 20:
        return "Номер счета введен не корректно"
    else:
        mask_account_number = f"**{account_number[-4:]}"
        return mask_account_number


# print(get_mask_account('73654108430135874305'))
