from datetime import datetime


def get_timestamp(self):
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))
