
name = input("Enter student name: ")

n = int(input("Enter number of subjects (3-5): "))

total = 0

for i in range(1, n + 1):
    marks = float(input("Enter marks for subject " + str(i) + ": "))
    total = total + marks

average = total / n
percentage = (total / (n * 100)) * 100

print("\n----- Student Marks Report -----")
print("Student Name:", name)
print("Total Marks:", total, "/", n * 100)
print("Average Marks:", round(average, 2))
print("Percentage:", round(percentage, 2), "%")
