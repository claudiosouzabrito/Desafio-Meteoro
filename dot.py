class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.duplaX = -1
        self.duplaY = -1

def plotLineLow(data2, x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy
    
    D = (2 * dy) - dx
    y = y0

    for x in range(x0, x1+1):
        data2[x][y][0] = 0.0
        data2[x][y][1] = 1.0
        data2[x][y][2] = 0.0
        if D > 0:
            y = y + yi
            D = D + (2 * (dy - dx))
        else:
            D = D + 2*dy

def plotLineHigh(data2, x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx
    
    D = (2 * dx) - dy
    x = x0

    for y in range(y0, y1+1):
        data2[x][y][0] = 0.0
        data2[x][y][1] = 1.0
        data2[x][y][2] = 0.0
        
        if D > 0:
            x = x + xi
            D = D + (2 * (dx - dy))
        else:
            D = D + 2*dx


def plotLine(data2, x0, y0, x1, y1):
    if abs(y1 - y0) < abs(x1 - x0):
        if x0 > x1:
            plotLineLow(data2, x1, y1, x0, y0)
        else:
            plotLineLow(data2, x0, y0, x1, y1)
        
    else:
        if y0 > y1:
            plotLineHigh(data2, x1, y1, x0, y0)
        else:
            plotLineHigh(data2, x0, y0, x1, y1)
       