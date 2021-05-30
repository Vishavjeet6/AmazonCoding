def ans(allLocations, numRestaurants):
    allLocations.sort(key=lambda x: x[0]**2 + x[1]**2)
    return allLocations[:numRestaurants]


allLocations = [[1,2],[3,4],[1,-1]]
numRestaurants=2
print(ans(allLocations, numRestaurants))