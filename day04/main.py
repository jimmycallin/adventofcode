import re

required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def validate(current):
    print("Validating", current)
    validations = [all([field in current for field in required])]
    for key, value in current.items():
        valid = False
        if key == "byr":
            valid = 1920 <= int(value) <= 2002
        elif key == "iyr":
            valid = 2010 <= int(value) <= 2020
        elif key == "eyr":
            valid = 2020 <= int(value) <= 2030
        elif key == "hgt":
            if value.endswith("cm"):
                valid = 150 <= int(value[:-2]) <= 193
            elif value.endswith("in"):
                valid = 59 <= int(value[:-2]) <= 76
            else:
                valid = False
        elif key == "hcl":
            valid = bool(re.match(r"^#[0-9abcdef]{6}$", value.lower()))
        elif key == "ecl":
            valid = value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        elif key == "pid":
            valid = bool(re.match(r"^\d{9}$", value))
        elif key == "cid":
            valid = True
        print(f"key {key} value {value} valid {valid}")

        validations.append(valid)
    print("Validations", validations)
    return all(validations)


with open("input.txt") as f:
    valids = 0
    current = {}
    for line in f:
        if line == "\n":
            valids += validate(current)
            current = {}
            continue
        matches = re.findall(r"(\w+):([\w#]+)", line)
        fields = {match[0]: match[1] for match in matches}
        current.update(fields)
    valids += validate(current)

    print("{} valids".format(valids))