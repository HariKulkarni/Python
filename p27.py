#prog to read the string and count the no of vowels
string=input("enter any string")
vowels=0

for i in string:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' ):
            vowels=vowels+1
print(f"no of vowels={vowels}")
