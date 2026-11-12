import math
import re

ISBN10_PATTERN = re.compile(r"[0-9]{9}[0-9Xx]")


def verify_isbn10_format(isbn_str):
    if not isinstance(isbn_str, str):
        return None
    cleaned = isbn_str.replace('-', '').strip()
    if not ISBN10_PATTERN.fullmatch(cleaned):
        return None
    first_digit = int(cleaned[0])
    group_code = cleaned[1:4]
    check_char = cleaned[9].upper()
    return f"Group {group_code}: Starts {first_digit}, Checksum {check_char}"


def calculate_depreciation_factor(book_age_str):
    if not isinstance(book_age_str, str):
        return None
    parts = book_age_str.split('/')
    if len(parts) != 2:
        return None
    try:
        age = float(parts[0])
        life = float(parts[1])
    except (ValueError, OverflowError):
        return None
    if not (math.isfinite(age) and math.isfinite(life)):
        return None
    if age < 0 or life <= 0:
        return None
    depreciation = 1.0 - (age / life)
    return round(max(0.1, depreciation), 2)


def lookup_condition_multiplier(condition_code):
    if not isinstance(condition_code, str):
        return None
    grade = condition_code.strip().upper()
    multipliers = {
        "MINT": 1.25,
        "LIKE_NEW": 1.00,
        "VERY_GOOD": 0.80,
        "GOOD": 0.60,
        "POOR": 0.30
    }
    return multipliers.get(grade)


def main():
    print("==== Running verify_isbn10_format ====")
    isbn_in = input("Enter ISBN-10 (e.g. 0-306-40615-2): ")
    result = verify_isbn10_format(isbn_in)
    print(result if result is not None else "Invalid ISBN-10 format")

    print("\n==== Running calculate_depreciation_factor ====")
    age_in = input("Enter age/lifespan in years (e.g. 3/10): ")
    result = calculate_depreciation_factor(age_in)
    print("Depreciation Factor:", result if result is not None else "Invalid input")

    print("\n==== Running lookup_condition_multiplier ====")
    cond_in = input("Enter condition (e.g. MINT, GOOD, POOR): ")
    result = lookup_condition_multiplier(cond_in)
    print("Multiplier:", result if result is not None else "Unknown condition")


if __name__ == "__main__":
    main()