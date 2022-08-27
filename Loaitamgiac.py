
n=int(input())
a=[[] for i in range(n)]
for i in range(n):
    for j in range(8):
        x, y = map(int, input().split())
        a[i].append([x, y])

def attack(i: int, j: int, queenList: list):
    '''
    input: i, j lần lượt là quân hậu thứ i, thứ j
            queenList: list ví trị 8 quân hậu
    function: return True nếu 2 quân hậu không tấn công lẫn nhau - không tấn công theo đường chéo hay đường thẳng
    '''
    if (cross_attack(i, j, queenList) or line_attack(i, j, queenList)):
        return True
    else:
        return False


def cross_attack(i: int, j: int, queenList: list):
    """
    function: return True nếu 2 quân hậu i, j tấn công nhau theo đường chéo
    """
    x1, y1 = queenList[i]
    x2, y2 = queenList[j]
    if (x1 + y1 == x2 + y2 or abs(y2 - y1) == abs(x2 - x1)):
        return True
    return False


def line_attack(i: int, j: int, queenList: list):
    x1, y1 = queenList[i]
    x2, y2 = queenList[j]
    if (x1 - x2 == 0 or y1 - y2 == 0):
        return True
    return False


# duyệt từng cặp quân hậu, nếu không có bất kì cặp hậu tấn công nhau -> print YES, có 1 cặp tấn công nhau -> print NO + break
#flag = True

for i in range(n):
    check=False
    for m in range(7):
        for j in range(m+1,8):
             if attack(m,j,a[i]):
                check=True
                break
    if check:
        print('YES')
    else:
        print('NO')



