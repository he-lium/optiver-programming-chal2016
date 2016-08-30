import sys
stars = dict()

for line in sys.stdin:
    star_count = 0
    args = line.strip('\n').split()
    if args[0] == 'Star':
        if star_count == 0:
            start_star = args[1]
        elif star_count == 1:
            dest_star = args[1]
        stars[args[1]] = [int(args[2])]
        star_count += 1
    elif args[0] == 'Flight':
        star1, star2 = args[1], args[2]
        stars[star1].append((star2, int(args[3]), int(args[4])))
        stars[star2].append((star1, int(args[3]), int(args[4])))

def search():
    queue = [(0, stars[start_star][0], start_star)]
    while len(queue) > 0:
        current = queue.pop(0)
        fuel_curr = current[1]
        star_curr = current[2]
        if len(stars[star_curr]) > 1:
            for next_star in stars[star_curr][1:]:
                # print(next_star)
                if fuel_curr - next_star[2] >= 0:
                    if next_star[0] == dest_star: # TODO next_star == dest
                        print("Reachable: Yes")
                        print("Distance:",current[0]+next_star[1])
                        print("Fuel burnt:",fuel_curr-next_star[2])
                        return
                    queue.append([current[0] + next_star[1], fuel_curr - next_star[2] + stars[next_star[0]][0]])
                    print(queue)
print(stars)
search()
# print(queue)
