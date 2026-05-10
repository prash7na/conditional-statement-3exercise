### format method ###
#item = "moon"
#animal = "cow"
#print("The {} jumped over the {}".format(animal,item))
#positional argument
#print("The {0} jumprd over the {1}".format(animal,item))
#keyword argument
#print("The {animal} jumped over the {item}".format(animal="cow",item="moon"))
#text
#text = "The {} jumped over the {}."
#print (text.format(animal,item))
# for numbers 
#number = 3.1459
#print("The number pi is {}".format(number))
 

 #### f-string method ### 
      #How to use ??
#name = "Ram"
#print (f"Hello! \n My name is {name}")
#name = "Hari"
#age = 23
#print(f"Hello \n My name is {name} \n I am {age} years old.")
        #formatting codes 
#import datetime


#today = datetime.datetime.today()
#print(f"{today:%B %d,%Y}")

#name = "Ram"
#age = 24
#print(f"My name is {name} \n I am {age} years old.")

###   replace
#name = "ram"
#print (name.replace('r','R'))

#price= "$12.33"
#print(price.replace("$",""))

#slicing
#num = "+977+1111"
#print(num[0:4]+ num[5:])


#replacing multiple letters using replace method
#name = "pyhton"
#print(name.replace("p","P").replace("n","N"))


###maketrans only returns S/key value.so we have to use translate the value to get the result.
#print(name.maketrans("pn","PN"))
#print(name.translate)


###    centre method

#name = "Ram"
#print(name.center(9,"*"))

###   operators:opertors are used to perform various operations
#  1.arithematic operators
#  2.assignment  operators;used to assign values
#  3.comparison operators;to compare between variables
#  4.Logical operators;AND,OR and NOT
#  5.Identity operatos(is);compare the object, not if they are equal but if they are the same object with same memory location
#x = ["apple","banana"]
#y = ["apple","banana"]
#z = x
#print(x is z)#true
#print(x is y)#false
#print(x==y)#true
 
#6.membership operators;it tests if a sequence is present in an object.
#fruits = {"apple","banana","mango"}
#print("banana" in fruits)#true
#print("guava" not in fruits)#true

#bitwise operators;compare binary numbers
#print(2 & 3)
#num1 = 18
#num2 = 17
#print(num1&num2)
#print(num1^num2)
#print(num1|num2)

#number1 = 21
#number2 = 23
#print(number1&number2)
#print(number1^number2)
#print(number1|number2)
#a = -19
#b = 117
#print(~a)
#print(~b)
#only for positive value
#step1;convert in binary
#step1;apply XOR (changes the sign bit)
#step2;apply1 1"complement and then 2's complment(doesn"t changes the sign bit)
#for negative :B,1's com,2's compl,TT


###   split method
#timestamp = "2026,12,13"
#print(timestamp[0:5])
#print(timestamp.split(","))#will split in place of (,)


###    ljust;shifts apace in the right

#name = "Ram"
#rint(name.ljust)

###    cleaning;shifting spacaces from left to right
#name = "eam"
#print(name.lstrip())#to shift into left


### startswith ;checks the prefix ot the starting of the data
#gives boolean value ahd is used in decision making.
#name ="tommy" 
#print(name.startswith("ram"))  

#endswith:
#url = "employee_record.pdf"
#print(url.endswith("pdf"))

#how it is used
#url = "employee_record.pdf"
#if url.endswith('.xllx'):
#    print("file not supported")
#else:


### find,rfind,index,rindex
#find returns-1 for not found but index gives value error for not found
#find work only on string but index work on strings,lists and tuples
#find=left,used to find if the datatype is present or not fron left to right
#r=right to left

#dataset = "ram is a boy"
#print(dataset.find("r"))
#print(dataset.rfind("r"))
#print(dataset.index("r"))
#print(dataset.rindex("r"))#allgive positive 

#to get negative index number
#index_number=dataset.rfind('r'
#print(-lens(dataset))

