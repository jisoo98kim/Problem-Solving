if __name__ == '__main__':
    # To collect the kth floor, nth unit from the input values
    test_case = int(input())

    for i in range(test_case):
        k = int(input())    # kth floor, 1 <= k
        n = int(input())    # nth unit, n <= 14

        # List Comprehension for the 0th floor
        ground = [j for j in range(1, n + 1)] # range func: n - 1, not n
        for x in range(k):
            for y in range(1, n):
                ground[y] = ground[y] + ground[y - 1]

        print(ground[-1]) # To print the value of last index
