import csv
# Bring CSV library into this program.


with open(
    "Attendance/attendance.csv",
    "a",
    newline=""
) as file:
    # Open file in append mode.

    writer = csv.writer(file)
    # Create CSV writer object.

    writer.writerow(
        [
            "Jegathayini",
            "2026-09-14",
            "09:30:15"
        ]
    )
    # Add one attendance record.


print(
    "Attendance recorded successfully."
)