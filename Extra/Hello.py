#Oppgave 7_10
class Hello:
    def __call__(self, text):
        return 'Hello, ' + text + '!'
    def __str__(self):
        return 'Hello World!'

a = Hello()
print(a('students'))
print(a)
