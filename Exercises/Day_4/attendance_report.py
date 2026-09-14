import csv
# Bring CSV library into this program.


with open(
    "Attendance/attendance.csv",
    "r"
) as file:

    reader = csv.reader(file)

    next(reader)
    # Skip header row.

    for row in reader:

        print(
            f"Name : {row[0]}"
        )

        print(
            f"Date : {row[1]}"
        )

        print(
            f"Time : {row[2]}"
        )

        print(
            "-" * 30
        )
