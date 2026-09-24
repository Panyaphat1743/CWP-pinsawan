# ex00/main.py
from checkmate import checkmate
 
def main():
    """ลองกระดานหลายแบบ แล้วเรียก checkmate"""
    # 1. ตัวอย่างจากโจทย์ -> Success (Pawn กิน King)
    board = """\
R...
.K..
..P.
....\
"""
    checkmate(board)
 
    # 2. ตัวอย่างจากโจทย์ -> Fail (ไม่มีหมากศัตรู)
    board = """\
..
.K\
"""
    checkmate(board)
 
    # 3. Queen กินแนวทแยง -> Success
    board = """\
Q...
....
....
...K\
"""
    checkmate(board)
 
    # 4. Rook โดน Pawn บังทาง -> Fail
    board = """\
.....
.....
R.P.K
.....
.....\
"""
    checkmate(board)
 
    # 5. Pawn อยู่เหนือ King กินถอยหลังไม่ได้ -> Fail
    board = """\
P..
.K.
...\
"""
    checkmate(board)
 
    # 6. กระดานไม่เป็นจัตุรัส -> Error
    board = """\
...
.K.\
"""
    checkmate(board)
 
    # 7. King สองตัว -> Error
    board = """\
K..
...
..K\
"""
    checkmate(board)

    # 8. Bishop โจมตีแนวทแยง -> Success
    board = """\
B...
....
..K.
....\
"""
    checkmate(board)

    # 9. Queen โจมตีแนวทแยงแต่มีหมากอื่น (R) ขวางสายตา -> Fail
    board = """\
K..
.R.
..Q\
"""
    checkmate(board)

    # 10. ไม่มี King บนกระดานเลย -> Error
    board = """\
...
...
...\
"""
    checkmate(board)
 
if __name__ == "__main__":
    main()