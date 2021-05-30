def ans1(rideDuration, songDurations):
    totalSongDurations = rideDuration - 30
    n = len(songDurations)
    for i in range(n):
        for j in range(n):
            if(i != j):
                ps = songDurations[i] + songDurations[j]
                if ps == totalSongDurations:
                    return [i,j]


def ans2(rideDuration, songDurations):
    totalSongDurations = rideDuration - 30
    n = len(songDurations)
    d={}
    m=0
    rs=0
    for i in range(n):
        if totalSongDurations-songDurations[i] in d:
            if(max(totalSongDurations-songDurations[i], songDurations[i]) > m):
                m= max(totalSongDurations-songDurations[i], songDurations[i])
                rs = [d[totalSongDurations-songDurations[i]], i]
        else:
            d[songDurations[i]] = i
    if m:
        return rs
    else:
        return -1

rideDuration = 90
songDurations = [25,30,1,35,59,30]
print(ans1(rideDuration, songDurations))
print(ans2(rideDuration, songDurations))