#prog to count the no os digits in a given string
string="a1b2c3123"
s=0
for i in string:
    if(i=='1' or i=='2' or i=='3'):
        s=s+1
print(f"no of digits={s}")
