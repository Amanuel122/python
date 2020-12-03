while True:
    try:
         no_of_students_in_the_class = int(input(" enter the number of students in the class: "))
         if no_of_students_in_the_class > 0 :
             break
         print (" enter a number above 0 please.")
    except Exception as error:
        print(error)
while True :
    try:
         no_of_pcs_in_the_lab = int(input ( " enter the number of PCs in the lab :"))
         if no_of_pcs_in_the_lab > 0:
          break
         print(" enter a number above 0 please")
    except Exception as error2:
     print (error2)
if no_of_pcs_in_the_lab >=no_of_students_in_the_class:
    print( " you need 1 lab for all the students")
else:
    print(" you need 2 labs for all the students")
