import sys

try: #try-block for arguments given in the terminal
    t = float(sys.argv[1])
    g = 9.81
    v0 = float(sys.argv[2])
    y = v0*t - 0.5*g*t**2
    print(f"After a time {t}s the distance the ball has traveled is {y: .2f} m")
except IndexError: #an exception if the try-block is not fulfilled with an input statement instead
    print('No command-line argument for v0 and t!')
    t = float(input("Time: ")) #input function for time values
    v0 = float(input("Velocity: ")) #input function for velocity values
    g = 9.81
    y = v0*t - 0.5*g*t**2
    print(f"After a time {t}s the distance the ball has traveled is {y: .2f} m")
except ValueError: #Added exception if the both the try and except IndexError block requirements are not met
    print('t and v0 has be pure numbers!')

"""
Output: python ball_cml_qa.py

Note:
For both the system arguments and the input values the result will be printed equally.
If either the try or the except-block for IndexError is fulfilled the program will run as usual.
If none of the statements over are met, the terminal will simply print the except-block for ValueError.
"""
