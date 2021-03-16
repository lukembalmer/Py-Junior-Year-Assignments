#palindrome checker
#1: strip string of spaces
#2: check if first and last characters are the same
#3: if yes, check if remaining middle is a palindrome
def isPalindrome(text):
    def formatText(text):
        text = text.lower()
        ans = ''
        for c in text:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(text):
        if len(text) <= 1: #base case
            return True
        else:
            return text[0] == text[-1] and isPal(text[1:-1])
    
    return isPal(formatText(text))

print(isPalindrome("Able was I, ere I saw Elba"))
