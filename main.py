def list_comprehension_exercise_1():
    output = [num for num in range(11)]
    return output

print(list_comprehension_exercise_1())

##############################################################################  

def list_comprehension_exercise_2():
    output = [num for num in range(22) if num % 2 == 0 or num % 3 == 0]
    return output

print(list_comprehension_exercise_2())

##############################################################################  

def list_comprehension_exercise_3():
    output = [num for num in range(-5,32) if num % 2 == 1 and num % 5 != 0]
    return output

print(list_comprehension_exercise_3())

##############################################################################  

def list_comprehension_exercise_4():
    output = [num ** 2 for num in range(11)]
    return output

print(list_comprehension_exercise_4())

##############################################################################  

def list_comprehension_exercise_5(sentence):
    output = [letter for letter in sentence if letter.isupper()]
    return output

sentence = 'O Rato Rui Gosta De QueiJo FresQuiNho'
print(list_comprehension_exercise_5(sentence))

##############################################################################

def list_comprehension_exercise_6(sentence):
    splitted_word = sentence.split(' ')
    output = [word for word in  splitted_word if word[0].lower() == 'r' and len(word) > 3]
    return output

sentence = 'o rato rui roeu a roupa do rei de roma'
print(list_comprehension_exercise_6(sentence))
