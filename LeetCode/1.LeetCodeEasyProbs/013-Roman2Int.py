def Roman2Int(num):
    roman_dict = {
        "I" : 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    num_arr = []

    #First edge case if the value is simply a one digit entity
    for key, value in roman_dict.items():
        if key == num:
            return value
        

    #For multiple values
    for char in num:
        for key, value in roman_dict.items():
            if char == key:
                num_arr.append(value)

    
    for i, j in enumerate(num_arr[:-1]):
        if j  < num_arr[i+1]: 
            num_arr[i] = num_arr[i+1] - num_arr[i] 
            num_arr[i+1] = 0

    return sum(num_arr)

print(Roman2Int("XXI"))