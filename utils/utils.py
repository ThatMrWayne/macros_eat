from datetime import datetime, timezone


def convert_timestamp_to_utc_datetime(milli_timestamp):
    if isinstance(milli_timestamp, str):
        milli_timestamp = int(milli_timestamp)
    return datetime.fromtimestamp(milli_timestamp / 1000, tz=timezone.utc)
