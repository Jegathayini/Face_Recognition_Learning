# Day 4 - Attendance System Foundation

## Overview

Day 4 focused on building the foundation of an attendance system.

The goal was to understand how a face recognition system can be connected to an attendance recording system.

By the end of Day 4, the following workflow was understood:

```text
Face Recognition
↓
Get Employee Name
↓
Generate Date & Time
↓
Check Duplicate Attendance
↓
Save Attendance
↓
Generate Attendance Reports
```

---

# Module 1 - What Is An Attendance System?

An attendance system records the presence of individuals.

Information stored:

```text
Name

Date

Time
```

Example:

```text
Jegathayini
2026-09-14
09:15:22
```

---

## Attendance Workflow

```text
Person Arrives
↓
Face Detected
↓
Face Recognized
↓
Attendance Recorded
```

---

# Module 2 - Creating attendance.csv

A CSV file was used as the attendance database.

CSV means:

```text
Comma Separated Values
```

Example:

```csv
Name,Date,Time
```

---

## CSV Library

```python
import csv
```

Used for:

```text
Creating CSV files

Writing CSV files

Reading CSV files
```

---

# Module 3 - Writing Attendance Records

Attendance records were added using:

```python
csv.writer()
```

and

```python
writer.writerow()
```

Example:

```python
writer.writerow(
    [
        "Jegathayini",
        "2026-09-14",
        "09:30:15"
    ]
)
```

---

## Write Mode

```python
open(file, "w")
```

Purpose:

```text
Create a new file

Overwrite an existing file
```

---

# Module 4 - Automatic Date and Time

Instead of manually typing dates and times, the system generates them automatically.

---

## datetime.now()

```python
datetime.now()
```

Purpose:

```text
Get the current date and time from the system.
```

Example:

```text
2026-09-14 11:45:32.123456
```

---

## strftime()

```python
strftime()
```

Purpose:

```text
Convert raw date and time into a readable format.
```

Example:

```python
current_date = current_datetime.strftime(
    "%Y-%m-%d"
)
```

Output:

```text
2026-09-14
```

---

Example:

```python
current_time = current_datetime.strftime(
    "%H:%M:%S"
)
```

Output:

```text
11:45:32
```

---

## Difference Between datetime.now() and strftime()

### datetime.now()

```text
Returns the current date and time.
```

### strftime()

```text
Formats the date and time into a readable string.
```

---

# Module 5 - Automatic Attendance Entry

Attendance entries were generated automatically.

Example:

```python
writer.writerow(
    [
        "Jegathayini",
        current_date,
        current_time
    ]
)
```

---

## Attendance Example

```csv
Name,Date,Time

Jegathayini,2026-09-14,09:15:22
```

---

# Module 6 - Duplicate Attendance Protection

A person should only be marked once per day.

---

## Incorrect Logic

```text
Check Name Only
```

Problem:

```text
Attendance marked today
↓
Attendance blocked tomorrow
```

Incorrect.

---

## Correct Logic

Check:

```text
Name
+
Date
```

Example:

```text
Jegathayini + 2026-09-14
```

---

### Same Name + Same Date

```text
Duplicate Attendance
↓
Ignore
```

---

### Same Name + Different Date

```text
New Attendance
↓
Allow
```

---

# Module 7 - Reading Attendance Records

Attendance records were read using:

```python
csv.reader()
```

Purpose:

```text
Read data from attendance.csv
```

---

## Example

```python
for row in reader:

    print(row)
```

Output:

```text
['Jegathayini', '2026-09-14', '09:30:15']
```

---

## Column Access

Example:

```python
row[0]
```

Output:

```text
Name
```

---

Example:

```python
row[1]
```

Output:

```text
Date
```

---

Example:

```python
row[2]
```

Output:

```text
Time
```

---

# Module 8 - Attendance Summary

Attendance records were counted.

---

## Counter Variable

```python
attendance_count += 1
```

Meaning:

```python
attendance_count = attendance_count + 1
```

Example:

```text
0
↓
1
↓
2
↓
3
```

---

## Example Output

```text
Total Attendance Records: 3
```

---

# Module 9 - Attendance Reports

Attendance data was displayed in a more readable format.

Example:

```python
print(
    f"Name : {row[0]}"
)

print(
    f"Date : {row[1]}"
)

print(
    f"Time : {row[2]}"
)
```

---

## Example Output

```text
Name : Jegathayini

Date : 2026-09-14

Time : 09:30:15
```

---

# Attendance System Architecture

The complete attendance workflow learned during Day 4:

```text
Known Faces
↓
Face Recognition
↓
Get Employee Name
↓
Generate Date
↓
Generate Time
↓
Check Duplicate Attendance
↓
Save Attendance
↓
Update attendance.csv
↓
Generate Reports
```

---

# Future Attendance Workflow

The future face recognition attendance project will follow:

```text
Webcam
↓
Face Detection
↓
Face Recognition
↓
Get Employee Name
↓
Generate Date & Time