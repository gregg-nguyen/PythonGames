# Write a function that takes in a single letter, and returns a 5x5 representation of that letter
# (Only from A -> M)

def print_big(letter):
    patterns = {1:'*', 2:'**', 3:'***', 4:'****', 5:'*****', 6:'*   *', 7:' * * ', 8:'  *  ', 9:'*  * ',
                10:' *** ', 11:'* *  ', 12:'** **', 13:'* * *'}
    dictionary = {'A':[8,7,5,6,6], 'B':[4,6,4,6,4], 'C':[10,6,1,6,10], 'D':[4,6,6,6,4], 'E':[5,1,5,1,5],
                  'F':[5,1,5,1,1], 'J':[5,8,8,11,3], 'K':[6,11,1,11,6], 'L':[1,1,1,1,5], 'M':[6,12,13,6,6]}
    for values in dictionary[letter.upper()]:
        print(patterns[values])
