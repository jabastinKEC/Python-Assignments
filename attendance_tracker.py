def get_attendance_status(total_classes, attended_classes):
    if total_classes <= 0:
        return "Invalid input: Total classes must be greater than 0."
    
    attendance_percentage = (attended_classes / total_classes) * 100
    print("Your attendance percentage: ",attendance_percentage)
    if attendance_percentage >= 75:
        return "Present"
    else:
        return "Absent"


total_classes = int(input("Enter the total number of classes: "))
attended_classes = int(input("Enter the number of classes attended: "))

status = get_attendance_status(total_classes, attended_classes)
print(f"Attendance Status: {status}")