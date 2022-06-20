from cgi import print_environ
from turtle import update


python = {
    "hemanth" : "the best coder",
    'fast' : 'the quick manner',
    'marks' : [1, 2, 3],
    'anotherdict' : {'harry': 'player'},
    'quick' : "fastest",
}
print(list(python.keys())) #print the keys of the dictionary
print(list(python.values())) # print the values of the dictionary
print(list(python.items())) # print the values in the dictionary
print(list(python.get("marks")))
print(list(python.get("hemanth")))
print(python)
updatepython ={
    'my mom' : 'my weakness',
    'my dad' : 'my strength'
}
python.update(updatepython)
print(python)