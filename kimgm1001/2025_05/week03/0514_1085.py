def main():

    x, y, w, h = map(int, input().split())

    if x > w - x:
        dis_width = w - x
    else:
        dis_width = x

    if y > h - y:
        dis_height = h - y
    else:
        dis_height = y

    if dis_width > dis_height:
        result = dis_height
    else:
        result = dis_width

    return result

if __name__ == '__main__':
    print(main())