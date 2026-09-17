# Distance between known face
# and webcam face.
distance = 0.42

# Recognition threshold.
threshold = 0.50

# Make recognition decision.
if distance < threshold:

    print(
        "Recognized Employee ✅"
    )

else:

    print(
        "Unknown Person ❌"
    )