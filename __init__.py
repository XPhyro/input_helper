# Simple input helper for getting user input in built-in data types.


import math
import re


def inclusive_to_lambda(min_inclusive, max_inclusive):
    if min_inclusive:
        if max_inclusive:
            in_range = lambda i, rng_min, rng_max : rng_min <= i <= rng_max
        else:
            in_range = lambda i, rng_min, rng_max : rng_min <= i < rng_max
    else:
        if max_inclusive:
            in_range = lambda i, rng_min, rng_max : rng_min < i <= rng_max
        else:
            in_range = lambda i, rng_min, rng_max : rng_min < i < rng_max
    
    return in_range


def get_int_rng(msg="", end="\n> ", low=float("-inf"), high=float("inf"), is_low_inclusive=True, is_high_inclusive=True):
    if not isinstance(msg, str):
        raise TypeError("msg must be a str.")
    if not isinstance(end, str):
        raise TypeError("end must be a str.")
    if not isinstance(low, (int, float)):
        raise TypeError("low must be either an int or float.")
    if not isinstance(high, (int, float)):
        raise TypeError("high must be either an int or float.")
    if not isinstance(is_low_inclusive, bool):
        raise TypeError("is_low_inclusive must be a bool.")
    if not isinstance(is_high_inclusive, bool):
        raise TypeError("is_high_inclusive must be a bool.")

    if math.isclose(low, high):
        return low
    if low > high:
        raise ValueError("high must be greater than or equal to low.")

    if msg == "":
        msg = "Enter an integer in range " + ("[" if is_low_inclusive else "(") + f"{low}, {high}" + ("]" if is_high_inclusive else ")") + "."

    while True:
        s = input(msg + end)

        try:
            s = int(s)
        except ValueError:
            continue

        in_range = inclusive_to_lambda(is_low_inclusive, is_high_inclusive)
        if not in_range(s, low, high):
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
    if not isinstance(msg, str):
        raise TypeError("msg must be a str.")
    if not isinstance(end, str):
        raise TypeError("end must be a str.")
    if not isinstance(low, (int, float)):
        raise TypeError("low must be either an int or float.")
    if not isinstance(low, (int, float)):
        raise TypeError("high must be either an int or float.")
    if not isinstance(is_low_inclusive, bool):
        raise TypeError("is_low_inclusive must be a bool.")
    if not isinstance(is_high_inclusive, bool):
        raise TypeError("is_high_inclusive must be a bool.")

    if math.isclose(low, high):
        return low
    if low > high:
        raise ValueError("low cannot be greater than high.")

    if msg == "":
        msg = "Enter a real number in range " + ("[" if is_low_inclusive else "(") + f"{low}, {high}" + ("]" if is_high_inclusive else ")") + "."

    while True:
        s = input(msg + end)

        try:
            s = float(s)
        except ValueError:
            continue

        in_range = inclusive_to_lambda(is_low_inclusive, is_high_inclusive)
        if not in_range(s, low, high):
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
    if not isinstance(size_x, int):
        raise TypeError("size_x must be an int.")
    if not isinstance(size_y, int):
        raise TypeError("size_y must be an int.")
    if not isinstance(msg, str):
        raise TypeError("msg must be a str.")
    if not isinstance(prompt, str):
        raise TypeError("prompt must be a str.")
    if not isinstance(allowed_chars, (str, list)):
        raise TypeError("allowed_chars must be either a str or a list of char.")
    if not isinstance(allowed_chars, (str, list)):
        raise TypeError("disallowed_chars must be either a str or a list of char.")
    if not isinstance(allow_all_if_allowed_chars_empty, bool):
        raise TypeError("allow_all_if_allowed_chars_empty must be a bool.")
    if size_x < 0:
        raise ValueError("size_x must be greater than or equal to 0.")
    if size_y < 0:
        raise ValueError("size_y must be greater than or equal to 0.")
    for i in allowed_chars:
        if not isinstance(i, str):
            raise TypeError("Elements of allowed_chars must be a str,")
        if len(allowed_chars) > 0 and len(i) != 1:
            raise ValueError("Elements of allowed_chars must be of length 1.")
    for i in disallowed_chars:
        if not isinstance(i, str):
            raise TypeError("Elements of allowed_chars must be a str,")
        if len(disallowed_chars) > 0 and len(i) != 1:
            raise ValueError("Elements of allowed_chars must be of length 1.")
    if len(allowed_chars) == 0 and not allow_all_if_allowed_chars_empty:
        raise ValueError("allowed_chars cannot be empty if not allow_all_if_allowed_chars_empty.")

    if size_x == 0 or size_y == 0:
        return []

    size = size_x * size_y
    s = ""

    if msg == "":
        if len(allowed_chars) == 0:
            if len(disallowed_chars) == 0:
                msg = f"Enter a {size_x}x{size_y} matrix of strings."
            else:
                msg = f"Enter a {size_x}x{size_y} matrix of strings such that the strings will not contain the characters \"{disallowed_chars}\"."
        elif len(disallowed_chars) == 0:
            msg = f"Enter a {size_x}x{size_y} matrix of strings such that the strings will only contain the characters \"{allowed_chars}\"."
        else:
            msg = f"Enter a {size_x}x{size_y} matrix of strings such that the strings will only contain the characters \"{allowed_chars}\" and not contain \"{disallowed_chars}\"."

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

        for i in r:
            if i in disallowed_chars:
                was_input_valid = False
                break

        if not (len(r) == size_x or (len(r) == size and len(s) == 0)):
            was_input_valid = False

        if was_input_valid:
            s += r

    return re.findall('.' * size_x, s)


