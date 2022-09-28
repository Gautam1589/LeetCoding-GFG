class Solution {
    public int mySqrt(int x) {
        int i=1,j=x;
        if(x==0) return x;
        int mid=1;
        while(i<j){
            mid = i+(j-i)/2;
            if((mid==x/mid) || (i+1==j)) break;
            if(mid < x/mid) i=mid;
            else j=mid;
        }
        return mid;
    }
}