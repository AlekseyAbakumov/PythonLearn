busStations = list(map(int, input().split()))
stations = set()
for i_b in range(len(busStations) // 2):
    route = set(range(min(busStations[2 * i_b: 2 * i_b + 2]),
                      max(busStations[2 * i_b: 2 * i_b + 2]) + 1))
    if not i_b:
        stations = route
    else:
        stations.intersection_update(route)
print(stations.__len__())
