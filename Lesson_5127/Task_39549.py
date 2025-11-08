word1 = input()
word2 = input()
word3 = input()
word4 = (word1 * (len(word1) < len(word2)) +
         word2 * (len(word2) < len(word1)) +
         (len(word1) == len(word2)) * (word1 * (word1 < word2) + word2 * (word2 <= word1)))
word5 = (word4 * (len(word4) < len(word3)) +
         word3 * (len(word3) < len(word4)) +
         (len(word4) == len(word3)) * (word4 * (word4 < word3) + word3 * (word3 <= word4)))
print(word5)