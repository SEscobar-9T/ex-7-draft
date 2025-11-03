# working with tuples
from pyscript import display


songbird = ('Katseye', 'Laufey', 'Taylor Swift')
item1, item2, item3 = songbird # unpacking a tuple


display(f'My favorite pop group is {item1}', target='output')
display(f'My favorite singer/s is {item2}', target='output')
display(f'My favorite singer/s is {item3}', target='output')

katseye = ['Manon', 'Sophia', 'Daniela', 'Lara', 'Megan', 'Yoonchae']
converted_tuple = (katseye) # convert to tuple

display(katseye, target='output')
display(converted_tuple, target='output')

num1 = 9
num2 = 21
comparison = num1 == num2
comparison2 = num1 != num2
comparison3 = num1 > num2
comparison4 = num1 < num2
comparison5 = num1 >= num2
comparison6 = num1 <= num2


display(comparison, target='output')
display(comparison2, target='output2')
display(comparison3, target='output2')
display(comparison4, target='output2')
display(comparison5, target='output2')
display(comparison6, target='output2') # comparing
