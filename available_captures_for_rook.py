"""
 Available Captures for Rook:
 On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. 

"""

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
      # First of all go through the 2D Array and figured out where the rook is placed.
        rookieRow = -1
        rookieCol = -1
        
        for colIndex,row in enumerate(board):
            for rowIndex,square in enumerate(row):
                if square == "R":
                    rookieRow = rowIndex
                    rookieCol = colIndex
        """
        Now Run 4 parallel while loops in each direction from the where the rook is placed to check if the pawn exits. If it exits increment the countered counter and break the loop. Also if B exits break the while loops without any counter.
        """

        counter = 0
        index = rookieCol-1
        while index >= 0:
            if board[index][rookieRow] == "p":
                counter += 1
                break
            elif board[index][rookieRow] == "B":
                break
            index -= 1
            continue
            
        index = rookieCol+1
        while index < 8:
            if board[index][rookieRow] == "p":
                counter += 1
                break
            elif board[index][rookieRow] == "B":
                break
            index += 1
            continue
        
        index = rookieRow-1
        while index >= 0:
            if board[rookieCol][index] == "p":
                counter += 1
                break
            elif board[rookieCol][index] == "B":
                break
            index -= 1
            continue
            
        index = rookieRow+1
        while index < 8:
            if board[rookieCol][index] == "p":
                counter += 1
                break
            elif board[rookieCol][index] == "B":
                break
            index += 1
            continue 
        # So how many pawns it can get    
        return counter
        