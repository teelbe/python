# strings
print("Hello World!")
print('Hello World!')
print('3 6 9 2 6 8')
print('@#5_]*^%&564')
print('========')
print('========')
message = 'Hello World!'
print(message)
print('========')
# indexing of a string
print(message[0])
print('========')
print(message[8])
print('========')
print(len(message))
print('========')
print(message[11])
print('========')
print('========')
# negative indexing of a string
print(message[-1])
print('========')
print(message[-12])
print('========')
print('========')
# slicing of a string
print(message[0:5])
print('========')
print(message[6:12])
print('========')
print('========')
# striding in a string
print(message[::2])
print('========')
print(message[0:6:2])
print('========')
print('========')
# concatenate of strings
question = ' How many people are living on the earth?'
statement = message + question
print(statement)
print('========')
print(4 * message)
# escape sequences
print('Hell World! \nHow many people are living on the earth?')
print('========')
print('Hell World! \tHow many people are living on the earth?')
print('========')
print('Hell World! \\ How many people are living on the earth?')
print('========')
print(r'Hell World! \ How many people are living on the earth?')
print('========')
print('========')
# string operations
message2 = 'hello python!'
print('Before uppercase: ', message2)
print('========')
message_upper = message2.upper()
print('After uppercase: ', message_upper)
print('========')
message_lower = message2.lower()
print('Again lowercase: ', message_lower)
print('========')
message_title = message2.title()
print('The first element of the string is uppercase: ', message_title)
print('========')
# replace() method in a string
message3 = 'Hello Python!'
message_hi = message3.replace('Hello', 'Hi')
message_python = message3.replace('Python', 'World')
print(message_hi)
print(message_python)
print('========')
print('========')
# find() method application in a string
print(message.find('Wo'))
print('========')
print(message.find('World!'))
print('========')
print(message.find('cndsjnd'))
print('========')
text = 'Jean-Paul Sartre somewhere observed that we each of us make our own hell out of the people around\nus. Had Jean-Paul known Nancy, he may have noted that at least one man, someday,\nmight get very lucky, and make his own heaven out of one of the people around him. She will be his \nmorning and his evening star, shining with the brightest and the softest light in his heaven. She will be \nthe end of his wanderings, and their love will arouse the daffodils in the spring to follow the crocuses \nand precede the irises. Their faith in one another will be deeper than time and their eternal spirit will \nbe seamlss once again.'
print(text)
print('========')
# find the first index of the substring
print(text.find('Nancy'))
print('========')
# replace the substring 'Nancy'
print(text.replace('Nancy', 'Nancy Lier Cosgrove Mullis'))
print('========')
print(text.lower())
print('========')
print(text.capitalize())
print('========')
print(text.casefold())
print('========')
# center() method will center align the string
message4 = 'Hello Leute!'
print(message4.center(50, '-'))
# count() methon returns the number of element
print(text.count('and'))
print('========')
# format method
txt = "Hello{word}"
print(txt.format(word='World!'))
print('========')
message5 = 'Hi, My name is {} and I am {} years old'
print(message5.format('Bob', 36))
message6 = 'Hi, My name is {name} and I am {number} years old'
print(message6.format(name='Bob', number=36))
message7 = 'Hi, My name is {0} and I am {1} years old'
print(message7.format('Bob', 36))
print('========')
