####  ACCEPT STUDENT DETAILS 


name = input("Enter your Name ")

roll_no = int(input("Enter Your Roll No"))


## Accept Marks (6 subjects )
total = 0
for i in range(6):
    mark = float(input("Enter your marks"))
    total += mark

print(total)

### PERCENTAGE 

percentage = (total /600 ) * 100 


print(percentage)



#### Grade 
grade = ''
if percentage > 90 :
    grade = 'A+' 
    
elif percentage > 85 :
    grade = 'A'
    
elif percentage > 75 : 
    grade = 'B+'
    
elif percentage > 65 :
    grade = 'B'
    
elif percentage > 50 : 
    grade = 'C'

elif percentage > 40 :
    grade = 'D'
else :
    grade = 'F'

status = ""
if grade == "F" : 
    status = "Fail"
else : 
    status = "Pass"

print("###### STUDENT REPORT CARD ##########")

print("Name", name)
print("Roll No", roll_no)
print("Total", total)
print("Percentage",percentage)
print("Grade",grade)
print("Status",status)




    
