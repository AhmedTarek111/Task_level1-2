#1 =======================================================================================================================================================
#----------------------------------------------------------normal list---------------------------------------------------------------------
upper_names=[]
Names=["mahmoud","farida","ali","hassan","mohamed","khaled","taha"]
for x in Names :
        upper_names.append(x.upper())
print(upper_names)
#----------------------------------------------------------list comprehension ---------------------------------------------------------------------
upper_names=[]
Names=["mahmoud","farida","ali","hassan","mohamed","khaled","taha"]
Names=[upper_names.append(x.upper()) for x in Names ]
print(upper_names)
#----------------------------------------------------------functional programing ---------------------------------------------------------------------
upper_names=[]
Names=["mahmoud","farida","ali","hassan","mohamed","khaled","taha"]
def upper(name:str):
       return name.upper()

x=map(upper,Names)
print(list(x))
#2  =======================================================================================================================================================
#----------------------------------------------------------normal list---------------------------------------------------------------------
letter_A=[]
Names=["mahmoud","farida","ali","hassan","mohamed","khaled","taha"]
for name in Names:
        for letter_a in name:
                if letter_a == "a":
                    letter_A.append(name)
print(letter_A)
#----------------------------------------------------------list comprehension ---------------------------------------------------------------------
letter_A=[]
Names=["mahmoud","farida","ali","hassan","mohamed","khaled","taha"]
letter_A=[x for x in Names for letter_a in x if letter_a == "a"]
print(letter_A)
#----------------------------------------------------------functional programing ---------------------------------------------------------------------
Names=["mahmoud","farida","ali","hassan","mohamed","khaled","taha"]
def find_letter_a(name):
    for letters in name:
        if letters =="a":
            return name
list_of_name_contain_a=map(find_letter_a,Names)
print(list(list_of_name_contain_a))
#3  =======================================================================================================================================================
#----------------------------------------------------------normal list---------------------------------------------------------------------
Names=["mahmoud","farida","ali","hassan","mohamed","khaled","taha"]
names_start_with_t=[]
for name in Names:
    if name.startswith("t") ==True:
        names_start_with_t.append(name)
print(names_start_with_t)
#----------------------------------------------------------list comprehension ---------------------------------------------------------------------
Names=["mahmoud","farida","ali","hassan","mohamed","khaled","taha"]
Names=[name for name in Names if name.startswith("t") ==True]
print(Names)
#----------------------------------------------------------functional programing ---------------------------------------------------------------------
Names=["mahmoud","farida","ali","hassan","mohamed","khaled","taha"]
def name_start_with_t(name:str):
    for letter in name:
        if letter.startswith("t") ==True:
            return name
        else:
            return 
list_of_name_start_with_t=filter(name_start_with_t,Names)
print(list(list_of_name_start_with_t))
#4  =======================================================================================================================================================
#----------------------------------------------------------normal list---------------------------------------------------------------------
Names=["mahmoud","farida","ali","hassan","mohamed","khaled","taha"]
list_of_names_have_dublicate_a=[]
for name in Names:
    count_letter_a=name.count("a")
    if count_letter_a >= 2:
        list_of_names_have_dublicate_a.append(name)
print(list_of_names_have_dublicate_a)
#----------------------------------------------------------list comprehension ---------------------------------------------------------------------
Names=["mahmoud","farida","ali","hassan","mohamed","khaled","taha"]
Names=[name for name in Names if name.count("a") >= 2]
print(Names)

#----------------------------------------------------------functional programing ---------------------------------------------------------------------
Names=["mahmoud","farida","ali","hassan","mohamed","khaled","taha"]
def count_letter_a(name:str):
    if name.count("a") >= 2:
        return name
list_of_names_have_dublicate_a=list(filter(count_letter_a,Names))
print(list_of_names_have_dublicate_a)
#5  =======================================================================================================================================================
#----------------------------------------------------------normal list---------------------------------------------------------------------
Names=["mahmoud","farida","ali","hassan","mohamed","khaled","taha"]
list_of_len_of_each_name=[]
for name in Names:
    Names=[len(name)]
    list_of_len_of_each_name.append(len(name))
print(list_of_len_of_each_name)
#----------------------------------------------------------list comprehension ---------------------------------------------------------------------
Names=["mahmoud","farida","ali","hassan","mohamed","khaled","taha"]
list_of_len_of_each_name=[len(name) for name in Names ]
print(list_of_len_of_each_name)
#----------------------------------------------------------functional programing ---------------------------------------------------------------------
Names=["mahmoud","farida","ali","hassan","mohamed","khaled","taha"]
def len_of_names(name):
    return len(name)
list_of_len_names=list(map(len_of_names,Names))
print(list_of_len_names)
#6  =======================================================================================================================================================
        #7-------------------------------------------------------------------
Names=["mahmoud","farida","ali","hassan","mohamed","khaled","taha"]
a,*b=Names
        #8--------------------------------------------------------------------
Names=["mahmoud","farida","ali","hassan","mohamed","khaled","taha"]
a,*_,b=Names
        #9--------------------------------------------------------------------
Names=["mahmoud","farida","ali","hassan","mohamed","khaled","taha"]
a,b,*_=Names




