def palindromes(a):
    palindromes = []
    for i in range(len(a)):
        for j in range(i+1, len(a)+1):
            substring = a[i:j]
            if substring == substring[::-1]:
                palindromes.append(substring)
    return palindromes

a = "sdrpopkdad"
palindrome_list = palindromes(a)
print(palindrome_list)