###isdecimal,isalpha,isdigit,isalnum
#num= "123"
#print(num.isdecimal()) #decimal
#print(num.isalpha())    #alphabet
#print(num.isdigit()) #digit
#pprint(num.isalnum())  #alphabet and number
#print(num.isnumeric()) #num,fractions and roman
#print(num.isspace()) #complete space all should be space
#print(num.isprintable()) #escape characters=False 



#name = input("enter your name")
#name = "Laxman Devkota"
#print(f"Your user name is :{name} ")
#step1=name.replace("","_")
#print(step1)
#print("_".join(step1))

#first_name="ram"
#middle_name="bahadur"
#last_name="kc"
#print(first_name,middle_name,last_name,sep="_")
#print("_".join((first_name,middle_name,last_name)))

#to capitalize the all the first word.
#text = "see you soon!"
#print(text.title())

#to capitalize the the first letter of the sentences.
#text = "see you soon.how are you?"
#print()



#text = "python is good"
#print(text.upper())
#print(text.lower())
#print(text.title())
#print(text.swapcase())
#print(text.capitalize())
#print(text.casefold())
#print(text.center(40))
#print(text.count(""))
#print(text.encode())
#print(text.find("is"))
#print("_".join(text))

#print(2**2**3)
#print(10/2//3)

#### Input function
#asks user for thr information from the keyboard.
#converts the given info in string only
#typecasting;changing the datatype
#implicit conversion:doesn't need user involvement
#explicit conversion:needs users involvement to convert
#eval function is used to convert the datatype in all type
#sep parameter ;print(year,month,sep="")
#end perameter :print("Hello", end=" ")
#print("World")
# Output: Hello World (on a single line)

####conditional statement
#age =  18
#if age>= 18 :
#    print("You are an adult")

###else
#temperature = 35
#if temperature >30: 
#    print("It is hot outside.")
#    print("Too hot")
#else:
#    print("The weather is good.")


#elif
#score = 75
#if score >= 90:
#    grade = "A"
#elif score>= 80:
#    grade = "B"

#marks = 45
#if marks>=90:
#    print("Grade = A")
#elif marks>80:
#    print("Grade = B")
#elif marks>70:
#    print("Grade = C")
#else:
#    print("Failed")

#name = "Ram"
#age =14

#if age >=18:
#    print(f"{name} is regestered to vote.")
#else:
#    print(f"{name} is an invalid user.")
#    print("You must 18+.")


#1
#num = int(input("Enter a number"))
#if num<=100:
#   print("Valid")
#else:
#    print("invalid") 

#2)
#num = int(input("Enter a number."))
#if num %2 == 0:
#    print("Even")
#else:
#    print("odd") 


#3
#num = int(input("Enter number between 1-12"))
#if num==1:
#    print("January")
#elif num==2:
#     print("feb")
#elif num==3:
#     print("march")
#elif num==4:
#     print("april")
#elif num==5:
#print("may")
#elif num==6:
#     print("june")
#elif num==7:
#     print("july")
#elif num== 8:
#     print("aug")
#elif num==9 :
#     print("sep")
#lif num==10:
#     print("oct")
#elif num== 11:
#     print("nov")
#elif num ==12:
#     print("dec")
#else:
#     print("Invalid")

###in dictionary method
#user_input= int(input("Enter a number"))
 # month={1:"jan,"}

#6
#num1 =int(input("enter num1"))
#num2 = int(input("enter num2"))
#op = input("enter op")
#ops = {"+": num1+num2,"-":num1-num2}
#if op in ops:
#     print(ops[op])
#else:
 #    print('invalid symbol')

 
#8
#integer = int(input("enter an integer"))
#if integer%3==0 and integer%5==0:
#    print("FizzBuzz")
#elif integer%3==0:
#    print("Fizz")
#elif integer%5==0:
#    print("Buzz")
#else:"nothing"

#7
#salary = int(input("Enter your salary"))
#Creditscore = int(input("Enter your credit score"))
#if salary >=50000 and Creditscore >=700:
#    print("Eligiable")
#else:
#    print("Not Eligible")



