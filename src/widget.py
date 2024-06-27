def mask_account_card(numbers: str) -> str | None:
    """Функция, возвращающая вариант наименования и маску номера"""
    name_var = ""
    numbers_var = ""
    for number in numbers:
        if number.isalpha() or number == " ":
            name_var += number
        if number.isdigit():
            numbers_var += number
    if numbers_var.isdigit() and len(numbers_var) == 16:
        return (
            f"{' '.join(name_var.split())} {numbers_var[:4]} {numbers_var[4:6]}{"*" * 2} {"*" * 4} {numbers_var[12:]}"
        )
    elif numbers_var.isdigit() and len(numbers_var) == 20:
        return f"{' '.join(name_var.split())} {'*' * 2}{numbers_var[-4::]}"
    else:
        return None


print(mask_account_card("Visa Classic 6831982476737658"))


def get_data(data: str) -> str | None:
    """Функция, возвращающая строку с датой в виде ДД.ММ.ГГГГ"""
    data_cut = ""
    for i in range(0, 10):
        data_cut += data[i]
    data_cut_split = data_cut.split("-")
    return f"{data_cut_split[2]}.{data_cut_split[1]}.{data_cut_split[0]}"


print(get_data("2018-07-11T02:26:18.671407"))