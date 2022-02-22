def palindrome_checker_2019_1_60_051(a):
    if a == a[::-1]:
        return True


a = input("Enter word: ")
if palindrome_checker_2019_1_60_051(a) == True:
    print(a, "is a palindrome")
else:
    print(a, "is not a palindrome")
