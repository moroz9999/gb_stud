# Lesson2, Ex.3. Var. Dictionary
mounth = int(input("Enter the mounth's number: "))
dic = {1: ('January', 'Winter'),
       2: ('February', 'Winter'),
       3: ('March', 'Spring'),
       4: ('April', 'Spring'),
       5: ('May', 'Spring'),
       6: ('June', 'Summer'),
       7: ('July', 'Summer'),
       8: ('August', 'Summer'),
       9: ('September', 'Autumn'),
       10: ('October', 'Autumn'),
       11: ('November', 'Autumn'),
       12: ('December', 'Winter')
       }
print(f'The mounth you entered: {dic.get(mounth)[0]}. It\'s {dic.get(mounth)[1]}')
