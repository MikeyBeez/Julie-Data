import datetime

# A class to return system info.
class SystemInfo:
    def __init__(self):
        pass

    @staticmethod
    def get_time():
        answer = 'The time is {} {}'.format(now.hour%12, now.minute)
        return answer



