class Piece:
    def __init__(piece, cod, positions, direction):
        piece.cod = cod
        piece.positions = positions
        piece.direction = direction

class Shot:
    def __init__(shot, cod, position):
        shot.cod = cod
        shot.position = position

def read_input_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines

jogador1_input = read_input_file('jogador1.txt')
jogador2_input = read_input_file('jogador2.txt')



def validate_shot_positions(positions, current_player):
    for position in positions:
        if len(position) < 2:
            return False
        
        x = position[1:]
        y = position[0]
        
        if not ('A' <= y <= 'P' and not y.isdigit() and y != 'K') or not (1 <= int(x) <= 15):
            error_message = f"{current_player} ERROR_POSITION_NONEXISTENT_VALIDATION"
            with open("resultado.txt", 'w') as file:
                file.write(error_message)
            exit() 

def validate_piece_positions(pieces, current_player):
    for piece in pieces:
        for position in piece.positions:
            if len(position) < 2:
                return False

            x = position[1:]
            y = position[0]

            if not ('A' <= y <= 'P' and not y.isdigit() and y != 'K') or not (1 <= int(x) <= 15):
                error_message = f"{current_player} ERROR_POSITION_NONEXISTENT_VALIDATION"
                with open("resultado.txt", 'w') as file:
                    file.write(error_message)
                exit()   

def validate_no_duplicate_piece_positions(pieces, current_player):
    all_positions = set()

    for piece in pieces:
        for position in piece.positions:
            if position in all_positions:
                error_message = f"{current_player} ERROR_OVERWRITE_PIECES_VALIDATION"
                with open("resultado.txt", 'w') as file:
                    file.write(error_message)
                exit()
            all_positions.add(position)
       
        
def process_shots(input_lines, current_player):
    shots = []
    torpedo_count = 0
    
    for line in input_lines:
        parts = line.strip().split(';')
        code = parts[0]
        positions_and_direction = parts[1].split("|") if len(parts) > 1 else []
        if code == 'T':
            for position in positions_and_direction:
                positions = [position]
                shot = Shot(code, position)
                shots.append(shot)
                torpedo_count += 1
    
    if torpedo_count != 25:
        error_message = f"{current_player} ERROR_NR_PARTS_VALIDATION"
        with open("resultado.txt", 'w') as file:
            file.write(error_message)
        exit()
        
    return shots



def process_pieces(input_lines, current_player):
    pieces = []  # Cada peça será representada como (code, positions, direction)
    code_count = {'1': 0, '2': 0, '3': 0, '4': 0}
    occupied_positions = set()
    
    for line in input_lines:
        
        parts = line.strip().split(';')
        code = parts[0]
        positions_and_direction = parts[1].split("|") if len(parts) > 1 else []
        
        if code == '3':
            for position in positions_and_direction:
                all_positions = [position]
                piece = Piece(code, all_positions, None)
                pieces.append(piece)
                code_count[code] += 1           
        else:
            for position in positions_and_direction:
                occupied_positions.add(position)
                
                nPositions = 0
                if code == '1':
                    nPositions = 4
                elif code == '2':
                    nPositions = 5
                elif code == '4':
                    nPositions = 2
                elif code == 'T':
                    break
                direction = position[-1:]
                initial_position = position[:-1]
                all_positions = [initial_position]
                if direction == 'H':         
                    base_row = ord(initial_position[0])
                    base_col = int(initial_position[1:])
                    for i in range(1, nPositions):
                        new_row = base_row
                        new_col = base_col + i
                        new_position = chr(new_row) + str(new_col)
                        all_positions.append(new_position)
                elif direction == 'V':
                    base_row = ord(initial_position[0])
                    base_col = int(initial_position[1:])
                    for i in range(1, nPositions):
                        new_row = base_row + i
                        new_col = base_col
                        new_position = chr(new_row) + str(new_col)
                        all_positions.append(new_position)
                piece = Piece(code, all_positions, direction)
                pieces.append(piece)
                code_count[code] += 1
                   
    if code_count['1'] != 5 or code_count['2'] != 2 or code_count['3'] != 10 or code_count['4'] != 5:
        error_message = f"{current_player} ERROR_NR_PARTS_VALIDATION"
        with open("resultado.txt", 'w') as file:
            file.write(error_message)
        exit() 
                        
    return pieces

player1_pieces = process_pieces(jogador1_input[0:], "J1")
player1_shots = process_shots(jogador1_input[0:], "J1")
validate_no_duplicate_piece_positions(player1_pieces, "J1")
validate_piece_positions(player1_pieces, "J1")
validate_shot_positions([shot.position for shot in player1_shots], "J1")

player2_pieces = process_pieces(jogador2_input[0:], "J2")
player2_shots = process_shots(jogador2_input[0:], "J2")
validate_no_duplicate_piece_positions(player2_pieces, "J2")
validate_piece_positions(player2_pieces, "J2")
validate_shot_positions([shot.position for shot in player2_shots], "J2")

def proccess_points(player_pieces, opponent_shots):
    points = 0
    shots_hits = 0
    shots_missed = 0
    
    for piece in player_pieces:
        hits = 0
        last_hit_position = None
        for player_positions in piece.positions:
            for shot in opponent_shots:
                if shot.position == player_positions:
                    hits += 1
                    last_hit_position = shot.position
                    break
        if len(piece.positions) == 1:
            if hits == 1:
                points += 5
                shots_hits += 1
            else: 
                shots_missed += 1
        else:
            if hits == len(piece.positions):
                for player_positions in piece.positions:
                    if player_positions == last_hit_position:
                        points += 5
                    else: 
                        points += 3
                shots_hits += 1
            else:
                points += hits * 3
                shots_missed += 1
        
    return points, shots_hits, shots_missed
           
player2_points, player2_shots_hit, player2_shots_missed = proccess_points(player1_pieces, player2_shots)
player1_points, player1_shots_hit, player1_shots_missed = proccess_points(player2_pieces, player1_shots)

def generate_output(players, file_name):
    with open(file_name, 'w') as file:
        for i, player in enumerate(players):
            output = f"{player['winner']} {player['hits']}AA {player['missed']}AE {player['points']}PT"
            file.write(output)
            if i < len(players) - 1:
                file.write('\n')

if player1_points > player2_points:
    winner = "J1"
    hits = player1_shots_hit
    missed = player1_shots_missed
    points = player1_points
    player_data = {'winner': winner, 'hits': hits, 'missed': missed, 'points': points}
else:
    if player1_points < player2_points:
        winner = "J2"
        hits = player2_shots_hit
        missed = player2_shots_missed
        points = player2_points
    else:
        winner = "J1"
        hits = player1_shots_hit
        missed = player1_shots_missed
        points = player1_points
        player1_data = {'winner': "J1", 'hits': hits, 'missed': missed, 'points': points}
        
        winner = "J2"
        hits = player2_shots_hit
        missed = player2_shots_missed
        points = player2_points
        player2_data = {'winner': "J2", 'hits': hits, 'missed': missed, 'points': points}       
        generate_output([player1_data, player2_data], "resultado.txt")
        exit()

player_data = {'winner': winner, 'hits': hits, 'missed': missed, 'points': points}
    
generate_output([player_data], "resultado.txt")
    
    
