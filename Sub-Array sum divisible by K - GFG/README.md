# Sub-Array sum divisible by K
## Easy 
<div class="problem-statement" style="user-select: auto;">
                <p style="user-select: auto;"></p><p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">You are given an array <strong style="user-select: auto;">A</strong> of <strong style="user-select: auto;">N</strong> positive and/or negative integers and a value <strong style="user-select: auto;">K</strong>. The task is to find the count of all sub-arrays whose sum is divisible by K.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></span></p>

<pre style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input: </strong>N = 6, K = 5
       arr[] = {4, 5, 0, -2, -3, 1}
<strong style="user-select: auto;">Output:</strong> 7
<strong style="user-select: auto;">Explanation</strong>: There are 7 sub-arrays whose 
is divisible by K {4, 5, 0, -2, -3, 1}, {5}, 
{5, 0}, {5, 0, -2, -3}, {0}, {0, -2, -3} 
and {-2, -3}
</span></pre>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></span></p>

<pre style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input: </strong>N = 6, K = 2
       arr[] = {2, 2, 2, 2, 2, 2}
<strong style="user-select: auto;">Output:</strong> 21
<strong style="user-select: auto;">Explanation</strong>: All subarray sums are 
divisible by 7
</span>
</pre>

<p style="user-select: auto;">&nbsp;</p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Your Task:</strong><br style="user-select: auto;">
This is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function <strong style="user-select: auto;">subCount</strong>() that takes array<strong style="user-select: auto;"> arr</strong>, integer<strong style="user-select: auto;"> N, </strong>and<strong style="user-select: auto;"> </strong>integer<strong style="user-select: auto;"> K&nbsp;</strong>as parameters and returns the desired output.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Expected Time Complexity:</strong> O(N+K).<br style="user-select: auto;">
<strong style="user-select: auto;">Expected Auxiliary Space:</strong> O(K).</span></p>

<p style="user-select: auto;">&nbsp;</p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Constraints:</strong><br style="user-select: auto;">
2 ≤ N ≤ 10<sup style="user-select: auto;">5</sup></span></p>

<p style="user-select: auto;">&nbsp;</p>
 <p style="user-select: auto;"></p>
            </div>