""" Useful utility functions """

# Python modules
import hashlib
import re
from datetime import datetime


def coerce_bool(value):
    """ Coerce boolean value """
    if value:
        if isinstance(value, bool):
            return value
        elif str(value).lower() == 'true' or str(value) == str(1):
            return True
    return False


def coerce_int(value):
    """ Coerce integer value """
    if value:
        if isinstance(value, int):
            return value
        else:
            try:
                value = int(value)
            except (TypeError, ValueError):
                return -1
    return False


def generate_date_hash():
    """
    Generate a hashed date of the current time
    """
    hasher = hashlib.sha256()
    hasher.update(str(datetime.now()))
    hashed_date = hasher.hexdigest()[0:30]

    return hashed_date


def strip_non_alphanumeric(string):
    """ Strip non alphanumeric characters """
    non_alpha_numeric = re.compile(r'[^0-9a-zA-Z]+')

    return non_alpha_numeric.sub('', string)


def standardize_phone_number(phone_number):
    new_phone_number = ""

    if phone_number:
        phone_number = strip_non_alphanumeric(phone_number)
        phone_number = re.compile(r'[^0-9]+').sub('x', phone_number)

        split_phone_extension = phone_number.split('x')

        phone_number = split_phone_extension[0]
        new_phone_number = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" % int(phone_number[:-1])) + phone_number[-1]

        if len(split_phone_extension) > 1:
            extension = split_phone_extension[1]
            new_phone_number = u"{0}x{1}".format(new_phone_number, extension)

    return new_phone_number
