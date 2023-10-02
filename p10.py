age=int(input("enter your age \n"))
citizen=(input("are your citizen of INDIA (y/n) \n"))
msg="you can vote" if age>=18 and citizen=='y' else "you cannot vote"
print()
