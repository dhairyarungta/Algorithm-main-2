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
            if clauses[0] =="CAPTURE":
                parsed_commands.append(instr)
            
            else :
                steps = int(clauses[1])//5
                for i in range (steps):
                    parsed_commands.append(f"{clauses[0]} 5")
                
                rem = int(clauses[1])%5

                if rem!=0:
                    parsed_commands.append(f"{clauses[0]} {rem}")

        elif len(clauses) ==3:
            
            if clauses[0] =="FORWARD" and (clauses[2]=="RIGHT" or clauses[2]=="RI"):
                if clauses[1] == "TURN":
                    parsed_commands += [f"FORWARD {b}"]
                    parsed_commands += ["ROTATE 90"]
                    parsed_commands += [f"FORWARD {a}"]
                    # parsed_commands += [f"ROTATE {angle}"]
                    # for i in range(5):
                    #     parsed_commands.append(f"FORWARD {hypotenuse}")
                    # parsed_commands += [f"ROTATE {90 - angle}"]
                else :
                     parsed_commands+=["ROTATE 90"]


            elif clauses[0] == "FORWARD" and (clauses[2]=="LEFT" or classes[2]=="LE"):
                if clauses[1] == "TURN":
                    parsed_commands +=[f"FORWARD {b}"]  
                    parsed_commands +=["ROTATE -90"]
                    parsed_commands +=[f"FORWARD {a}"]
                    # parsed_commands += [f"ROTATE {-angle}"]
                    # for i in range(5):
                    #     parsed_commands.append(f"FORWARD {hypotenuse}")
                    # parsed_commands += [f"ROTATE {-90 + angle}"]
                else :

                    parsed_commands+=["ROTATE -90"]

            elif clauses[0] =="BACKWARD" and (clauses[2]=="LEFT" or clauses[2]=="LE"):
                parsed_commands +=[f"BACKWARD {a}"]
                parsed_commands += ["ROTATE 90"]
                parsed_commands+= [f"BACKWARD {b}"] 
                # parsed_commands += [f"ROTATE {angle}"]
                # for i in range(5):
                #     parsed_commands.append(f"BACKWARD {hypotenuse}")
                # parsed_commands += [f"ROTATE {90 - angle}"]

            elif clauses[0]="BACKWARD" and (clauses[2]=="RIGHT" or clauses[2]=="RI"):
                parsed_commands += [f"BACKWARD {a}"]
                parsed_commands += ["ROTATE -90"]
                parsed_commands += [f"BACKWARD {b}"]
                # parsed_commands += [f"ROTATE {- angle}"]
                # for i in range(5):
                #     parsed_commands.append(f"BACKWARD {hypotenuse}")
                # parsed_commands += [f"ROTATE {-90 + angle}"]
    return parsed_commands