### first name
#first_name = input("Enter your name: ")
#if first_name =="":
#    print("First name cannot be empty.")
#elif not first_name.isalpha():
#    print("Must be letters only")
#else:
#    print("Valid")

###Last name
#last_name = input("Enter your last name: ")
#if last_name=="":
    #print("Last name cannot be empty")
#elif last_name.isalpha:
#    print("Valid")
#else:
#    print("Must be lettrs only.")


###email
#email = input("Enter your E-mail")
#if "@"in email and "." in email:
#    print("Valid")
#else:
#    print("Invalid")


###Re-email
#re_email = input("Enter your email again")
#if re_email == email:
#    print("Valid")
#else:
#    print("E-mail and re-email doesnot match")


####Password
#password = int(input("Enter your password"))
#if len(password) >=6:
#    print("Valid")
#else:
#    print("minimum 6 characters needed")




##if not (First_name and Last_name and email and re_email):
##  print("all fields are mandatory")
#elif not(first_name.isaplha() and last_name,isalpha()):
     #print("must enter letters only")
#elif not("@" in email and "." in email and "@" in re_email and "." in re_email):
    #print("Invalid")
#elif not(email == re-email):
    #print("email not matched")
#else:
#print("Registered Sucessfully")


####   Nested 
#command1 = input("Scissor/Paper/rock")
#command2 = input("Scissor/Paper/rock")
#if command1 ==  command2:
#    print("It's a tie!!")

#elif command1 == "rock":
#  if command2 =="scissor":
#    print("Player 1 won")
#  else:
#    print("Player 2 won")
#
#elif command1=="scissor":
#  if command2=="rock":
#    print("player2 won")
#  else:
#     print("Player 1 won")
#
#elif command1 == "paper":
#    if command2 == "rock":
#        print("player1 won")
#    else:
#        print("Player 2 won")


#else:
#    print("Invalid input")


##### nested way
#balance = 20000
#is_card_valid = True

#correct_pin = 1234

#print("Weolcome to 123Back")

#user_pin = int(input("Enter your pin: "))

#if user_pin == correct_pin:
#    print ("1.check balance")
#    print(".Withdraw amount")
#    print("3.Exit")
#    choice= int(input("Select an option(1-3): "))
#    if choice ==1:
#        print(f"Your balance is {balance}")
#    elif choice ==2:
#        amount = int(input("Enter the amount"))
#          
#        if amount<= balance:
#           print(f"Please collect your cash:Rs{amount}")
#            print(f"your updated balance is Rs:{balance-amount}")
#        elif amount<=0:
#            print("Invalid amount")
#        else:
#            print("Insufficient Balance")
#    elif choice ==3:
#       print("Thank you for visiting.")
#    else:
#        print("Invalid selection")
#else:
#    print("Invalid Pin")
    

####    Elevator

#user_input = int(input("Enter your floor number (1-10):"))


#if 1<= user_input <=10:
#    print("Valid floor")
#    weight = int(input("Enter the total weight:"))
#    if weight<=500:
#        print("valid Weight")
#        door = input("Is the door closed?").lower()
#        if door =="yes":
#            print("Lift moving up")
#        else:
#            print("The door isnot closed.")
#    elif weight<0:
#        print("Invalid weight")
#    else:
#        print("weight cannot be more than 500kg")
#else:
#   print("Invalid floor")



####   Questions
#5.
total_purchase_amount = int(input("Enter your purchase amount"))
user_input = 6000
if total_purchase_amount>5000:
   has_membership = input("Do you have membership?").lower()
   if has_membership == "yes":
     persent_membership = input("do you have membership card now?").lower()
     if persent_membership =="yes": 
      discount=total_purchase_amount*0.30
      final_amount=total_purchase_amount - discount
      print(f"final amount = {discount}")
      print(f"Total saved = {final_amount}" )
     else:
        print(f"Final bill = {total_purchase_amount}")
   else:
     print(f"Final bill = {total_purchase_amount}") 
else:
    print(f"Final bill = {total_purchase_amount}")



