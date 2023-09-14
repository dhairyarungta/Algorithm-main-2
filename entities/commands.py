from tkinter import COMMAND
from constants import STM_COMMANDS, TR
import math
COMMANDS = STM_COMMANDS

def parse(commands):
    parsed_commands =[]
    a,b = TR["90 Turn"]
    angle = round(math.degrees(math.atan(b/a)))
    hypotenuse = round(math.sqrt(a**2 + b**2)/5,2)

    for instr in commands:
        clauses = instr.split(" ")
        if len(clauses) ==2:
            if clasuses[0] =="CAPTURE":
                
