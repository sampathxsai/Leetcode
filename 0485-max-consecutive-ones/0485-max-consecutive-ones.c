int findMaxConsecutiveOnes(int* a, int numsSize) {
    int count = 0;
    int max = 0;
    for (int i = 0; i<numsSize ; i++){
        if(a[i] != 1){
            count =0 ;
            continue;
        }
        count++;
        if(count > max){
                max = count ;
            }
    }
    return max;
}