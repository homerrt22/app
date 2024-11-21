BOX = []
def main():
    for i in range(1,100):
        BOX.append(i)
        return BOX


def boubleSour(BOX = []):
    tmp = 0
    for j in BOX:
        for t in BOX + 1:
            tmp = BOX[t]
            if BOX[j] > BOX[t + 1]:
                BOX[t + 1], BOX[t]
    print(BOX)
    
main(boubleSour(BOX))