def get_mat_bool(size_x, size_y, msg="", prompt="> ", allowed_trues=["True", "true", "1"], allowed_falses=["False", "false", "0"]):
    if not isinstance(size_x, int):
        raise TypeError("size_x must be an int.")
    if not isinstance(size_y, int):
        raise TypeError("size_y must be an int.")
    if not isinstance(msg, str):
        raise TypeError("msg must be a str.")
    if not isinstance(prompt, str):
        raise TypeError("prompt must be a str.")
    if not isinstance(allowed_trues, list):
        raise TypeError("allowed_trues must be either a list of str.")
    if not isinstance(allowed_falses, list):
        raise TypeError("allowed_falses must be either a list of str.")
    if not isinstance(allow_all_if_allowed_chars_empty, bool):
        raise TypeError("allow_all_if_allowed_chars_empty must be a bool.")
    for i in allowed_trues:
        if not isinstance(i, str):
            raise TypeError("Elements of allowed_trues must be a str,")
    for i in allowed_falses:
        if not isinstance(i, str):
            raise TypeError("Elements of allowed_falses must be a str,")
    if size_x < 0:
        raise ValueError("size_x must be greater than or equal to 0.")
    if size_y < 0:
        raise ValueError("size_y must be greater than or equal to 0.")
    if len(allowed_trues) == 0:
        raise ValueError("allowed_trues must be of length 1 or greater.")
    if len(allowed_falses) == 0:
        raise ValueError("allowed_falses must be of length 1 or greater.")

    if size_x == 0 or size_y == 0:
        return []

    size = size_x * size_y
    m = []

    if msg == "":
        msg = f"Enter a {size_x}x{size_y} matrix of booleans."

    print(msg)

    was_input_valid = True
    while len(m) != size_y:
        if not was_input_valid:
            # erase last line
            print("\x1b[1A\x1b[2K", end="")
            was_input_valid = True

        r = input(prompt).split()

        for i in r:
            if i not in allowed_trues and i not in allowed_falses:
                was_input_valid = False
                break

        if not was_input_valid:
            continue

        for i, j  in enumerate(r):
            if j in allowed_trues:
                r[i] = True
            else:
                r[i] = False

        m.append(r)

    return m


