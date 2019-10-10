I = input()

try:
    # try to interpret the input as a number
    f_input = float(I)
    i_input = int(f_input)

    if not (f_input-i_input) == 0:
        # the number is not integer
        print("You inserted a decimal number:\nInteger part:\t{}\nDecimal part:\t{}".format(i_input, f_input-i_input))
    else:
        # the number is integer OR 0.0
        if "." in I:
            print("You inserted a 'decimal' 0!")
        else:
            print("You inserted an integer number:\t{}".format(i_input))

except Exception as err:
    # the input is not a number

    introductionString = "my name is"

    if introductionString in I.lower():
        # catch the name!
        index = I.lower().index(introductionString) + len(introductionString)
        name = I[index:].strip(" ")
        
        if len(name) <= 0:
            # name not typed
            print("Hi!\nI'm sorry, I didn't get your name...")
        else:
            # say hello
            print("Hello " + name.capitalize() + "!")
    else:
        # suggest writing your name

        print("Hi!\nIt looks like you inserted a string...\nTry writing your name (e.g. My name is Simon)")