from typing import List
def reorder_log_files(logs: List[str]) -> List[str]:
    # WRITE YOUR BRILLIANT CODE HERE
    alphas = []
    nums = []
    for log in logs:
        ident, cont = log.split(' ', 1)
        (alphas if cont[0].isalpha() else nums).append((cont, ident))
    alphas.sort()
    return [f'{i} {c}' for c, i in alphas + nums]
if __name__ == '__main__':
    # logs = [input() for _ in range(int(input()))]
    logs = ["id1 233 232 232", "12d amazon kindle", "13d amazon kindle", "id2 54352 23", "id6 amazon book"]
    res = reorder_log_files(logs)
    for line in res:
        print(line)
