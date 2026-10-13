def mobile_validator(value):
    value = value.strip()
    try:
        int(value)
    except Exception:
        raise ValueError("موبایل باید فقط عدد باشد")

    if len(value) != 11 or not value.startswith("09"):
        raise ValueError("موبایل باید ۱۱ رقم باشد و با 09 شروع شود")

    return value


def national_code_validator(value):
    value = value.strip()
    try:
        int(value)
    except Exception:
        raise ValueError("کد ملی باید فقط عدد باشد")

    if len(value) != 10:
        raise ValueError("کد ملی باید ۱۰ رقم باشد")

    return value


def card_number_validator(value):
    value = value.strip()
    try:
        int(value)
    except Exception:
        raise ValueError("شماره کارت باید فقط عدد باشد")

    if len(value) != 16:
        raise ValueError("شماره کارت باید ۱۶ رقم باشد")

    return value


def plate_validator(value):
    value = value.strip()
    if value == "" or len(value) < 7:
        raise ValueError("پلاک معتبر نیست")

    return value


def bill_id_validator(value):
    value = value.strip()
    try:
        int(value)
    except Exception:
        raise ValueError("شناسه قبض باید فقط عدد باشد")

    if not (8 <= len(value) <= 13):
        raise ValueError("طول شناسه قبض باید بین ۸ تا ۱۳ رقم باشد")

    return value