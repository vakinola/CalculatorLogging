# This is used to creating logging
from datetime import datetime


def print_logger(level, message, time):

    if level == 5:
        level_value = "CRITICAL"

    elif level == 4:
        level_value = "ERROR"

    elif level == 3:
        level_value = "WARNING"

    elif level == 2:
        level_value = "INFO"

    elif level == 1:
        level_value = "DEBUG"

    level_casting = str(level_value)
    message_casting = str(message)
    time_casting = str(time)

    msg = f"Message: {message_casting} | level: {level_casting} | {time_casting} \n "

    with open('logs', 'a') as opened_file:
        opened_file.write(msg)
