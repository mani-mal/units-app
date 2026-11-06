"""Unit converter — standard-library only."""

CONVERSIONS = {
    ("celsius", "fahrenheit"): lambda v: v * 9 / 5 + 32,
    ("fahrenheit", "celsius"): lambda v: (v - 32) * 5 / 9,
    ("meters", "feet"): lambda v: v * 3.28084,
    ("feet", "meters"): lambda v: v / 3.28084,
    ("kilometers", "miles"): lambda v: v * 0.621371,
    ("miles", "kilometers"): lambda v: v / 0.621371,
    ("kilograms", "pounds"): lambda v: v * 2.20462,
    ("pounds", "kilograms"): lambda v: v / 2.20462,
}


def convert(value, from_unit, to_unit):
    key = (from_unit.lower(), to_unit.lower())
    if from_unit.lower() == to_unit.lower():
        return value
    fn = CONVERSIONS.get(key)
    if fn is None:
        raise ValueError(f"unsupported conversion: {from_unit} -> {to_unit}")
    return fn(value)


def supported():
    return sorted({f"{a} -> {b}" for a, b in CONVERSIONS})


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("usage: convert.py VALUE FROM TO", file=sys.stderr)
        print("supported:", ", ".join(supported()), file=sys.stderr)
        sys.exit(2)
    value = float(sys.argv[1])
    try:
        print(convert(value, sys.argv[2], sys.argv[3]))
    except ValueError as err:
        print(err, file=sys.stderr)
        sys.exit(1)
