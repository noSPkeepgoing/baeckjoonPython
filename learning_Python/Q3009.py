import collections

point_x = []
point_y = []

for i in range(3) :
    x, y = map(int, input().split())
    point_x.append(x)
    point_y.append(y)

count_x = collections.Counter(point_x)
count_y = collections.Counter(point_y)
print(count_x.most_common(2)[1][0], count_y.most_common(2)[1][0])