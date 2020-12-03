studentID= int(input("please enter studentID number: "))
username= input("please enter username: ")
password1= input("please enter password: ")
password2= input (" please re-enter password: ")
list_of_criteria = [ len(password1)>5,
          len(password1)<13,
          len(password2)>5,
          len(password2)<13,
          password1>=password2]
restrictions=['huddersfield',
              'password',
              'cheese',
              'programming']
not_allowed_words = [password1 == username,
                     password1 == str(studentID),
                     password1 == str(restrictions),]
if any(not_allowed_words):
    print("you cannot have that as your password try again")
else:
    if all(list_of_criteria):
        print("password changed sucessfully")
    else:
        print("password does not meet criteria")
