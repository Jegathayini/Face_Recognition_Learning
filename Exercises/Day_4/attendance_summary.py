import csv
# Bring CSV library into this program.


attendance_count = 0
# Counter variable.


with open(
    "Attendance/attendance.csv",
    "r"
) as file:

    reader = csv.reader(file)

    next(reader)
    # Skip header row.

    for row in reader:

        attendance_count += 1
        # Count each attendance record.


print(
    "Total Attendance Records:",
    attendance_count
)