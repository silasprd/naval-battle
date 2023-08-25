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
        if(code == '3'):
            for piece in positions_and_direction:
                position = piece.split("|")
        else:
            for p in positions_and_direction:
                position_and_direction = p.split("|")
                for piece in position_and_direction:
                    position = piece[:-1]
                    direction = piece[-1:]
                    print(direction)
            
            
    return pieces

player1_pieces = process_pieces(jogador1_input[0:])
