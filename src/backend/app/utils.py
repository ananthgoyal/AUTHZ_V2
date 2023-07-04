import uuid
import datetime


def is_valid_uuid(value):
    try:
        uuid.UUID(str(value))

        return True
    except ValueError:
        return False
    
def is_valid_date_format(date):
    try:
        datetime.datetime.fromisoformat(date)
        return True
    except ValueError:
        #raise ValueError("Invalid Date")
        return False