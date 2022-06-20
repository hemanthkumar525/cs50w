people = [
    {'name':'hemanth', 'dept':'computer science\n'},
    {'name':'adithya',  "dept":'eletronics\n'},
    {'name':'rajesh', "dept":'mechanical'}
]


people.sort(key=lambda person: person['dept'])

print(people)