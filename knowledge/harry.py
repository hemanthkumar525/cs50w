from logic import *

rain = Symbol("rain")  #it is a raining
hagrid = Symbol("hagrid") #harry visits hagrid
dumbledore = Symbol("dumbledore") #harry visits dumbledore

knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid,dumbledore)),
    dumbledore
)

print(model_check(knowledge, dumbledore))
