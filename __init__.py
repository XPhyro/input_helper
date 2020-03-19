# Simple input helper for getting user input in built-in data types.


import re


def get_int_rng(msg="", end="\n> ", low=float("-inf"), high=float("inf"), is_low_inclusive=True, is_high_inclusive=True):
    if msg == "":
        msg = "Enter an integer in range " + ("[" if is_low_inclusive else "(") + f"{low}, {high}" + ("]" if is_high_inclusive else ")") + "."

    while True:
        s = input(msg + end)

        try:
            s = int(s)
        except:
            continue
        
        if is_low_inclusive:
            if is_high_inclusive:
                if not low <= s <= high:
                    continue
            else:
                if not low <= s < high:
                    continue
        else:
            if is_high_inclusive:
                if not low < s <= high:
                    continue
            else:
                if not low < s < high:
                    continue

        return s


def get_int(msg="Enter an integer.", end="\n> "):
    return get_int_rng(msg=msg, end=end)


def get_pint(msg="Enter a positive integer.", end="\n> "):
    return get_int_rng(msg=msg, end=end, low=0, is_low_inclusive=False)


def get_nonnint(msg="Enter a non-negative integer.", end="\n> "):
    return get_int_rng(msg=msg, end=end, low=0)


def get_nint(msg="Enter a negative integer.", end="\n> "):
    return get_int_rng(msg=msg, end=end, high=0, is_high_inclusive=False)


def get_nonpint(msg="Enter a non-positive integer.", end="\n> "):
    return get_int_rng(msg=msg, end=end, high=0)


def get_float_rng(msg="", end="\n> ", low=float("-inf"), high=float("inf"), is_low_inclusive=True, is_high_inclusive=True):
    if msg == "":
        msg = "Enter a real number in range " + ("[" if is_low_inclusive else "(") + f"{low}, {high}" + ("]" if is_high_inclusive else ")") + "."

    while True:
        s = input(msg + end)

        try:
            s = float(s)
        except:
            continue

        if is_low_inclusive:
            if is_high_inclusive:
                if not low <= s <= high:
                    continue
            else:
                if not low <= s < high:
                    continue
        else:
            if is_high_inclusive:
                if not low < s <= high:
                    continue
            else:
                if not low < s < high:
                    continue

        return s


def get_float(msg="Enter a real number.", end="\n> "):
    return get_float_rng(msg=msg, end=end)


def get_pfloat(msg="Enter a positive real number.", end="\n> "):
    return get_float_rng(msg=msg, end=end, low=0, is_low_inclusive=False)


def get_nonnfloat(msg="Enter a non-negative real number.", end="\n> "):
    return get_float_rng(msg=msg, end=end, low=0)


def get_nfloat(msg="Enter a negative real number.", end="\n> "):
    return get_float_rng(msg=msg, end=end, high=0, is_high_inclusive=False)


def get_nonpfloat(msg="Enter a non-positive real number.", end="\n> "):
    return get_float_rng(msg=msg, end=end, high=0)


def get_mat_str(size_x, size_y, msg="", prompt="> ", allowed_chars="", disallowed_chars="", allow_all_if_allowed_chars_empty=True):
    if size_x <= 0 or size_y <= 0:
        return []

    size = size_x * size_y
    s = ""

    print(msg)

    was_input_valid = True
    while len(s) != size:
        if not was_input_valid:
            # erase last line
            print("\x1b[1A\x1b[2K", end="")
            was_input_valid = True

        r = input(prompt)

        if not allow_all_if_allowed_chars_empty or allowed_chars != "":
            for i in r:
                if i not in allowed_chars:
                    was_input_valid = False
                    break

            if not was_input_valid:
                continue

        if i in r:
            if i in disallowed_chars:
                was_input_valid = False
                continue

        if len(r) == size_x or (len(r) == size and len(s) == 0):
            s += r
            was_input_valid = True

    return re.findall('.' * size_x, s)

