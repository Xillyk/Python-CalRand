import random
import math
func = ['Add', 'Subtract', 'Multiply', 'Divide', 'Sin', 'Cosine', 'Tan', 'Square Root', 'Power', 'BMI', 'Random Number']
# input_value = {'Add':2, 'Subtract':2, 'Multiply':2, 'Divide':2, 'Sin':1, 'Cosine':1, 'Tan':1, 'Square Root':1, 'Power':2, 'BMI':2, 'Random Number':2}
input_value = {1: 2, 2: 2, 3: 2, 4: 2, 5: 1, 6: 1, 7: 1, 8: 1, 9: 2, 10: 2, 11: 2}
def options(option):
    if option == 1:
        val_1, val_2 = input_val(option)
        result = add(val_1, val_2)
    elif option == 2:
        val_1, val_2 = input_val(option)
        result = subtract(val_1, val_2)
    elif option == 3:
        val_1, val_2 = input_val(option)
        result = multiply(val_1, val_2)
    elif option == 4:
        while(True):
            val_1, val_2 = input_val(option)
            result = divide(val_1, val_2)
            if result != 'divide by zero exception':
                break
            else:
                print('Error: Divide by zero -> Try Again')
    elif option == 5:
        val = input_val(option)
        result = sin(val)
    elif option == 6:
        val = input_val(option)
        result = cosine(val)
    elif option == 7:
        val = input_val(option)
        result = tan(val)
    elif option == 8:
        while(True):
            val = input_val(option)
            result = sqrt(val)
            if result != 'sqrt of negative number':
                break
            else:
                print('Error: SQRT of negative number -> Try Again')
    elif option == 9:
        while(True):
            val_1, val_2 = input_val(option)
            result = pow(val_1, val_2)
            if result != 'math error':
                break
            else:
                print('Error: Math Error -> Try Again')
    elif option == 10:
        while(True):
            print('value 1: Weight (Kg) | value 2: Height (m)')
            val_1, val_2 = input_val(option)
            result = bmi(val_1, val_2)
            if result != 'weight or height less than 0':
                break
            else:
                print('Error: Weight or Height Error -> Try Again')
    elif option == 11:
        val_1, val_2 = input_val(option)
        result = random_num(val_1, val_2)
    return result
def input_val(option):
    state = True
    if input_value.get(option) == 1:
        while (state):
            val = input('Enter value : ')
            state = check_val_1(val)
        return val
    elif input_value.get(option) == 2:
        while (state):
            val_1 = input('Enter value 1 : ')
            val_2 = input('Enter value 2 : ')
            state = check_val_2(val_1, val_2)
        return val_1, val_2
def check_val_1(val):
    state_val = True
    try:
        val = int(val)
        state_val = False   
    except ValueError:
        try:
            float(val)
            state_val = False     
        except ValueError:
            state_val = True
            print("This is not a number. Try Again")
    return state_val
def check_val_2(val_1, val_2):
    state_val_1 = True
    state_val_2 = True
    try:
        val_1 = int(val_1)
        state_val_1 = False
    except ValueError:
        try:
            float(val_1)
            state_val_1 = False
        except ValueError:
            state_val_1 = True
    try:
        val_2 = int(val_2)
        state_val_2 = False
    except ValueError:
        try:
            float(val_2)
            state_val_2 = False
        except ValueError:
            state_val_2 = True
    if state_val_1 or state_val_2:
        print("This is not a number. Try Again")
        return True
    else:
        return False
def add(val_1, val_2):
    return float(val_1) + float(val_2)
def subtract(val_1, val_2):
    return float(val_1) - float(val_2)
def multiply(val_1, val_2):
    return float(val_1) * float(val_2)
def divide(val_1, val_2):
    if float(val_2) == 0.0:
        return 'divide by zero exception'
    else:
        return float(val_1) / float(val_2)
def sin(val):
    return round(math.sin(float(val)), 3)
def cosine(val):
    return round(math.cos(float(val)), 3)
def tan(val):
    return round(math.tan(float(val)), 3)
def sqrt(val):
    if float(val) < 0.0:
        return 'sqrt of negative number'
    else:
        return round(math.sqrt(float(val)), 3)
def pow(val_1, val_2):
    if float(val_1) == 0.0 and float(val_2) < 0.0:
        return 'math error'
    else:
        return round(math.pow(float(val_1), float(val_2)), 3)
def bmi(weight, height):
    if float(weight) < 0.0 or float(height) < 0.0:
        return 'weight or height less than 0'
    else:
        return round(float(weight) / (float(height) * float(height)), 3)
def random_num(val_1, val_2):
    return random.randint(float(val_1), float(val_2))