def get_mat_int(size_x, size_y, msg="", prompt="> ", allowed_values=[], disallowed_values=[], allow_all_if_allowed_values_empty=True, allowed_range_min=float("-inf"), allowed_range_max=float("inf"), allowed_range_min_inclusive=True, allowed_range_max_inclusive=True):
    if not isinstance(size_x, int):
        raise TypeError("size_x must be an int.")
    if not isinstance(size_y, int):
        raise TypeError("size_y must be an int.")
    if not isinstance(msg, str):
        raise TypeError("msg must be a str.")
    if not isinstance(prompt, str):
        raise TypeError("prompt must be a str.")
    if not isinstance(allowed_values, list):
        raise TypeError("allowed_values must be a list.")
    if not isinstance(disallowed_values, list):
        raise TypeError("disallowed_values must be a list.")
    if not isinstance(allow_all_if_allowed_values_empty, bool):
        raise TypeError("allow_all_if_allowed_values_empty must be a bool.")
    if not isinstance(allowed_range_min, (int, float)):
        raise TypeError("allowed_range_min must be either an int or a float.")
    if not isinstance(allowed_range_max, (int, float)):
        raise TypeError("allowe_range_max must be either an int or a float.")
    if not isinstance(allowed_range_min_inclusive, bool):
        raise TypeError("allowed_range_min_inclusive must be a bool.")
    if not isinstance(allowed_range_max_inclusive, bool):
        raise TypeError("allowed_range_max_inclusive must be a bool.")
    if len(allowed_values) == 0 and not allow_all_if_allowed_values_empty:
        raise ValueError("allowed_values cannot be empty if not allow_all_if_allowed_values_empty.")
    for i in allowed_values:
        if not isinstance(i, int):
            raise ValueError("Elements of allowed_values must be an int.")
    for i in disallowed_values:
        if not isinstance(i, int):
            raise ValueError("Elements of disallowed_values must be an int.")
    if size_x <= 0 or size_y <= 0:
        return []
    if math.isclose(allowed_range_min, allowed_range_max):
        m = []
        v = []
        for i in range(size_x):
            v.append(allowed_range_min)
        for i in range(size_y):
            m.append(v)
        return m
    if allowed_range_min > allowed_range_max:
        raise ValueError("allowed_range_max_inclusive must be greater than or equal to allowed_range_min_inclusive.")

    size = size_x * size_y
    m = []

    if msg == "":
        if len(allowed_values) != 0: 
            if len(disallowed_values) != 0:
                msg = f"Enter a {size_x}x{size_y} matrix of integers such that the values will be in the set {allowed_values} and not be in the set {disallowed_values} and be in the range " + ("[" if allowed_range_min_inclusive else "(") + f"{allowed_range_min}, {allowed_range_max}" + ("]" if allowed_range_max_inclusive else ")") + "."
            else:
                msg = f"Enter a {size_x}x{size_y} matrix of integers such that the values will be in the set {allowed_values} and be in the range " + ("[" if allowed_range_min_inclusive else "(") + f"{allowed_range_min}, {allowed_range_max}" + ("]" if allowed_range_max_inclusive else ")") + "."
        elif len(disallowed_values) != 0:
            msg = f"Enter a {size_x}x{size_y} matrix of integers such that the values will not be in the set {disallowed_values} and be in the range " + ("[" if allowed_range_min_inclusive else "(") + f"{allowed_range_min}, {allowed_range_max}" + ("]" if allowed_range_max_inclusive else ")") + "."
        else:
            msg = f"Enter a {size_x}x{size_y} matrix of integers such that the values will be in the range " + ("[" if allowed_range_min_inclusive else "(") + f"{allowed_range_min}, {allowed_range_max}" + ("]" if allowed_range_max_inclusive else ")") + "."

    print(msg)

    was_input_valid = True
    while len(m) != size_y:
        if not was_input_valid:
            # erase last line
            print("\x1b[1A\x1b[2K", end="")
            was_input_valid = True

        r = input(prompt).split()

        if len(r) != size_x:
            was_input_valid = False
            continue

        for i, j in enumerate(r):
            try:
                s = int(float(j))
                r[i] = s
            except ValueError:
                was_input_valid = False
                break

        # if the validity of the input is not checked here, the program might crash as the rest assumes integers
        if not was_input_valid:
            continue

        in_range = inclusive_to_lambda(allowed_range_min_inclusive, allowed_range_max_inclusive)

        if not allow_all_if_allowed_values_empty or allowed_values != []:
            in_range_and_allowed = lambda i : in_range(i, allowed_range_min, allowed_range_max) and i in allowed_values
        else:
            in_range_and_allowed = in_range

        for i in r:
            if not in_range_and_allowed(i):
                was_input_valid = False
                break

        for i in disallowed_values:
            if i in r:
                was_input_valid = False
                break

        if not was_input_valid:
            continue

        m.append(r)

    return m


def get_mat_digit(size_x, size_y, msg="", prompt="> ", base=10):
    if not isinstance(size_x, int):
        raise TypeError("size_x must be an int.")
    if not isinstance(size_y, int):
        raise TypeError("size_y must be an int.")
    if not isinstance(msg, str):
        raise TypeError("msg must be a str.")
    if not isinstance(prompt, str):
        raise TypeError("prompt must be a str.")
    if not isinstance(base, int):
        raise TypeError("base must be an int.")
    if size_x < 0:
        raise ValueError("size_x must be greater than or equal to 0.")
    if size_y < 0:
        raise ValueError("size_y must be greater than or equal to 0.")
    if base <= 0:
        raise ValueError("base cannot be less than or equal to 0.")

    if size_x <= 0 or size_y <= 0:
        return []
    if base == 1:
        m = []
        v = []
        for i in range(size_x):
            v.append(0)
        for i in range(size_y):
            m.append(v)
        return m

    size = size_x * size_y
    m = []

    if msg == "":
        msg = f"Enter a {size_x}x{size_y} matrix of digits in base {base}."

    print(msg)

    was_input_valid = True
    while len(m) != size_y:
        if not was_input_valid:
            # erase last line
            print("\x1b[1A\x1b[2K", end="")
            was_input_valid = True

        r = input(prompt).split()

        if len(r) != size_x:
            was_input_valid = False
            continue

        for i, j in enumerate(r):
            try:
                s = int(j, base)

                if s < 0 or s >= base:
                    raise ValueError(f"Given input ({s}) is not a digit in the given base ({base}).")

                r[i] = s
            except ValueError:
                was_input_valid = False
                break

        if not was_input_valid:
            continue

        m.append(r)

    return m
