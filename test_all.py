import decimal_time
from freezegun import freeze_time
from datetime import datetime

@freeze_time("00:00:00")
def test_time_calculation_midnight():
    hours, minutes, seconds, microseconds = decimal_time.decimal_now()
    assert hours == 0
    assert minutes == 0
    assert seconds == 0
    assert microseconds == 0


@freeze_time("12:00:00")
def test_time_calculation_noon():
    hours, minutes, seconds, microseconds = decimal_time.decimal_now()
    assert hours == 5
    assert minutes == 0
    assert seconds == 0
    assert microseconds == 0
