
square_side=10

def draw_squares():
    for i in range(4):
        # this won't work: 
        # square_side=square_side+10
        # but this will:
        print(square_side)

draw_squares()

