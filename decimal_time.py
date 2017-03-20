from collections import namedtuple
from datetime import datetime


DecimalTimeDelta = namedtuple("DecimalTimeDelta", "hours minutes seconds microseconds")


def _dsecs_since_midnight(timestamp: datetime) -> float:
    midnight = timestamp.replace(hour=0, minute=0, second=0, microsecond=0)
    dt = timestamp - midnight
    return (dt.seconds + dt.microseconds/1e6) / 0.864  # decimal seconds
    

def decimal_now():
    dt = _dsecs_since_midnight(datetime.now())
    dt_str = f"{dt:012.6f}"
    hours = int(dt_str[0])
    minutes = int(dt_str[1:3])
    seconds = int(dt_str[3:5])
    microseconds = int(dt_str[-6:])
    return DecimalTimeDelta(hours, minutes, seconds, microseconds)


def update_ui_number(indicator):
    hours, minutes, seconds, microseconds = decimal_now()
    display_string = f"{hours}:{minutes}.{seconds}"
    indicator.set_label(display_string, "decimal time")
    return True
