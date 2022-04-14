users = [{'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'sex': 'M'},
    {'mail': 'hintoncynthia@hotmail.com', 'name': 'Madison Martinez', 'sex': 'F'},
    {'mail': 'wwagner@gmail.com', 'name': 'Michael Jenkins', 'sex': 'M'},
    {'mail': 'daniel79@gmail.com', 'name': 'Karen Rodriguez', 'sex': 'F'},
    {'mail': 'ujackson@gmail.com', 'name': 'Amber Rhodes', 'sex': 'F'}]

print(users)
result = map(lambda u: u['mail'], users)
print(type(list(result)))