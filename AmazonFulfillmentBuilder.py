def ans(parts):
    if len(parts)==1:
        return 0
    parts.sort()
    Sum = [sum(parts[:2])]
    for i in range(len(parts)-1):
        parts.remove(parts[0])
        parts[0] = Sum[i]
        if len(parts) == 2:
            Sum.append(sum(parts))
            break
        else:
            Sum.append(Sum[i] + parts[1])
    return sum(Sum)


parts=[8,4,6,12]
print(ans(parts))