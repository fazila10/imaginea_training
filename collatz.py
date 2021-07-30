def collatz(num):
    if num==1:
        return
    else:
        if num%2==0:
            num=num//2
        else:
            num=num*3+1
        print(num)
        collatz(num)
collatz(int(input('Enter a value: ')))
