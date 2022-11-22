listoffruit = ['apple', 'orange', 'pear']
print(listoffruit)

has_kiwi = False
for fruit in listoffruit:
    print('I am in the loop')
    print(fruit)
    if fruit == 'kiwi':
        has_kiwi = True
        break

has_kiwi_2 = False
index = 0
while not has_kiwi_2 and index < len(listoffruit):
    has_kiwi_2 = listoffruit[index] == 'kiwi'
    index += 1


print('loop has ended')
print(f'Do we have kiwi in the list {has_kiwi}')
print(f'has kiwi 2 = {has_kiwi_2}')
