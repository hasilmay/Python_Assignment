#Question 1
while True:
    try:
        age = int(input("Enter your age: "))
        print("Your age is", age)
        break

    except ValueError:
        print("Invalid age! Please enter a valid age.")

#Question 2
fruits = ["Apple", "Banana", "Strawberry", "Litchi", "Orange"]
with open("fruits.txt", "w") as file:
    for fruit in fruits:
        file.write(fruit + "\n")
with open("fruits.txt", "r") as file:
    for fruit in file:
        print(fruit.strip())

#Question 3(i)
students = {"Jeff": 74, "Samantha": 88, "Mike": 93, "Hannah": 80, "Frank": 97}
for name, mark in students.items():
    print(name, ":", mark)
highest_student = max(students,key=students.get)
print("\nStudent with the highest mark:")
print(highest_student, ":", students[highest_student])

#Question 3(ii)
class Book:
    def __init__(self, Title, Author, Price):
        self.title = Title
        self.author = Author
        self.price = Price

    def display_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price: $", self.price)

book1 = Book("How to train your dragon", "Jessica May", 25)
book2 = Book("Python programming", "James May", 30)

print("Book1 Details")
book1.display_details()
print ()
print("Book2 Details")
book2.display_details()

#Question 4

logs = ["2026-08-04T13:21:18", "2026-08-04T13:30:00", "2026-08-04T14:15:30", "2026-08-04T13:45:10", "2026-08-04T14:20:00", "2026-08-04T09:10:00"]

def find_peak_usage(logs):
    counts = [0] * 24

    for log in logs:
        hour = int(log[11:13])
        counts[hour] += 1

    peak_hour = 0
    for hour in range(1, 24):
        if counts[hour] > counts[peak_hour]:
            peak_hour = hour
    return peak_hour

result = find_peak_usage(logs)
print("\nPeak usage hour:", result)