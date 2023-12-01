# testcases
target = __import__("12-01-2023 main")
arrayStringsAreEqual = target.arrayStringsAreEqual

def run_tests():
    assert arrayStringsAreEqual(["ab", "c"], ["a", "bc"]) == True
    assert arrayStringsAreEqual(["a", "cb"], ["ab", "c"]) == False
    assert arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]) == True
    assert arrayStringsAreEqual(["abc", "d", "defg"], ["abcddef"]) == False

if __name__ == '__main__':
    run_tests()
    
