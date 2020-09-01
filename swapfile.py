sm1 = "this is sample text1"
sm2 = "this is sample text2"


sm1 = input('Enter string to be swapped with other file: ')
sm2 = input('Enter string to be swapped with the first file: ')


temp = sm1
sm1 = sm2
sm2 = temp

print('The value of sm1 after swapping: {}'.format(sm1))
print('The value of sm2 after swapping: {}'.format(sm2))
    