#6
print("Welcome to the Magic Forest")
direction = input("Go north or south").lower()
if direction =="north":
   print("stage 2")
   path = input("cross the river or follow the path").lower()
   if path == ("cross the river"):
      print("Stage 3")
      angel = input("Chose fairy,ogre and elf").lower()
      if angel==("elf"):
         print("Stage 4")
      else:
         print("Game over")
   else:
      print("Game over")
else:
   print("Game Over")


#10.
body_weight = float(input("Enter your body weight"))
height = float(input("Enter your height"))
BMI = body_weight/(height**2)

if BMI<18.5:
   print("Underweight")
elif 18.5<= BMI<=25:
   print("Normal weight")
elif 25<BMI<=30:
   print("Overweight")
else:
    print("Obese")



#16
units = float(input("Enter your electricity units"))
if units<=100:
   cost = units*5
   print(f"total_cost={cost}")
elif 100<units<=300:
   cost = (100*5)+((units-100)*8)
   print(f"total cost = {cost}")
else:
   cost=(100*5)+(200*8)+((units-200)*10)
   print(f"total cost = {cost}")

#19. A store gives a 20% discount if the total purchase is above RS
#1000 AND the customer is a member, or a 10% discount if the
#purchase is above RS 1000 but the customer is not a member. Write a
#program that takes total_amount and is_member (True/False) as
#input and prints the final amount after applying the correct discount
#or no discount
total_amount=int(input("Enter your amount"))
if total_purchase_amount>1000:
   is_member = input("Are you member(yes/no?").lower()
   if is_member == "yes":
      discount=total_amount*0.20
      final_amount=total_amount-discount
      print(f"final amount={final_amount}")
   else:
      discount=total_amount*0.10
      final_amount=total_amount-discount
      print(f"Final amount={final_amount}")
else:
   print(f"Final amount={total_amount}")

#20
weight=float(input("Enter your earth weight: "))
planet={
   1:0.38,
   2:0.91,
   3:0.38,
   4:2.53,
   5:1.07,
   6:0.89,
   7:1.14
}
planet_number=int(input("Enter your planet number(1-7): "))
if planet_number in planet:
   gravity=planet[planet_number]
   print(f"weight={weight}*{planet}")
else:
   print("Invalid planet number")


#21
math =float(input("Enter maths mark"))
science =float(input("Enter science mark"))
social =float(input("Enter social mark"))
nepali =float(input("Enter nepali mark"))

total_marks=math+science+social+nepali
print(f"total marks = {total_marks}")
percentage = (total_marks/400)*100
print(f"percentage={percentage}")
if percentage > 70:
   print("grade:distinction")
elif percentage>60:
   print("First")
elif percentage>40:
   print("pass")
else:
   print("fail")

#22
is_card_valid="true"
initial_balance = 5000
correct_pin=123

pin=int(input("Enter your pin"))
if pin == correct_pin:
   while True:
      print("\n---ATM MENU---")
      print("1=Withdraw")
      print("2=check Balance")
      print("3=Exit")
      choice = input("Select an option(1-3: ")
      if choice == "1":
         amount=float(input("Enter amount to withdraw"))
         if amount<=initial_balance:
            balance = initial_balance-amount
            print(f"Rs{amount} is detucted.you current balance is Rs{balance}")
         else:
            print("indufficient balance")
      elif choice =="2":
         print(f'Balance ={initial_balance}')
      elif choice =="3":
          print("Thank you for visiting.")
      else:
         print("Invalid option.")
else:
   print("Incorrect pin")


#23
target_floor=int(input("Enter your floor number(0-10): "))
weight=float(input("Enter your weight(In KG): "))
door_status=input("Is door open or closed?: ").lower()

if 0>target_floor or target_floor>10:
   print("Invalid Floor")
elif weight>500:
   print("over weight:lift cannot move")
elif door_status =="open":
   print("WARNING:CLOSE THE DOOR")
else:
   print("ACTIVATE ELEVATOR MOTION")
