from datetime import datetime

current_datetime = datetime.now()

current_date = current_datetime.strftime(
    "%Y-%m-%d"
)

current_time = current_datetime.strftime(
    "%H:%M:%S"
)

print(current_date)

print(current_time)