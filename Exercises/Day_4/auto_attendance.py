import csv
# Bring CSV library into this program.

from datetime import datetime
# Import datetime class.


current_datetime = datetime.now()
# Get current date and time.


current_date = current_datetime.strftime(
    "%Y-%m-%d"
)
# Format current date.


current_time = current_datetime.strftime(
    "%H:%M:%S"
)
# Format current time.


with open(
    "Attendance/attendance.csv",
    "a",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow(
        [
            "Jegathayini",
            current_date,
            current_time
        ]
    )
    # Save attendance record.


print(
    "Attendance recorded successfully."
)