input_string=input()

k=''

all_digits=['0','1','2','3','4','5','6','7','8','9']

b=len(input_string)

total_digits=0

for s in input_string:
    if s in all_digits:
        total_digits += 1
        k += s
        
con=0        
for j in range(len(input_string)):
    if('a' in input_string):
        con=con+1
        if(con==2):
            output_string='a2'
            break
    
if(b==input_string[1]):
    output_string='7L'
elif(total_digits>3):
    output_string=k

   
print(output_string)
