def isPalindrome(str):
    s = 0
    e = len(str) - 1
    while( s < e):
        if str[s] != str[e]:
            return False
        s+=1
        e-=1
    return True


str = input("Enter any string: ")
if(isPalindrome(str)):
    print("The give string is a palindrome!!")
else:
    print("The give string is not a palindrome!!")