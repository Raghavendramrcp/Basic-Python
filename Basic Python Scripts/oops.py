class CPR():

    def __init__(self, high,low, close):
        self.high = high
        self.low = low
        self.close = close

    def central_pivot(self):
        central_pivot = (float(self.high)+float(self.low)+float(self.close))/3
        print(central_pivot)
        return central_pivot
    def top_central_pivot(self):
        top_central_pivot = (float(self.high)+float(self.low))/2
        print(top_central_pivot)
        return abs(top_central_pivot)
    def bottom_central_pivot(self):
        pivot = (float(self.high)+float(self.low)+float(self.close))/3
        top_pivot = (float(self.high)+float(self.low))/2
        bottom_pivot = pivot+(pivot-top_pivot)
        print(bottom_pivot)
        return abs(bottom_pivot)

bn1 = CPR(41516,41051,41258)

print(bn1.central_pivot(),bn1.top_central_pivot(),bn1.bottom_central_pivot())