import random
import pygame

# define constants for the puzzle dimensions
PUZZLE_WIDTH = 200
PUZZLE_HEIGHT = 100

# define a list of math problems at different difficulty levels
problems = [
    {"problem": "2 + 2", "answer": 4, "difficulty": "easy"},
    {"problem": "5 - 3", "answer": 2, "difficulty": "easy"},
    {"problem": "6 * 7", "answer": 42, "difficulty": "medium"},
    {"problem": "8 / 4", "answer": 2, "difficulty": "easy"},
    {"problem": "9 - 2", "answer": 7, "difficulty": "easy"},
    {"problem": "10 * 10", "answer": 100, "difficulty": "hard"},
]

# define a dictionary of point values for each difficulty level
points = {
    "easy": 10,
    "medium": 20,
    "hard": 30,
}

# define a variable to keep track of the user's total points
total_points = 0

# define a variable to keep track of the user's level
level = 1

# define a variable to keep track of the number of pieces in the current puzzle
puzzle_pieces = 0

# define a function to generate a math puzzle
def generate_puzzle():
  # select a random problem from the list
  problem = random.choice(problems)
  # create a Pygame surface for the puzzle piece
  piece = pygame.Surface((PUZZLE_WIDTH, PUZZLE_HEIGHT))
  # draw the puzzle piece outline
  pygame.draw.rect(piece, (0, 0, 0), (0, 0, PUZZLE_WIDTH, PUZZLE_HEIGHT), 2)
  # render the math problem text
  pygame.font.init()
  font = pygame.font.Font(None, 36)
  text = font.render(problem["problem"], True, (0, 0, 255))
  # center the text on the puzzle piece
  text_rect = text.get_rect(center=(PUZZLE_WIDTH // 2, PUZZLE_HEIGHT // 2))
  piece.blit(text, text_rect)
  # display the puzzle piece to the user
  pygame.display.set_caption("Solve the math problem to unlock a puzzle piece")
  pygame.display.set_mode((PUZZLE_WIDTH, PUZZLE_HEIGHT))
  pygame.display.set_mode((PUZZLE_WIDTH, PUZZLE_HEIGHT))
  pygame.display.set_caption("Math Puzzle")
  screen = pygame.display.set_mode((PUZZLE_WIDTH, PUZZLE_HEIGHT))
  screen.blit(piece, (0, 0))
  pygame.display.flip()
  # get the user's answer
  answer = int(input("Enter your answer: "))
  # check if the user's answer is correct
  if answer == problem["answer"]:
    # if the answer is correct
      # if the answer is correct, award points, increase the user's level, and add a piece to the puzzle
    print("Correct!")
    global total_points
    total_points += points[problem["difficulty"]]
    global level
    level += 1
    global puzzle_pieces
    puzzle_pieces += 1
    # display the current puzzle status
    print("Puzzle status:")
    for i in range(puzzle_pieces):
      print(" _______ ")
      print("|       |")
      print("|       |")
      print("|_______|")
    # check if the puzzle is complete
    if puzzle_pieces == 5:
      # if the puzzle is complete, reset the puzzle counter and move on to the next level
      puzzle_pieces = 0
      print("Congratulations, you've completed the puzzle! Moving on to the next level.")
  else:
    # if the answer is incorrect, tell the user and try again
    print("Incorrect, try again.")
    generate_puzzle()

# generate and solve the first math puzzle
generate_puzzle()

# keep generating and solving puzzles until the user reaches the maximum level
while level <= 3:
  generate_puzzle()

# when the user has reached the maximum level, display their total points
print("Congratulations, you've reached the maximum level!")
print("You earned a total of", total_points, "points.")
