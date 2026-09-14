import csv
# Bring CSV library into this program.


with open(
    "Attendance/attendance.csv",
    "w",
    newline=""
) as file:
    # Create attendance file.

    writer = csv.writer(file)
    # Create CSV writer object.

    writer.writerow(
        ["Name", "Date", "Time"]
    )
    # Create column headings.


print(
    "attendance.csv created successfully."
)