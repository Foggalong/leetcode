#!/usr/bin/env python3

function = "big(x,y)=sqrt(x+y)*10"

name = function.split("=")[0].replace("(", "(float ").replace(",", ",float ")
for op in ["sqrt", "sin", "cos", "tan", "exp", "log"]:
    actions = function.split("=")[1].replace(op, op+"f")
actions = actions.replace("abs", "fabsf") + ";"

print("float %s\n{\n\treturn %s\n}" % (name, actions))
