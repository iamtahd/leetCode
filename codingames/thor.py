import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.


# My Code:
def _map(coord, dir_):
    d = {"x": {1: "E", -1: "W", 0: ""}, "y": {1: "N", -1: "S", 0: ""}}
    return d[coord][dir_]


def sign(n):
    return math.copysign(1, n) if n != 0 else 0


def moveThor(light, thor):
    dX = light[0] - thor[0]
    dY = light[1] - thor[1]

    moves = []
    count = 0
    while dX != 0 and dY != 0:
        xDir = sign(dX)
        yDir = sign(dY)

        moves.append("".join((_map("y", yDir), _map("x", xDir))))
        dX -= xDir
        dY -= yDir

        count += 1
    return moves


# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())
    for move in moveThor([light_x, light_y], [initial_tx, initial_ty]):
        print(move)
