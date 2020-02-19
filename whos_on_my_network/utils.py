import datetime


def get_utc_datetime():
    """ Get the current UTC time """
    return datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)


def to_utc_datetime(date: datetime.datetime):
    """ Sets a datetime's timezone to UTC """
    return date.replace(tzinfo=datetime.timezone.utc)


def remove_timezome(date: datetime.datetime) -> datetime.datetime:
    """ Remove timezone from a datetime """
    return date.replace(tzinfo=None)


def datetime_to_iso_string(date: datetime.datetime) -> str:
    """ Convert a datetime to an ISO 8601 string that is safe to pass to JavaScript """
    return date.isoformat()


def iso_string_to_datetime(string: str) -> datetime.datetime:
    """ Convert an ISO string (passed from a JavaScript client) to a datetime """
    return datetime.datetime.strptime(string, "%Y-%m-%dT%H:%M:%S.%f%z")


def __serialize_value(value):
    if type(value) == datetime.datetime:
        return datetime_to_iso_string(value)
    elif type(value) == list:
        return [__serialize_value(i) for i in value]
    else:
        return value


def serialize_dict(_dict: dict) -> dict:
    """ A function to support generic dict serialization for dynamic DTOs """
    for key in _dict:
        value = _dict[key]
        _dict[key] = __serialize_value(value)
    return _dict
