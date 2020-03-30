import os

today = "Monday"

gems = """
ruby
sapphire
diamond
emerald
topaz
"""

gems2 = """
ruby,
sapphire,
diamond,
emerald,
topaz,
"""


# print today
print("Print the required Hello World to STDOUT")
print("Hello World!")
print('hello', 'world', sep=' ')
print('hello', 'world', sep='\n')

print()
print(today)
print(gems)
print(list(gems))

print('Hello, ' + os.getlogin() + '! How are you this fine' + today + '?')
print('The year is %d'%2020)
print("Today is {}!".format(today))
print(f"Hello {os.getlogin()}! How are you this fine {today}?")
print(f"Hello {os.getlogin()}! How are you this 'fine' {today}?")
print(f'Hello {os.getlogin()}! How are you this "fine" {today}?')
