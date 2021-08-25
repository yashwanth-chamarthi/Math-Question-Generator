import random

def arithm_qsns():
    choice = int(input('please select\n 1.add \n 2.sub \n 3.multi \n 4.div\n :'))
    y = True

    while y:
        a = random.randint(1,100)
        b = random.randint(1,100)
        if choice == 1:
            print(str(a)+'+'+str(b))
            ans = input('please enter the sum : ')
            while int(ans)!= (a+b):
                print(str(a)+'+'+str(b))
                ans = input('please enter the sum : ')
            else:    
                print('your ans is correct')
                choice2 = input('do you want to continue ? select "y" or "n" :')
                if choice2 == 'y':
                    continue
                elif choice2 == 'n':
                    break
        if choice == 2:
            print(str(a)+'-'+str(b))
            ans = input('please enter the diff : ')
            while int(ans)!= (a-b):
                print(str(a)+'-'+str(b))
                ans = input('please enter the diff : ')
            else:    
                print('your ans is correct')
                choice2 = input('do you want to continue ? select "y" or "n" :')
                if choice2 == 'y':
                    continue
                elif choice2 == 'n':
                    break
        if choice == 3:
            print(str(a)+'*'+str(b))
            ans = input('please enter the product : ')
            while int(ans)!= (a*b):
                print(str(a)+'*'+str(b))
                ans = input('please enter the product : ')
            else:    
                print('your ans is correct')
                choice2 = input('do you want to continue ? select "y" or "n" :')
                if choice2 == 'y':
                    continue
                elif choice2 == 'n':
                    break
        if choice == 4:
            print(str(a)+'/'+str(b))
            ans = input('please enter the division rounded upto 2 digits : ')
            while int(ans)!= round((a/b),2):
                print(str(a)+'/'+str(b))
                ans = input('please enter the division rounded upto 2 digits : ')
            else:    
                print('your ans is correct')
                choice2 = input('do you want to continue ? select "y" or "n" :')
                if choice2 == 'y':
                    continue
                elif choice2 == 'n':
                    break
arithm_qsns()