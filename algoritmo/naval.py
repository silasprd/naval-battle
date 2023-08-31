class Piece:
    def __init__(piece, cod, positions, direction):
        piece.cod = cod
        piece.positions = positions
        piece.direction = direction

def read_input_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines

jogador1_input = read_input_file('jogador1.txt')
jogador2_input = read_input_file('jogador2.txt')

#print(jogador1_input)
#print(jogador2_input)

def validate_piece_count(piece_count, expected_count, error_message):
    if piece_count != expected_count:
        print(error_message)
        exit()

def process_pieces(input_lines):
    pieces = []  # Cada peça será representada como (code, positions, direction)
    for line in input_lines:
        parts = line.strip().split(';')
        code = parts[0]
        positions_and_direction = parts[1:]
        if code == '3':
            positions = positions_and_direction[0].split("|")
            for position in positions:
                all_positions = [position]
                piece = Piece(code, all_positions, None)
                pieces.append(piece)
        elif code == '1':
            positions = positions_and_direction[0].split("|")
            for position in positions:
                direction = position[-1:]
                initial_position = position[:-1]
                all_positions = [initial_position]
                if direction == 'H':         
                    base_row = initial_position[0]
                    for i in range(1, 4):
                        new_position = base_row + chr(ord(initial_position[1]) + i)
                        all_positions.append(new_position)
                elif direction == 'V':
                    base_col = initial_position[1:]
                    for i in range(1, 4):
                        new_position = chr(ord(initial_position[0]) + i) + base_col
                        all_positions.append(new_position)
                piece = Piece(code, all_positions, direction)
                pieces.append(piece)
                     
    return pieces

player1_pieces = process_pieces(jogador1_input[0:])