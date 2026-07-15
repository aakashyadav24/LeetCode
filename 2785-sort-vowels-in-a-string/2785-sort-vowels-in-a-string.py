class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i' , 'o' , 'u']
        vowel = ""
        for c in s:
            if c in vowels:
                vowel += c
        sorted_vowel =''.join(sorted(vowel))
        t = ""
        i = 0
        for c in s:
            if c in vowels:
                t += sorted_vowel[i]
                i +=1
            else:
                t += c
        return t.strip('')
