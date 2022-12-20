

def Main():
    path = "D:\\dev\\ssuish-repo\\python\\problems\\avc-2022\\data\\day2.txt"
    
    game = {'X':1, 'Y':2, 'Z':3}
    opponent = {'X':'A', 'Y':'B', 'Z':'C'}
    # X = A = Rock
    # Y = B = Paper
    # Z = C = Scissors
    score = 0
      
    with open(path, 'r') as file:
        for line in file:
            pick = line.strip()
            if pick[0] == opponent.get(pick[2]):
                score += game.get(pick[2]) + 3
            else:
                if pick[0] == 'A' and pick[2] == 'Y':
                    score += game.get(pick[2]) + 6
                elif pick[0] == 'A' and pick[2] == 'Z':
                    score += game.get(pick[2]) + 0
                elif pick[0] == 'B' and pick[2] == 'X':
                    score += game.get(pick[2]) + 0
                elif pick[0] == 'B' and pick[2] == 'Z':
                    score += game.get(pick[2]) + 6
                elif pick[0] == 'C' and pick[2] == 'X':
                    score += game.get(pick[2]) + 6
                elif pick[0] == 'C' and pick[2] == 'Y':
                    score += game.get(pick[2]) + 0
    
    print("Total score: ", score) 

if __name__ == '__main__':
    Main()