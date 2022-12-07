def isPalindrome(x: int) -> bool:
    if x < 0: return False
    
    num = x
    reverse = 0
    
    while num:
        reverse = reverse * 10 + num % 10
        num //= 10
    
    return x==reverse

print(isPalindrome(323))
print(isPalindrome(327))