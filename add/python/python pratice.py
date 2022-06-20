 #f1 = input('enter Frutis number 1:')
 #f2 = input('enter Frutis number 2:')
 #f3 = input('enter Frutis number 3:')
 #f4 = input('enter Frutis number 4:')
 #f5 = input('enter Frutis number 5: ')
 #f6 = input('enter Frutis number 6:')
 #f7 = input('enter Frutis number 7:')

 #myfrutislist = [f1, f2, f3, f4, f5, f6, f7]
 #print(myfrutislist)

 #to find greatest of 4 number

 
#a = int(input())
#b = int(input())
#c = int(input())
#d = int(input())
#
#if(a>d) :
#    f1 = a
#else :
#    f1 = d 
#
#if(b>d) :
#    f2 = b
#else :
#    f2 = a
#
#if(f1>f2) :
#    print(str(f1) + " is greater")
#else:
#    print(str(f2) + " is greater")




#a = int(input('enter english marks\n'))
#b = int(input('enter maths marks\n')) 
#c = int(input('entter programming marks\n'))

#if(a<33 or b<33 or c<33):#
    # print('u r failed bcoz lees in subject marks')
#elif(a+b+c)/3 < 40:#
   # print('u r failed  for less score in total ')
#else :
    # print('CONGRAJULATION! YOU HAVEE PASSED THE TESt')
  




#   Text = input('enter a text\n')

#   if('make alot of money ' in Text):
#       spam = True
#   elif('buy now' in Text):
 #      spam = True
#   elif('click this' in Text):
#       spam = True
#   elif('subscribe this' in Text):
#       spam = True
#   else:
#       spam = False  

#   if(spam):
#       print('this a spam comment')
#   else:
#       print('this is not a spam comment')




#  a = input('enter a string to find the charater by user\n')

#  if(len(a)<10):
#      print('the given text contain less than 10 character ')
#  else:
#      print('the given character is more than 10')





#  a = ['hemanth,baji,subhadra,sai']
#  b = input('enter any text\n')

#  if(b in a):
#      print('the character is in list')
#  else:
#      print('the name is not in list')


# conditional 


# a = int(input('enter the marks\n'))

##if(a>=90):
#    print('the student is extra ordinary')
#elif(a>=80):
#    print('the student is A')
#elif(a>=70):
#    print('the student is B')
#elif(a>=60):
#    print('the student is C')
#elif(a>=50):
 #   print('the student is D')
#else:
   # print('the student is failed')


# loops (for, while)


#a = int(input('enter a number\n'))
#for i in range(1, 11):
 #   print(f"{a}X{i}={a*i}")     # print multiplcation of for loop





#   l1 = ['haryy', 'soban', 'sahil', 'sunny']

#   for name in l1:
#       if name.startswith("s"):
#           print("hello " +  name)





number = int(input ("Enter the number of which the user wants to print the multiplication table: "))      
count = 1    
# we are using while loop for iterating the multiplication 10 times      
print ("The Multiplication Table of: ", number)    
while count <= 10:    
    number = number * 1    
    print (number, 'x',  '=', number * count)    
    count += 1    
    