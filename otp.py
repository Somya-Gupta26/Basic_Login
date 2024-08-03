def log():
  un1="somya"
  pd1=123
  un2=str(input("Enter username:"))
  pd2=int(input("Enter password:"))
  if (un1==un2 and pd1==pd2):
   print("Login successful")
  else:
   print("Incorrect username or password")
   a=int(input("Press 1 for relogin or Press 2 for forget password:"))
   if (a==1):
    log()
   elif (a==2):
     def re():
        import random
        inc=random.randrange(1000,10000)
        print("OTP is:",inc)
        q=int(input("Enter OTP:"))
        if (inc==q):
         print("Your username is:",un1,"\nYour password is:",pd1)
         log()
        else:
          print("Incorrect OTP")
          re()
     re()
   else:
    print("Invalid number pressed. You can only press 1 or 2")
log()  