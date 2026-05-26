import test
# print(test.num)
test.num=20
# print(__name__)
print(test.num,"this is test2.py")
print(tes.num==true)
#bought some new changed to the repo hehe eeee
#from hereee:
# MTLD internal implementation
def mtld_calc(word_array, ttr_threshold):
    current_ttr = 1.0
    token_count = 0
    type_count = 0
    types = set()
    factors = 0.0
    for token in word_array:
        token = token.translate(None, string.punctuation).lower() # trim punctuation, make lowercase        
        token_count += 1
        if token not in types:
            type_count +=1
            types.add(token)
        current_ttr = float(type_count) / token_count
        if current_ttr <= ttr_threshold:
            factors += 1
            token_count = 0
            type_count = 0
            types = set()
            current_ttr = 1.0
