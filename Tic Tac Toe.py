import random

def ChoosePlayer():
      print("Do you want to be X or O?")
      player = input()
      while player != 'x' and player != 'o' and player != 'X' and player !='O':
            print("Plase choose one or the following letters: X or O")
            player = input()

      return player

def FirstTurn():
      turn = random.randint(1,2)
      if turn == 1:
            turn = True
            print("You will go first")
      elif turn ==2:
            turn = False
            print("The computer will go first.")
      return turn


def CheckWon(tile):
      if tile[1] == tile[2]== tile[3] != ' ':
            game_over = True
      elif tile[4] == tile[5] == tile[6] != ' ':
            game_over = True
      elif tile[7] == tile[8] == tile[9] != ' ':
            game_over = True
      elif tile[1] == tile[4] == tile[7] != ' ':
            game_over = True
      elif tile[2] == tile[5] == tile[8] != ' ':
            game_over = True
      elif tile[3] == tile[6] == tile[9] != ' ':
            game_over = True
      elif tile[1] == tile[5] == tile[9] != ' ':
            game_over = True
      elif tile[3] == tile[5] == tile[7] != ' ':
            game_over = True
      else:
            game_over = False
      return game_over

def CheckStatus(tile, computer):
      if tile[1] == tile[2]== tile[3] == computer:
            status = 'computer'
      elif tile[4] == tile[5] == tile[6] == computer:
            status = 'computer'
      elif tile[7] == tile[8] == tile[9] == computer:
            status = 'computer'
      elif tile[1] == tile[4] == tile[7] == computer:
            status = 'computer'
      elif tile[2] == tile[5] == tile[8] == computer:
            status = 'computer'
      elif tile[3] == tile[6] == tile[9] == computer:
            status = 'computer'
      elif tile[1] == tile[5] == tile[9] == computer:
            status = 'computer'
      elif tile[3] == tile[5] == tile[7] == computer:
            status = 'computer'
      else:
            status = 'player'
      return status

      
def DisplayBoard(tile):
      print('    |    |')
      print('  ' + tile[1] + ' |  ' + tile[2] + ' |  ' + tile[3])
      print('    |    |')
      print('--------------')
      print('    |    |')
      print('  ' + tile[4] + ' |  ' + tile[5] + ' |  ' + tile[6])
      print('    |    |')
      print('--------------')
      print('    |    |')
      print('  ' + tile[7] + ' |  ' + tile[8] + ' |  ' + tile[9])
      print('    |    |')
      print()
      print()

def ComputerWinningMove(tile, computer):
      if tile[1] == ' ':
            if tile[2] == tile[3] == computer or tile[4] == tile[7] == computer or tile[5] == tile[9] == computer:
                  next_move = 1
                  return next_move
      if tile[2] == ' ':
            if tile[1] == tile[3] == computer or tile[5] == tile[8] == computer:
                  next_move = 2
                  return next_move
      if tile[3] == ' ':
            if tile[2] == tile[1] == computer or tile[6] == tile[9] == computer or tile[5] == tile[7] == computer:
                  next_move = 3
                  return next_move
      if tile[4] == ' ':
            if tile[5] == tile[6] == computer or tile[1] == tile[7] == computer:
                  next_move = 4
                  return next_move
      if tile[5] == ' ':
            if tile[2] == tile[8] == computer or tile[4] == tile[6] == computer or tile[1] == tile[9] == computer or tile[3] == tile[9] == computer:
                  next_move = 5
                  return next_move
      if tile[6] == ' ':
            if tile[9] == tile[3] == computer or tile[4] == tile[5] == computer:
                  next_move = 6
                  return next_move
      if tile[7] == ' ':
            if tile[1] == tile[4] == computer or tile[8] == tile[9] == computer or tile[5] == tile[3] == computer:
                  next_move = 7
                  return next_move
      if tile[8] == ' ':
            if tile[2] == tile[5] == computer or tile[9] == tile[7] == computer:
                  next_move = 8
                  return next_move
      if tile[9] == ' ':
            if tile[6] == tile[3] == computer or tile[8] == tile[7] == computer or tile[5] == tile[1] == computer:
                  next_move = 9
                  return next_move
      return 100
      
