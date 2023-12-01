# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/?envType=daily-question&envId=2023-12-01
# 12-01-2023
# solved without help


def arrayStringsAreEqual(word1, word2) -> bool:
    w1 = 0
    w2 = 0
    index1 = 0
    index2 = 0
    
    while (w1 < len(word1) and w2 < len(word2)):
        if (word1[w1][index1] != word2[w2][index2]):
            return False

        index1 += 1
        index2 += 1
        print(index1, " ", index2)

        if (index1 >= len(word1[w1])):
            w1 += 1
            index1 = 0
        if (index2 >= len(word2[w2])):
            w2 += 1
            index2 = 0

    return w1 == len(word1) and w2 == len(word2)

if __name__ == '__main__':
    arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"])