#Ask the user to type in the first line of a nursery rhyme and
#display the length of the string. Ask for a starting number and an
#ending number and then display just that section of the text
#(remember Python starts counting from 0 and not 1).

rhyme = input('Enter the rhyme: ')
print('length of the string',len(rhyme))
sNum = int(input('Enter the starting number'))
lNum = int(input('Enter the last number'))

print(rhyme[sNum:lNum])