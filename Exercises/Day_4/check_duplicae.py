import csv
# Bring CSV library into this program.


name_to_check = "Jegathayini"
# Person we are checking.


already_marked = False
# Assume attendance has not been marked.


with open(
    "Attendance/attendance.csv",
    "r"
) as file:
    # Open attendance file.

    reader = csv.reader(file)
    # Create CSV reader.

    next(reader)
    # Skip header row.

    for row in reader:
        # Check every attendance record.

        if row[0] == name_to_check:
            # Compare names.

            already_marked = True
            break
            # Stop checking once found.


if already_marked:

    print(
        "Attendance already marked."
    )

else:

    print(
        "Attendance not marked yet."
    )