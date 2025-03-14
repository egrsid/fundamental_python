'''

У вас есть карта лабиринта в виде матрицы размером N⋅M, где каждая ячейка
может быть свободной (обозначается как '.') или стеной (обозначается как '#').
В одной из свободных ячеек находится сокровище (обозначено как 'S'), а в
другой - вход в лабиринт (обозначен как 'E'). Ваша задача - написать
программу, которая найдёт кратчайший путь от входа до сокровища,
перемещаясь только по свободным ячейкам. Путь можно проложить вверх,
вниз, влево или вправо, но нельзя двигаться по диагонали.

Формат ввода
Первая строка ввода содержит два целых числа N и M (1≤N,M≤100),
разделенных пробелом, обозначающих размеры лабиринта.
Последующие N строк содержат по M символов, описывающих лабиринт.

Формат вывода
Программа должна вывести одно целое число - количество шагов в
кратчайшем пути от входа до сокровища. Если путь найти невозможно,
программа должна вывести -1.

'''

n, m = map(int, input().split())
s_col, s_raw, e_col, e_raw = 0, 0, 0, 0


def is_valid_cell(col, raw, visited):
    if 0 <= col < n and 0 <= raw < m:
        if mtx[col][raw] != '#' and not visited[col][raw]: return True
    return False


def bfs(start, end):
    cur_y, cur_x = start
    end_y, end_x = end

    visited = [[False]*m for _ in range(n)]
    q = [(cur_y, cur_x, 0)]
    visited[cur_y][cur_x] = True

    while q:
        cur_y, cur_x, dist = q.pop(0)

        if cur_y == end_y and cur_x == end_x: return dist

        if is_valid_cell(cur_y+1, cur_x, visited):
            q.append((cur_y+1, cur_x, dist+1))
            visited[cur_y+1][cur_x] = True
        if is_valid_cell(cur_y, cur_x+1, visited):
            q.append((cur_y, cur_x+1, dist+1))
            visited[cur_y][cur_x+1] = True
        if is_valid_cell(cur_y-1, cur_x, visited):
            q.append((cur_y-1, cur_x, dist+1))
            visited[cur_y - 1][cur_x] = True
        if is_valid_cell(cur_y, cur_x-1, visited):
            q.append((cur_y, cur_x-1, dist+1))
            visited[cur_y][cur_x - 1] = True

    return -1


mtx = []
for i in range(n):
    a = input()
    mtx.append(list(a))
    if 'S' in a: s_col, s_raw = i, a.find("S")
    if 'E' in a: e_col, e_raw = i, a.find("E")

print(mtx)

r = bfs((s_col, s_raw), (e_col, e_raw))
print(r)