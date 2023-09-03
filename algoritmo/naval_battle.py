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


print("Player 1 - Shots")
for shot in player1_shots:
    print(shot.cod, shot.position)

print("Player 1 - Pieces")
for piece in player1_pieces:
    print(piece.cod, piece.positions, piece.direction)
    
print("--------------------------------------------------------")

print("Player 2 - Shots")
for shot in player2_shots:
    print(shot.cod, shot.position)

print("Player 2 - Pieces")
for piece in player1_pieces:
    print(piece.cod, piece.positions, piece.direction)

