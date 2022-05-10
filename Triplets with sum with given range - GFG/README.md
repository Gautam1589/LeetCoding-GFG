# Triplets with sum with given range
## Medium 
<div class="problem-statement" style="user-select: auto;">
                <p style="user-select: auto;"></p><p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Given an array <strong style="user-select: auto;">Arr[]&nbsp;</strong>of <strong style="user-select: auto;">N</strong> distinct integers and a range from <strong style="user-select: auto;">L</strong>&nbsp;to <strong style="user-select: auto;">R</strong>, the task is to count the number of triplets having a sum in the range [L, R].</span></p>

<p style="user-select: auto;"><br style="user-select: auto;">
<span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></span></p>

<pre style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:</strong>
N = 4
Arr = {8 , 3, 5, 2}
L = 7, R = 11
<strong style="user-select: auto;">Output:</strong> 1
<strong style="user-select: auto;">Explaination:</strong> There is only one triplet {2, 3, 5}
having sum 10 in range [7, 11].</span></pre>

<p style="user-select: auto;"><br style="user-select: auto;">
<span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></span></p>

<pre style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:</strong>
N = 5
Arr = {5, 1, 4, 3, 2}
L = 2, R = 7
<strong style="user-select: auto;">Output:</strong> 2
<strong style="user-select: auto;">Explaination:</strong> There two triplets having 
sum in range [2, 7] are {1,4,2} and {1,3,2}.</span></pre>

<p style="user-select: auto;"><br style="user-select: auto;">
<span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Your Task:</strong><br style="user-select: auto;">
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong style="user-select: auto;">countTriplets()</strong>&nbsp;which takes the array <strong style="user-select: auto;">Arr[]</strong> and its size <strong style="user-select: auto;">N </strong>and <strong style="user-select: auto;">L</strong> and <strong style="user-select: auto;">R&nbsp;</strong>as input parameters&nbsp;and returns the count.</span></p>

<p style="user-select: auto;"><br style="user-select: auto;">
<span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Expected Time Complexity:</strong> O(N<sup style="user-select: auto;">2</sup>)<br style="user-select: auto;">
<strong style="user-select: auto;">Expected Auxiliary Space:</strong> O(1)</span></p>

<p style="user-select: auto;"><br style="user-select: auto;">
<span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Constraints:</strong><br style="user-select: auto;">
1 ≤ N ≤ 10<sup style="user-select: auto;">3</sup><br style="user-select: auto;">
1 ≤ Arr[i]&nbsp;≤ 10<sup style="user-select: auto;">3</sup><br style="user-select: auto;">
1 ≤ L&nbsp;≤ R ≤ 10<sup style="user-select: auto;">9</sup></span></p>
 <p style="user-select: auto;"></p>
            </div>