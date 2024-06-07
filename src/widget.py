def mask_account_card(number: str) -> str | None:
    """Функция, возвращающая маску карты"""
    if number.isdigit() and len(number) == 16:
        return f"{number[:4]} {number[5:7]}{"*" * 2} {"*" * 4} {number[12:]}"
    elif number.isdigit() and len(number) == 20:
        return f"{'*' * 2}{number[-4::]}"
    else:
        return None


print(mask_account_card('Maestro 1596837868705199'))