

def Main():
    path = "D:\\dev\\ssuish-repo\\python\\problems\\avc-2022\\data\\day2.txt"
    
    value = {'X':1, 'Y':2, 'Z':3}
    draw = {'A':'X', 'B':'Y', 'C':'Z'}
    win = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    loss = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    
    # Opponent 'A X' You
    
    # Condition 1
    # X = A = Rock
    # Y = B = Paper
    # Z = C = Scissors
    
    # Condition 2
    # X = Win
    # Y = Draw
    # Z = Lose
    
    # Pseudocode
    """
        if opponent = A and you = Y
            Y is draw, so you = B
            score = 3 + 2
        else if = A and you = X
            X is win, so you = C
            score = 6 + 1
        else if = A and you = Z
            Z is lose, so you = A
            score = 0 + 3  
    """
    
    score = 0
      
    with open(path, 'r') as file:
    
        for line in file:
            pick = line.strip()
            if pick[2] == 'X':
                you = loss[pick[0]]
                score += value[you] + 0
            elif pick[2] == 'Y':
                you = draw[pick[0]]
                score += value[you] + 3
            elif pick[2] == 'Z':
                you = win[pick[0]]
                score += value[you] + 6
            
    print("Total score: ", score) 

if __name__ == '__main__':
    Main()