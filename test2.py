import test
# print(test.num)
test.num=20
# print(__name__)
print(test.num,"this is test2.py")
#this is the edit i am making to the main branch 

def mtld(word_array, ttr_threshold=0.72):
    if isinstance(word_array, str):
        raise ValueError("Input should be a list of strings, rather than a string. Try using string.split()")
    if len(word_array) < 50:
        raise ValueError("Input word list should be at least 50 in length")    
    return (mtld_calc(word_array, ttr_threshold) + mtld_calc(word_array[::-1], ttr_threshold)) / 2
