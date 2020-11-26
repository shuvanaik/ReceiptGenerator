#python programme to calculate the receipt of total item untill user press q key on keyboard
sum = 0
while(True):
    userInput = input('Enter the item price or press q to Quit: \n')
    if (userInput!= 'q'):
        sum = sum + int(userInput)
        print(f"Order total so far : {sum}")

    else:
        print("your Bill total is {sum}. Thanks for shopping with us")
        break    