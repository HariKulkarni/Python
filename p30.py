#prog to count the no os digits in a given string and character
string="a1b2c3"
s=0
c=0
for i in string:
    if(i=='1' or i=='2' or i=='3'):
        s=s+1
    else:
        c=c+1

print(f"no of digits={s}")
print(f"no of character={c}")


