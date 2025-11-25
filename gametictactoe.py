import math
import random

# Global constants
BOARD_SIZE = 3 # Ukuran papan 3x3
PLAYER_MARK = 'X'
AI_MARK = 'O'
EMPTY_CELL = ' '
WIN_LENGTH = 3 # Tiga dalam satu baris untuk menang

def create_board():
    """Membuat papan 3x3 kosong."""
    return [[EMPTY_CELL for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def print_board(board):
    """Mencetak papan ke konsol."""
    print("\n  " + " | ".join(str(i) for i in range(BOARD_SIZE)))
    print("  " + "---" * BOARD_SIZE)
    for i, row in enumerate(board):
        print(f"{i} " + " | ".join(row))
    print()

def is_valid_move(board, row, col):
    """Memeriksa apakah langkah valid (dalam batas dan sel kosong)."""
    if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and board[row][col] == EMPTY_CELL:
        return True
    return False

def check_win(board, mark):
    """Memeriksa apakah tanda tertentu telah menang (3 dalam satu baris)."""
    
    # Cek baris
    for row in board:
        if all(cell == mark for cell in row):
            return True

    # Cek kolom
    for col in range(BOARD_SIZE):
        if all(board[row][col] == mark for row in range(BOARD_SIZE)):
            return True

    # Cek diagonal utama (kiri atas ke kanan bawah)
    if all(board[i][i] == mark for i in range(BOARD_SIZE)):
        return True

    # Cek anti-diagonal (kanan atas ke kiri bawah)
    if all(board[i][BOARD_SIZE - 1 - i] == mark for i in range(BOARD_SIZE)):
        return True

    return False

def is_board_full(board):
    """Memeriksa apakah papan penuh (seri)."""
    return all(EMPTY_CELL not in row for row in board)

def get_available_moves(board):
    """Mengembalikan daftar (baris, kolom) untuk semua sel kosong."""
    moves = []
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            if board[r][c] == EMPTY_CELL:
                moves.append((r, c))
    return moves

# --- Implementasi AI Minimax (Modifikasi Kunci) ---

def evaluate(board):
    """
    Mengevaluasi status papan.
    +10 untuk kemenangan AI, -10 untuk kemenangan Pemain, 0 untuk seri/berlangsung.
    """
    if check_win(board, AI_MARK):
        return 10
    elif check_win(board, PLAYER_MARK):
        return -10
    return 0

def minimax(board, depth, is_maximizing):
    """
    Algoritma Minimax rekursif.
    """
    score = evaluate(board)

    # Kasus dasar: status terminal (menang/kalah/seri)
    if score != 0:
        # Sesuaikan skor dengan kedalaman untuk memprioritaskan kemenangan lebih cepat
        return score - depth if is_maximizing else score + depth 
    if is_board_full(board):
        return 0

    if is_maximizing:
        # Pemain maksimalisasi (AI)
        best_score = -math.inf
        for r, c in get_available_moves(board):
            board[r][c] = AI_MARK
            best_score = max(best_score, minimax(board, depth + 1, False))
            board[r][c] = EMPTY_CELL # Undo move
        return best_score
    else:
        # Pemain minimalisasi (Manusia)
        best_score = math.inf
        for r, c in get_available_moves(board):
            board[r][c] = PLAYER_MARK
            best_score = min(best_score, minimax(board, depth + 1, True))
            board[r][c] = EMPTY_CELL # Undo move
        return best_score

def find_best_move(board):
    """
    Mencari langkah optimal untuk AI menggunakan Minimax.
    """
    best_score = -math.inf
    best_move = None
    
    # Acak langkah untuk sedikit variasi di antara langkah yang sama baiknya
    moves = get_available_moves(board)
    random.shuffle(moves) 

    for r, c in moves:
        board[r][c] = AI_MARK
        # Panggil Minimax dengan is_maximizing=False karena giliran berikutnya adalah pemain
        score = minimax(board, 0, False)
        board[r][c] = EMPTY_CELL # Undo move

        if score > best_score:
            best_score = score
            best_move = (r, c)
            
    return best_move

# --- Loop Game Utama ---

def play_game():
    """Fungsi utama untuk menjalankan game."""
    board = create_board()
    current_player = PLAYER_MARK # Pemain mulai duluan

    print("=============================================")
    print("  Unbeatable Tic-Tac-Toe (3x3) with Minimax AI")
    print("=============================================")
    print(f"Anda adalah '{PLAYER_MARK}', AI adalah '{AI_MARK}'. Yang pertama mendapatkan 3 dalam satu baris menang.")

    while True:
        print_board(board)

        if current_player == PLAYER_MARK:
            # Giliran Pemain
            while True:
                try:
                    move_input = input("Giliran Anda. Masukkan langkah (baris kolom, cth: 1 1): ")
                    row, col = map(int, move_input.split())
                    
                    if is_valid_move(board, row, col):
                        board[row][col] = PLAYER_MARK
                        break
                    else:
                        print("Langkah tidak valid. Coba lagi.")
                except ValueError:
                    print("Input tidak valid. Harap masukkan dua angka (baris dan kolom) dipisahkan oleh spasi.")
                except IndexError:
                    print("Input tidak valid. Harap masukkan dua angka (baris dan kolom) dipisahkan oleh spasi.")
            
            if check_win(board, PLAYER_MARK):
                print_board(board)
                print("Selamat! Anda menang!")
                break
            
            current_player = AI_MARK

        else:
            # Giliran AI
            print("AI sedang berpikir...")
            move = find_best_move(board)
            
            if move:
                row, col = move
                board[row][col] = AI_MARK
                print(f"AI bermain di ({row}, {col})")
            
            if check_win(board, AI_MARK):
                print_board(board)
                print("AI menang! Coba lagi lain kali.")
                break
            
            current_player = PLAYER_MARK

        if is_board_full(board):
            print_board(board)
            print("Hasilnya Seri!")
            break

if __name__ == "__main__":
    play_game()
