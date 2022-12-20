def Main():
    path = "D:\\dev\\ssuish-repo\\python\\problems\\avc-2022\\data\\day1.txt"
    elves_with_calories = []
    basket = 0
    
    with open(path, 'r') as file:
        for line in file: 
            calories = line.strip()
            if calories == "":
                elves_with_calories.append(basket)
                basket = 0
                continue
            else:
                basket += int(calories)
            
    print("Highest total calories garthered by the elf: ", max(elves_with_calories))
    n = 3 
    elves_with_calories.sort()
    total_highest3 = sum(elves_with_calories[-n:])
    print("Total of the highest 3 elves: ", total_highest3)

if __name__ == '__main__':
    Main()