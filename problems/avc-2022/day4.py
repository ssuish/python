def main():
    path = "D:\\dev\\ssuish-repo\\python\\problems\\avc-2022\\data\\day4.txt"
    
    count_pairs = 0
    pair1 = []
    pair2 = []
    
    with open(path, 'r') as file:
        for line in file:
            line = line.strip()
            p1, p2 = line.split(",")
            p1 = p1.split("-")
            p2 = p2.split("-")
            p1 = [int(p1[0]), int(p1[1])]
            p2 = [int(p2[0]), int(p2[1])]
            pair1.append(p1)
            pair2.append(p2)
    
    # Case 1
    for i in range(len(pair1)):
        s1 = set(range(pair1[i][0], pair1[i][1] + 2))
        s2 = set(range(pair2[i][0], pair2[i][1] + 2))
        
        if s1.issubset(s2) or s2.issubset(s1):  
            count_pairs += 1
    
    # Case 2
    for i in range(len(pair1)):
        if ((pair1[i][0] <= pair2[i][1] and pair1[i][1] >= pair2[i][0]) or 
            (pair2[i][0] <= pair1[i][1] and pair2[i][1] >= pair1[i][0])):
            count_overlaps += 1 
    
    print("Pairs that fully contain each other: ", count_pairs)
    print("Pairs that overlaps: ", count_overlaps) 

if __name__ == '__main__':
    main()