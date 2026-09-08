int singleNonDuplicate(int* arr, int n) {
    int l = 0, h = n - 1;

    while (l < h) {
        int m = l + (h - l) / 2;

        // make m even
        if (m % 2 == 1)
            m--;

        if (arr[m] == arr[m + 1]) {
            // pair is correct, single element is on right
            l = m + 2;
        }
        else {
            // pair is broken, single is at m or on left
            h = m;
        }
    }

    return arr[l];
}