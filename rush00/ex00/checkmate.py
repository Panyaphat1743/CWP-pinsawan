# ex00/checkmate.py 
 
PIECES = "PBRQ"  # ตัวอักษรอื่นทั้งหมดถือว่าเป็นช่องว่าง
 
# แต่ละทิศที่มองออกจาก King: (แถว, คอลัมน์, หมากที่กิน King ได้จากทิศนั้น)
DIRECTIONS = [
    (-1, 0, "RQ"), (1, 0, "RQ"), (0, -1, "RQ"), (0, 1, "RQ"),  # ตรง
    (-1, -1, "BQ"), (-1, 1, "BQ"),                              # ทแยงบน
    (1, -1, "BQP"), (1, 1, "BQP"),                              # ทแยงล่าง (Pawn กินขึ้นบน เลยอยู่ใต้ King)
]
 
 
def checkmate(board):
    """print Success ถ้า King โดนรุก, Fail ถ้าปลอดภัย, Error ถ้ากระดานผิด"""
    rows = board.splitlines() if isinstance(board, str) else []
    size = len(rows)
 
    # กระดานต้องไม่ว่าง และต้องเป็นสี่เหลี่ยมจัตุรัส
    if size == 0 or any(len(row) != size for row in rows):
        print("Error")
        return
 
    # ต้องมี King ตัวเดียว
    kings = [(r, c) for r in range(size) for c in range(size) if rows[r][c] == "K"]
    if len(kings) != 1:
        print("Error")
        return
    king_r, king_c = kings[0]
 
    # เดินออกจาก King ทีละช่องในแต่ละทิศ จนเจอหมากตัวแรกหรือหลุดกระดาน
    for dr, dc, attackers in DIRECTIONS:
        r, c = king_r + dr, king_c + dc
        steps = 1
        while 0 <= r < size and 0 <= c < size:
            piece = rows[r][c]
            if piece in PIECES:
                # Pawn กินได้แค่ช่องที่ติดกัน (steps == 1)
                if piece in attackers and (piece != "P" or steps == 1):
                    print("Success")
                    return
                break  # ไม่ใช่ตัวที่กินได้ = บังทางไว้ ทิศนี้ปลอดภัย
            r += dr
            c += dc
            steps += 1
 
    print("Fail")
 