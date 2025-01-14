def carFleet(target: int, position: list, speed: list) -> int:
    carfleet = list()
    # zipping car position and reach time to target
    for pos, sp in zip(position, speed):
        reach = (target - pos) / sp
        carfleet.append((pos, reach))
    carfleet.sort(reverse=True)

    carstack = list()
    # iterating through fleet list
    for car in carfleet:
        if len(carstack) == 0:
            carstack.append(car)
        elif car[1] <= carstack[len(carstack) - 1][1]:
            # skip if curr car reach time less than or equal to reach time of car at stack top
            # because they'll end up being a fleet
            pass
        else:
            # if curr car reach time greater than car at stack top, then push
            carstack.append(car)
    # return the len of car stack 
    return len(carstack)


target = 10
position = [4,1,0,7]
speed = [2,2,1,1]


res = carFleet(target, position, speed)

print(res)
