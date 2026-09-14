import csv
# Bring CSV library into this program.


with open(
    "Attendance/attendance.csv",
    "r"
) as file:
    # Open attendance file.

    reader = csv.reader(file)
    # Create CSV reader.

    for row in reader:
        # Loop through each row.

        print("Name:",row[0])
        # Display row.