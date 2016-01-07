string =raw_input("Enter the string:")
str_rev = reversed(string)
if list(string) == list(str_rev):
   print "The given string is a palindrome"
else:
    print "The given string is not a palindrome"
