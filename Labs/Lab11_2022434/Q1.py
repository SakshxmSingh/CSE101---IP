import matplotlib.pyplot as mpt

y_coords = list(map(int,input().split()))
x_coords = [i+1 for i in range(len(y_coords))]
y_mean = float(sum(y_coords)/len(y_coords))

mpt.plot(x_coords,y_coords, color="blue")
mpt.axhline(y_mean, linestyle='--', color="red")
mpt.show()
