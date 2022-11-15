import employees
import csv

ask = int(input("How many students do you want to create? "))

stu_list = []
f = open("students.txt", "a")

for employee in range(1, ask+1):
    
    print("\nEnter information for student",employee)
    
    firstName = input("Enter employee's first Name: ")
    lastName = input("Enter employee's last Name: ")
    job = input("Enter job: ")
    stu = employees.Employee(firstName,lastName, job)
    
    stu_list.append(stu)
 

with open ('employees.csv', 'w', newline=("")) as outFile:
  writer = csv.writer(outFile)
  writer.writerow(["First", "Last", "Job"])
  for item in stu_list:
    writer.writerow([item.get_fName(), item.get_lName(), item.get_job()])
