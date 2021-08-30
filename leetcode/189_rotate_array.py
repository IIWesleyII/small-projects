def rotate(lst, k):
    # lst[:] = lst[-k % len(lst) :] + lst[: -k % len(lst)]  # to the right
    # print(lst)
    lst[:] = lst[k % len(lst) :] + lst[: k % len(lst)]  # to the left
    print(lst)


rotate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)