def ComputerBlockMove(tile, player):
      if tile[1] == ' ':
            if tile[2] == tile[3] == player or tile[4] == tile[7] == player or tile[5] == tile[9] == player:
                  next_move = 1
                  return next_move
      if tile[2] == ' ':
            if tile[1] == tile[3] == player or tile[5] == tile[8] == player:
                  next_move = 2
                  return next_move
      if tile[3] == ' ':
            if tile[2] == tile[1] == player or tile[6] == tile[9] == player or tile[5] == tile[7] == player:
                  next_move = 3
                  return next_move
      if tile[4] == ' ':
            if tile[5] == tile[6] == player or tile[1] == tile[7] == player:
                  next_move = 4
                  return next_move
      if tile[5] == ' ':
            if tile[2] == tile[8] == player or tile[4] == tile[6] == player or tile[1] == tile[9] == player or tile[3] == tile[9] == player:
                  next_move = 5
                  return next_move
      if tile[6] == ' ':
            if tile[9] == tile[3] == player or tile[4] == tile[5] == player:
                  next_move = 6
                  return next_move
      if tile[7] == ' ':
            if tile[1] == tile[4] == player or tile[8] == tile[9] == player or tile[5] == tile[3] == player:
                  next_move = 7
                  return next_move
      if tile[8] == ' ':
            if tile[2] == tile[5] == player or tile[9] == tile[7] == player:
                  next_move = 8
                  return next_move
      if tile[9] == ' ':
            if tile[6] == tile[3] == player or tile[8] == tile[7] == player or tile[5] == tile[1] == player:
                  next_move = 9
                  return next_move
      
      return 100

def ComputerCornerMove(tile):
      if tile[1] == ' ':
            next_move = 1
            return next_move
      elif tile[3] == ' ':
            next_move = 3
            return next_move
      elif tile[7] == ' ':
            next_move = 7
            return next_move
      elif tile[9] == ' ':
            next_move = 9
            return next_move
      return 100

def ComputerCentreMove(tile):
      if tile[5] == ' ':
            next_move = 5
            return next_move
      return 100

def ComputerSideMove(tile):
      if tile[2] == ' ':
            next_move = 2
            return next_move
      elif tile[4] == ' ':
            next_move = 4
            return next_move
      elif tile[6] == ' ':
            next_move = 6
            return next_move
      elif tile[8] == ' ':
            next_move = 8
            return next_move
      return 100

def CheckTie(tile):
      if ' ' not in tile:
            tie = True
      else:
            tie = False
      return tie
      
play_again = 'yes' 
while play_again == 'yes':
      print("Welcome to Tic Tac Toe!")
      print()
      print(''' This is our board:
    |    |    
  1 |  2 |  3 
    |    |    
--------------
    |    |
  4 |  5 |  6
    |    |
--------------
    |    |
  7 |  8 |  9
    |    |    ''')
      print()
      print("To select a tile, simply type in the number corresponding to it.")

      player = ChoosePlayer()
      player = player.upper()
      if player == 'X':
            computer = 'O'
      else:
            computer = 'X'

      tile = ['0',' ',' ',' ',' ',' ',' ',' ',' ',' ']

      turn = FirstTurn()
      game_over = False
                  
      while game_over == False:

            if turn == True:
                  print("What is your next move? (1-9)")
                  index = input()
                  while index not in '123456789':
                        print("Please enter a number between 1-9")
                        index = input()
                  index = int(index)

                  while tile[index] != ' ':
                        print("Please enter a free tile number: ")
                        index = input()

                  index = int(index)                        
                  tile[index] = player
                  DisplayBoard(tile)
                  game_over = CheckWon(tile)
                  tie = CheckTie(tile)
                  if tie == True:
                        game_over = True
                  if game_over == True:
                        break
                  turn = False
                  
            if turn == False:
                  next_move = 100
                  while next_move >10:
                        next_move = ComputerWinningMove(tile, computer)
                        if next_move < 10:
                               break
                        next_move = ComputerBlockMove(tile, player)
                        if next_move <10:
                              break
                        next_move = ComputerCornerMove(tile)
                        if next_move <10:
                              break
                        next_move = ComputerCentreMove(tile)
                        if next_move <10:
                              break
                        next_move = ComputerSideMove(tile)
                        if next_move <10:
                              break
                        
                  next_move = int(next_move)
                  tile[next_move] = computer
                  DisplayBoard(tile)
                  game_over = CheckWon(tile)
                  tie = CheckTie(tile)
                  if tie == True:
                        game_over = True
                  if game_over == True:
                        break
                  turn = True

      if game_over == True:
            if tie == True:
                  print("Draw.")
            status = CheckStatus(tile, computer)
            if status == 'computer':
                  print("The " + status, " has won. Better Luck next time!")
            if status == 'player':
                  print("Great job! You have won the game!")
                        
            print("Would you like to play again? (yes or no)")
            play_again = input()

            if play_again != 'yes':
                  print("Goodbye.")

                        
              
        
            
