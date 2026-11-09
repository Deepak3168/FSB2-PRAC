s = "A man a plan, a canal : Panama"
def is_valid_palindrome(s):
    l = 0 
    r = len(s)-1

    while l<r :
        # print(s[l] ,s[r])
        while l<r and  not s[l].isalnum():
            l+=1
        while l<r and not s[r].isalnum():
            r-=1
        
        if s[l].lower() != s[r].lower() :
            print("Not a valid palindrome")
            return False
        l+=1
        r-=1
    return True

print(is_valid_palindrome(s))
