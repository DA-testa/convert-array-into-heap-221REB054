# python3
def swapping(data, i, n):
    swaps=[]
    st = i 
    leftChild = 2 * i + 1
    rightChild = 2 * i + 2


    if leftChild <= n-1 and data[leftChild] < data[st]:
        st = leftChild

    if rightChild <= n-1 and data[rightChild] < data[st]:
        st = rightChild
    
    if i != st:
        data[i], data[st] = data[st], data[i]
        swaps.append((i, st))
        swaps += swapping(data, st, n)


    return swaps

def build_heap(data):
    swaps = []
    n = len(data)
    
    for i in range(n // 2, -1, -1):
        swaps += swapping(data, i, n)

    return swaps


def main():
    # add another input for I or F 
    test = input("F or I : ")

    # input from keyboard
    if "I" in test:
        n = int(input())
        data = list(map(int, input().split()))

    # input from a file
    if "F" in test:
        fails = "test/" + input("File: ")
        with open(fails, "r") as file:
            n = int(file.readline())
            data = (list(map(int, file.readline().split())))


    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))

    # output all swaps
    print(len(swaps))

    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
