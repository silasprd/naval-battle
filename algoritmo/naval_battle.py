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

def validate_piece_count(piece_count, expected_count, error_message):
    if piece_count != expected_count:
        print(error_message)
        exit()
        
def process_shots(input_lines):
    shots = []
    for line in input_lines:
        parts = line.strip().split(';')
        code = parts[0]
        positions_and_direction = parts[1].split("|") if len(parts) > 1 else []
        if code == 'T':
            for position in positions_and_direction:
                positions = [position]
                shot = Shot(code, position)
                shots.append(shot)
    return shots

def process_pieces(input_lines):
    pieces = []  # Cada peça será representada como (code, positions, direction)
    for line in input_lines:
        parts = line.strip().split(';')
        code = parts[0]
        positions_and_direction = parts[1].split("|") if len(parts) > 1 else []
        if code == '3':
            for position in positions_and_direction:
                all_positions = [position]
                piece = Piece(code, all_positions, None)
                pieces.append(piece)
        else:
            for position in positions_and_direction:
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
                     
    return pieces

player1_pieces = process_pieces(jogador1_input[0:])
player2_pieces = process_pieces(jogador2_input[0:])
player1_shots = process_shots(jogador1_input[0:])
player2_shots = process_shots(jogador2_input[0:])

def proccess_points(player_pieces, opponent_shots):
    points = 0
    
    for shot in opponent_shots:
        for piece in player_pieces:
            hits = 0
            for player_positions in piece.positions:
                if shot.position in player_positions:
                    hits += 1
                    points += 3
           



    # for shot in opponent_shots:
    #     if shot.position in opponent_positions:
    #         piece_hit = None
    #         for piece in player_pieces:
    #             if shot.position in piece.positions:
    #                 piece_hit = piece
    #                 break
    #         points += 3
    #         if all(position not in opponent_positions for position in piece_hit.positions):
    #             points += 5 
    #         shots_hits += 1
    #         opponent_positions.remove(shot.position)

    # shots_missed = len(opponent_positions)
    # points += shots_hits // 5 * 5
    
    return points


player_points = proccess_points(player1_pieces, player1_shots)

print(player_points)

# player1_points, player1_targets_hit, player1_targets_missed = proccess_points(player2_pieces, player1_shots)

# player2_points, player2_targets_hit, player2_targets_missed = proccess_points(player1_pieces, player2_shots)

# winner = "J1" if player1_points > player2_points else "J2" if player2_points > player1_points else "EMPATE"

# print("Vencedor: ", winner)
# print("Player 1 points: ", player1_points)
# print("Player 2 points: ", player2_points)

# print("Player 1 - Shots")
# for shot in player1_shots:
#     print(shot.cod, shot.position)

# print("Player 1 - Pieces")
# for piece in player1_pieces:
#     print(piece.cod, piece.positions, piece.direction)
    
# print("--------------------------------------------------------")

# print("Player 2 - Shots")
# for shot in player2_shots:
#     print(shot.cod, shot.position)

# print("Player 2 - Pieces")
# for piece in player1_pieces:
#     print(piece.cod, piece.positions, piece.direction)

# Condição para adicionar 5 pontos diretamente se a peça for cod 3
        # if shot.position in code_3_positions:
        #     points += 5
        # else:
        #     points += 3

# variável utilizada para verificar se a peça acertada é de código 3, para ser adicionado +5 pontos diretamente
    # code_3_positions = {position for piece in player_pieces if piece.cod == '3' for position in piece.positions}

