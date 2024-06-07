def mask_account_card(numbers: str) -> str | None:
    """Функция, возвращающая маску карты"""
    name_var = ''
    numbers_var = ''
    for number in numbers:
        if number.isalpha():
            name_var += number
        if number.isdigit():
            numbers_var += number
    if numbers_var.isdigit() and len(numbers_var) == 16:
        return f"{name_var} {numbers_var[:4]} {numbers_var[5:7]}{"*" * 2} {"*" * 4} {numbers_var[12:]}"
    elif numbers_var.isdigit() and len(numbers_var) == 20:
        return f"{name_var} {'*' * 2}{numbers_var[-4::]}"
    else:
        return None


print(mask_account_card('Visa Platinum 7000 7922 8960 6361'))