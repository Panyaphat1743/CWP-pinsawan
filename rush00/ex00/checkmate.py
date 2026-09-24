def checkmate(board):
    # ตรวจสอบว่ามีข้อมูลส่งมาหรือไม่
    if not board:
        return
        
    # แยกกระดานออกเป็นแถวๆ ตัดช่องว่างและบรรทัดว่างออก
    rows = board.strip().split('\n')
    size = len(rows)
    
    # หากไม่มีแถวเลยให้ออกจากฟังก์ชัน
    if size == 0:
        return

    # ตรวจสอบว่ากระดานเป็นสี่เหลี่ยมจัตุรัสหรือไม่
    for row in rows:
        if len(row) != size:
            return # หรือจะ print("Error") ก็ได้ตามโจทย์กำหนด
            
    # หาตำแหน่งของ King
    king_pos = None
    king_count = 0
    for r in range(size):
        for c in range(size):
            if rows[r][c] == 'K':
                king_pos = (r, c)
                king_count += 1
                
    # ต้องมี King แค่ 1 ตัวเท่านั้น
    if king_count != 1:
        return

    kr, kc = king_pos
    
    # กำหนดทิศทาง (delta_row, delta_col) และศัตรูที่อันตรายในทิศทางนั้น
    # r- คือขึ้นบน, r+ คือลงล่าง, c- คือซ้าย, c+ คือขวา
    directions = [
        # ทิศตั้งและนอน (Rook, Queen)
        (-1, 0, ['R', 'Q']), # บน
        (1, 0, ['R', 'Q']),  # ล่าง
        (0, -1, ['R', 'Q']), # ซ้าย
        (0, 1, ['R', 'Q']),  # ขวา
        
        # ทิศทแยงมุม (Bishop, Queen) และ Pawn (เฉพาะระยะ 1 ช่อง)
        (-1, -1, ['B', 'Q']), # ทแยงบนซ้าย
        (-1, 1, ['B', 'Q']),  # ทแยงบนขวา
        (1, -1, ['B', 'Q', 'P']), # ทแยงล่างซ้าย (Pawn ศัตรูอยู่ด้านล่าง โจมตีขึ้นมาหา King ได้)
        (1, 1, ['B', 'Q', 'P'])   # ทแยงล่างขวา (Pawn ศัตรูอยู่ด้านล่าง โจมตีขึ้นมาหา King ได้)
    ]

    # ยิงสายตาเช็กจาก King ไปยังทิศทางต่างๆ
    for dr, dc, attackers in directions:
        r, c = kr + dr, kc + dc
        distance = 1
        
        while 0 <= r < size and 0 <= c < size:
            piece = rows[r][c]
            
            # ถ้าไม่ใช่ช่องว่าง แปลว่าเจอหมากขวาง
            if piece != '.' and piece != ' ': 
                # เช็กว่าเป็นหมากที่โจมตีในทิศนี้ได้หรือไม่
                if piece in attackers:
                    # กฎพิเศษสำหรับ Pawn: โจมตีได้ระยะแค่ 1 ช่องเท่านั้น
                    if piece == 'P':
                        if distance == 1 and dr == 1:
                            print("Success")
                            return
                    else:
                        print("Success")
                        return
                # ถ้าเจอหมากแต่โจมตีไม่ได้ รัศมีนี้ถือว่าโดนบล็อก ให้หยุดเช็กทิศนี้
                break 
                
            # เลื่อนช่องตรวจสอบไปตามทิศทางเดิม
            r += dr
            c += dc
            distance += 1

    # ถ้ารอดทุกทิศทาง
    print("Fail")