
def read():
    line = input().split()
    rows,cols = int(line[0]), int(line[1])

    m = []
    for i in range(rows):
        line = input().split()
        row =list( map(int, line))
        m.append(row)
    return m

def main():
    print("Simple Matrix")
    m = read()
    print(m)

if __name__=="__main__":
    main()

