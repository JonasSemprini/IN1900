#Oppgave 4.6
while True:
    value = input("Provide some input, q to quit: ")
    if value == 'q':
        break

    result = eval(value)
    print(result, type(result))
    
