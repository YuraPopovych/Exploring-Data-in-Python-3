
def calculate_max_min():

    ar = []

    while(True):
        number = input("Enter a number:")

        if (number == 'done'):
            max_value = max(ar)
            min_value = min(ar)
            print('Maximum: ', max_value)
            print('Minimum: ', min_value)
            exit()

        try:
            number = float(number)
            ar.append(number)

        except:
            print ("Only number type are allowed")
            continue

print(calculate_max_min())