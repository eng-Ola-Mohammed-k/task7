#########1###############
n = int(input('enter num of rows :'))
for row in range(1, n+1):
    for column in range(1, row + 1):
        print(column, end=' ')
    print("")
print('\n')
#########2###############
x= int(input('enter num :'))
s=0
for i in range(0,x+1):
    s += i
print(f'sum is : {s}')
print('\n')
#########3###############
n = input('enter name :')
x =0
for i in n :
     x = x + 1
     print(n[0:x])

for i in n:
    x = x - 1
    print(n[0:x])
print('\n')
#########4###############
n = str(input('Input a word to reverse :'))
print(n[::-1])
print('\n')
#########5###############
n = int(input(" Enter range: "))
i = n
while ( i >= 1):
    print (i, end = '  ')
    i = i - 1
print('\n')

#########6###############
for i in range(1,11):
    multiple = 5*i
    print(multiple,end=' ')
print('\n')
#########7###############
Limit_number  = int(input('enter the Limit_number :'))
Max_display_on_screen = int(input('enter the maximum output to display(Max_display_on_screen):'))
Target_number = int(input('enter the Target_number :'))
count = 0
num = Target_number
while num <= Limit_number and count < Max_display_on_screen :
    print(num ,end=' ')
    num += Target_number
    count += 1