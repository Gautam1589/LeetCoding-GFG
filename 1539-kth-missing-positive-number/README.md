<h2><a href="https://leetcode.com/problems/kth-missing-positive-number/">1539. Kth Missing Positive Number</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an array <code style="user-select: auto;">arr</code> of positive integers sorted in a <strong style="user-select: auto;">strictly increasing order</strong>, and an integer <code style="user-select: auto;">k</code>.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the</em> <code style="user-select: auto;">k<sup style="user-select: auto;">th</sup></code> <em style="user-select: auto;"><strong style="user-select: auto;">positive</strong> integer that is <strong style="user-select: auto;">missing</strong> from this array.</em></p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong class="example" style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> arr = [2,3,4,7,11], k = 5
<strong style="user-select: auto;">Output:</strong> 9
<strong style="user-select: auto;">Explanation: </strong>The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5<sup style="user-select: auto;">th</sup>&nbsp;missing positive integer is 9.
</pre>

<p style="user-select: auto;"><strong class="example" style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> arr = [1,2,3,4], k = 2
<strong style="user-select: auto;">Output:</strong> 6
<strong style="user-select: auto;">Explanation: </strong>The missing positive integers are [5,6,7,...]. The 2<sup style="user-select: auto;">nd</sup> missing positive integer is 6.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= arr.length &lt;= 1000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= arr[i] &lt;= 1000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= k &lt;= 1000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">arr[i] &lt; arr[j]</code> for <code style="user-select: auto;">1 &lt;= i &lt; j &lt;= arr.length</code></li>
</ul>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Follow up:</strong></p>

<p style="user-select: auto;">Could you solve this problem in less than O(n) complexity?</p>
</div>