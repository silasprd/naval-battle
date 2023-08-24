class Vessel:
    def __init__(vessel, type, position,direction):
        vessel.type = type
        vessel.position = position
        vessel.direction = direction

with open("jogador1.txt") as file:
    
    lines = file.readlines()
        
    index = None
    for i, line in enumerate(lines):
        if line.startswith("#Jogada"):
            index = i
            break
    
    vessels = lines[:index]
    shots = lines[index + 1:]
    
    for position in vessels:
        infos = position.split(";")
        vesselType = infos[0]
        movesLine = infos[1].strip().split("|")
        for move in movesLine:
            if vesselType == '3':
                vessel = Vessel(vesselType, move[0:2], None)
            else:
                vessel = Vessel(vesselType, move[:-1], move[-1:])
            print(vessel.type)       
            print(vessel.position)       
            print(vessel.direction)             
        
    # for shot in shots:
    #     print(shot)