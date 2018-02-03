# triplets summing to zero
#function trio is used to find the triplets
def trio(arr, n):
    check = False
    # initially we sort the given set of array elemets
    arr.sort()
    #the main logic behind the triplets extraction
    for i in range(0, n - 1):

        # initialize left and right
        lt = i + 1
        rt = n - 1
        t = arr[i]
        while (lt < rt):

            if (t + arr[lt] + arr[rt] == 0):
                # print numbers if it's summation is zero
                print(t, arr[lt], arr[rt])
                lt += 1
                rt -= 1
                check = True


            # If summation of 3 numbers is less than 0 increase in left
            elif (t + arr[lt] + arr[rt] < 0):
                lt += 1

            # if summation is more than 0 decrease in right
            else:
                rt -= 1

    if (check == False):
        print(" there is no Triplet in given array")


arr = [0, -10, -2, 3, 1, 5, 7, 8]
n = len(arr)
trio(arr, n)