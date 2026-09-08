int singleNonDuplicate(int* arr, int n) {
    int l = 0, h = n - 1;

    while (l < h) {
        int m = l + (h - l) / 2;
        if (m % 2 == 1)
            m--;

        if (arr[m] == arr[m + 1]) {
            l = m + 2;
        }
        else {
            h = m;
        }
    }

    return arr[l];
}