from collections import defaultdict
import re


graph = defaultdict(list)
with open("data7.txt") as f:
    for line in f.readlines():
        regex = re.match('(.+?) bags', line)
        color_primary = regex.group(1)
        color_inside = re.findall('(\d+) (.+?) bag', line)
        for num, val in color_inside:
            graph[color_primary].append((int(num), val))


def recur(color):
    if color not in graph.keys():
        return 1
    res = 1
    for n, c in graph[color]:
        res += recur(c)*n
    return res


print(recur("shiny gold")-1)
