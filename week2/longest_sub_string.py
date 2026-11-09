
# LC 3

s = "deepakchand"



def longest_substring_brute_force(s):
    best = 0 

    for i in range(len(s)):
        seen = set()
        for j in range(i,len(s)):
            if s[j] in seen :
                break
            seen.add(s[j])
            best = max(best,j-i+1)
    return best


print(longest_substring_brute_force(s))



def longest_substring(s):
    seen = set() 
    left = 0 
    best = 0 
    for right in range(len(s)):
        while s[right] in seen :

            print(f"since {s[right]} exist im removing element from  my window till i dont see the {s[right]}")
            seen.remove(s[left])
            print(f"im removing {s[left]}")
            left+=1 
            print(f"im moving my left pointer or shrinking my window {s[left:right+1]} ")
        print(f"Im adding the element in my set {s[right]}")
        seen.add(s[right])
        best = max(best,right-left+1)

    return best


print(longest_substring(s))