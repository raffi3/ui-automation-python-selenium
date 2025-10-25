import time


def get_timestamp_ms_in_past(go_past_in_seconds: int = 120):
    time_in_past_sec = time.time() - go_past_in_seconds
    return int(time_in_past_sec * 1000)
