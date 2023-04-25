# 1_________________________________________________________________________________________________________________________
def even_odd(x:int,y:int):
    even_list=[E for E in range(x,y) if E %2 ==0 ];odd_list=[O for O in range(x,y) if O %3 ==0 ]  
    print(f"Even numbers = {even_list} \n \n  Odd numbers = {odd_list}")
# 2_________________________________________________________________________________________________________________________
def numbers_divided_on_parameters(x,y):
    for range_numbers in range(1,101):
        if (range_numbers % x ==0 and  range_numbers %y == 0)  : 
            print(range_numbers)

numbers_divided_on_parameters(1000,50)
# 3_________________________________________________________________________________________________________________________
def multiplication_table(x:int,y:int):
    for q in range(x,y+1):
        for w in range(1,11):
            multiplication=q*w
            print(w,"*",q,"=",multiplication,)
        print(50*"-")
# 4_________________________________________________________________________________________________________________________      
def remove_duplicate(sentence:str):
    split_sentence=sentence.split() ;    o=[]
    [o.append(x) for x in split_sentence if x not in o]  ; print(" ".join(o))
# 5_________________________________________________________________________________________________________________________      
def count_words(sentence:str):
    split_sentence=sentence.split() ; print(len(split_sentence))
# 6_________________________________________________________________________________________________________________________    
def remove_word_from_sentence(sentence:str,word:str):
    sentence2=sentence.replace(word,""); print(sentence2)
# 7_________________________________________________________________________________________________________________________
def count_repeated_word_in_sentence(sentence:str,word:str):
    sentence2=sentence.count(word) ; print(sentence2)
# 8_________________________________________________________________________________________________________________________
def number_able_divisible_by_y(x:int,y:int)->int:
    for x in range(x,101):
        if x%y==0:
            print(x)