import requests
import json
import chess

def listen_for_opponent_move(game_id, headers, board):
    stream_url = f'https://lichess.org/api/board/game/stream/{game_id}'
    with requests.get(stream_url, headers=headers, stream=True) as response:
        for line in response.iter_lines():
            if line:
                decoded_line = json.loads(line.decode('utf-8'))
                if 'moves' in decoded_line and decoded_line['moves']:
                    moves = decoded_line['moves'].split()
                    last_move = moves[-1]
                    opponent_move = chess.Move.from_uci(last_move)
                    return board.san(opponent_move)  # Convert to standard notation
    return None

def display_legal_moves(board):
    legal_moves = [board.san(move) for move in board.legal_moves]
    print("Legal moves are:", ", ".join(legal_moves))

def resign_game(game_id, headers):
    resign_url = f'https://lichess.org/api/board/game/{game_id}/resign'
    response = requests.post(resign_url, headers=headers)
    return response.ok

def main():
    token = 'API_KEY_HERE'
    headers = {'Authorization': f'Bearer {token}'}

    difficulty = int(input("Enter Stockfish difficulty level (1-8): "))
    user_color = 'white' if input("Do you want to play as white or black? ").lower() == 'white' else 'black'
    payload = {'level': difficulty, 'color': user_color}

    response = requests.post('https://lichess.org/api/challenge/ai', headers=headers, data=payload)
    game_id = response.json()['id']

    board = chess.Board()
    print("You are playing as", user_color)
    print("Type your move in standard notation (e.g., e4, Nf3), 'show' to display the board, or 'resign' to resign the game.")

    while not board.is_game_over():
        try:
            move_san = input("Your move: ")
            if move_san.lower() == 'show':
                print(board)
                continue
            elif move_san.lower() == 'resign':
                if resign_game(game_id, headers):
                    print("You have resigned the game.")
                    break
                else:
                    print("Error: Unable to resign. Please try again or make a move.")
                    continue

            if move_san not in [board.san(m) for m in board.legal_moves]:
                print("Invalid move. Legal moves are:")
                display_legal_moves(board)
                continue

            move = board.parse_san(move_san)
            board.push(move)

            uci_move = board.uci(move)
            move_url = f'https://lichess.org/api/board/game/{game_id}/move/{uci_move}'
            requests.post(move_url, headers=headers)

            stockfish_move_san = listen_for_opponent_move(game_id, headers, board)
            if stockfish_move_san:
                print("Stockfish's move:", stockfish_move_san)
                board.push_san(stockfish_move_san)

        except ValueError as e:
            print(f"Invalid move: {e}. Please try again.")
            display_legal_moves(board)

    print("Game over")

if __name__ == "__main__":
    main()
