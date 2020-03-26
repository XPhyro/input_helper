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
    if len(allowed_chars) == 0 and not allow_all_if_allowed_chars_empty:
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
    if size_x <= 0 or size_y <= 0:
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

        for i in range(len(r)):
            if r[i] in allowed_trues:
                r[i] = True
            else:
                r[i] = False

        m.append(r)

    return m

def get_mat_int(size_x, size_y, msg="", prompt="> ", allowed_values=[], disallowed_values=[], allow_all_if_allowed_values_empty=True, allowed_range_min=float("-inf"), allowed_range_max=float("inf"), allowed_range_min_inclusive=True, allowed_range_max_inclusive=True):
    if size_x <= 0 or size_y <= 0:
        return []
    if len(allowed_values) == 0 and not allow_all_if_allowed_values_empty:
        return []

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

        for i in range(len(r)):
            try:
                s = int(float(r[i]))
                r[i] = s
            except:
                was_input_valid = False
                break

        # if the validity of the input is not checked here, the program might crash as the rest assumes integers
        if not was_input_valid:
            continue

        if allowed_range_min_inclusive:
            if allowed_range_max_inclusive:
                in_range = lambda i : allowed_range_min <= i <= allowed_range_max
            else:
                in_range = lambda i : allowed_range_min <= i < allowed_range_max
        else:
            if allowed_range_max_inclusive:
                in_range = lambda i : allowed_range_min < i <= allowed_range_max
            else:
                in_range = lambda i : allowed_range_min < i < allowed_range_max

        if not allow_all_if_allowed_values_empty or allowed_values != []:
            in_range_and_allowed = lambda i : in_range(i) and i in allowed_values
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
    if type(base) is not int:
        raise TypeError("Base must be an integer.")
    if base <= 0:
        raise ValueError("Base cannot be less than or equal to 0.")

    if size_x <= 0 or size_y <= 0:
        return []

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

        for i in range(len(r)):
            try:
                s = int(r[i], base)

                if s < 0 or s >= base:
                    raise ValueError(f"Given input ({s}) is not a digit in the given base ({base}).")

                r[i] = s
            except:
                was_input_valid = False
                break

        if not was_input_valid:
            continue

        m.append(r)

    return m
