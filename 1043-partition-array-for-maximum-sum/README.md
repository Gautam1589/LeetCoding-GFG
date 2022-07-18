<h2><a href="https://leetcode.com/problems/partition-array-for-maximum-sum/">1043. Partition Array for Maximum Sum</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an integer array <code style="user-select: auto;">arr</code>, partition the array into (contiguous) subarrays of length <strong style="user-select: auto;">at most</strong> <code style="user-select: auto;">k</code>. After partitioning, each subarray has their values changed to become the maximum value of that subarray.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a <strong style="user-select: auto;">32-bit</strong> integer.</em></p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> arr = [1,15,7,9,2,5,10], k = 3
<strong style="user-select: auto;">Output:</strong> 84
<strong style="user-select: auto;">Explanation:</strong> arr becomes [15,15,15,9,10,10,10]
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
<strong style="user-select: auto;">Output:</strong> 83
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> arr = [1], k = 1
<strong style="user-select: auto;">Output:</strong> 1
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= arr.length &lt;= 500</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= arr[i] &lt;= 10<sup style="user-select: auto;">9</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= k &lt;= arr.length</code></li>
</ul>
</div>