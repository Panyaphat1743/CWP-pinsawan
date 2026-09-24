from checkmate import checkmate

def main():
    # Example 1: P โจมตี K ได้ (Success)
    board1 = """\
R...
.K..
..P.
....\
"""
    checkmate(board1)

    print("-" * 10)

    # Example 2: K รอดพ้น (Fail)
    board2 = """\
..
.K\
"""
    checkmate(board2)

if __name__ == "__main__":
    main()