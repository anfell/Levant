import random
identifiers = []
def generate_identifiers(num_entries):
    number_list = []
    _sum = 0
    out = ""
    for i in reversed(range(2, 11)):
        _j = random.randint(0, 9)
        number_list.append(str(_j))
        _sum += _j * i
    _m = _sum % 11
    if _m < 2:
        number_list.append(str(_m))
    elif _m >= 2:
        number_list.append(str(11 - _m))
    national_code = out.join(number_list)


    for _ in range(num_entries):
        while True:
            phone_number = "09" + ''.join(random.choice("0123456789") for _ in range(9))
            if len(phone_number) == 11:
                break

        phone_data = {
            "nationalCode": national_code,
            "phoneNumber": phone_number
        }
        identifiers.append(phone_data)

    return identifiers