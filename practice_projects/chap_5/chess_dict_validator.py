def isValidChessBoard(valid_board):
    # Checkpoint 1: Valid place on board or not
    valid_spaces=['1a','1b','1c','1d','1e','1f','1g','1h','2a','2b','2c','2d','2e','2f','2g','2h',
        '3a','3b','3c','3d','3e','3f','3g','3h','4a','4b','4c','4d','4e','4f','4g','4h',
        '5a','5b','5c','5d','5e','5f','5g','5h','6a','6b','6c','6d','6e','6f','6g','6h',
        '7a','7b','7c','7d','7e','7f','7g','7h','8a','8b','8c','8d','8e','8f','8g','8h']
    global r
    spaces=[]
    for i in valid_board.keys():
        spaces.append(i)
    valid = dict(valid_spaces)
    given = dict(spaces)
    w=0
    b=0
    bking=0
    wking=0
    wpawn=0
    bpawn=0
    pieces=('pawn','rook','bishop','queen','king','knight')
    if given!=valid:
        print("Invalid Chess Board: Incorrect space")
        r=0
    if given==valid:
        for i in valid_board.values():
            if i!=(''):
        # Checkpoint 2: Exactly 1 black and white king or not
                 if i=='bking':
                      bking+=1
                 if i=='wking':
                      wking+=1
                 if bking>1:
                      print("Invalid Chess Board: More than one black king")
                      r=0
                      break
                 if wking>1:
                      print("Invalid Chess Board: More than one white king")  
                      r=0
                      break
         
        # Checkpoint 3: No of total black and white chess pieces
                 if i[0]=='w':
                       w+=1
                 if i[0]=='b':
                       b+=1
                 if w>16:
                       print("Invalid Chess Board: More than 16  white pieces")
                       r=0
                       break
                 if b>16:
                       print("Invalid Chess Board: More than 16  black pieces")
                       r=0
                       break

        # Checkpoint 4: No of pawns of each colour should not exceed 8
                 if i=='wpawn':
                       wpawn+=1
                 if i=='bpawn':
                       bpawn+=1
                 if wpawn>8:
                       print("Invalid Chess Board: More than 8 white pawns")
                       r=0
                       break
                 if bpawn>8:
                       print("Invalid Chess Board: More than 8 black pawns")
                       r=0
                       break
                  
        # Checkpoint 5: Colour of pieces
                 if i[0]!='w':
                     if i[0]!='b':
                       print("Invalid Chess Board: Only black or white colour pieces")
                       r=0
                       break

        #Checkpoint 6: Valid pieces
                 if i[1:] not in pieces:
                       print("Invalid Chess Board: Invalid piece type")
                       r=0
                       break


board = {'1a': 'bking','2a': 'bqueen','3a': 'brook','4a': 'brook',
'5a': 'bknight','6a': 'bknight','7a':'bbishop','8a': 'bbishop',
'1b': 'bpawn','2b': 'bpawn','3b': 'bpawn','4b':'bpawn',
'5b': 'bpawn','6b': 'bpawn','7b': 'bpawn','8b': 'bpawn',
'1c': 'wking','2c': 'wqueen','3c': 'wrook','4c': 'wrook',
'5c': 'wbishop','6c': 'wbishop','7c': 'wknight','8c':'wknight',
'1e': 'wpawn','2e': 'wpawn','3e': 'wpawn','4e': 'wpawn',
'5e': 'wpawn','6e': 'wpawn','7e': 'wpawn','8e': 'wpawn',
'1f': '','2f': '','3f': '','4f': '','5f': '','6f': '','7f': '','8f': '',
'1g': '','2g': '','3g': '','4g': '','5g': '','6g': '','7g': '','8g': '',
'1h': '','2h': '','3h': '','4h': '','5h': '','6h': '','7h': '','8h': '',}

r=1
isValidChessBoard(board)  
if r!=0:
      print("This chess board is valid")  










