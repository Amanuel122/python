email='john@pop.ac.uk'
x = email.count('@')
email_spt = email.split('@')
domain='pop.ac.uk'


if not x == 1:
    print(str(email)+' '+'is not valid at'+' '+ str(domain ))

elif not len(email_spt[0])> 0:
    print(str(email)+' '+' is not valid at'+' '+ str(domain ))

elif not email_spt[-1] ==domain :
             print(str(email)+' '+' is not valid at '+' '+ str(domain))


else:
    print(str(email)+' '+'is valid at' +' '+ domain)