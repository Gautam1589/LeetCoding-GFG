<h2><a href="https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/">1835. Find XOR Sum of All Pairs Bitwise AND</a></h2><h3>Hard</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">The <strong style="user-select: auto;">XOR sum</strong> of a list is the bitwise <code style="user-select: auto;">XOR</code> of all its elements. If the list only contains one element, then its <strong style="user-select: auto;">XOR sum</strong> will be equal to this element.</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">For example, the <strong style="user-select: auto;">XOR sum</strong> of <code style="user-select: auto;">[1,2,3,4]</code> is equal to <code style="user-select: auto;">1 XOR 2 XOR 3 XOR 4 = 4</code>, and the <strong style="user-select: auto;">XOR sum</strong> of <code style="user-select: auto;">[3]</code> is equal to <code style="user-select: auto;">3</code>.</li>
</ul>

<p style="user-select: auto;">You are given two <strong style="user-select: auto;">0-indexed</strong> arrays <code style="user-select: auto;">arr1</code> and <code style="user-select: auto;">arr2</code> that consist only of non-negative integers.</p>

<p style="user-select: auto;">Consider the list containing the result of <code style="user-select: auto;">arr1[i] AND arr2[j]</code> (bitwise <code style="user-select: auto;">AND</code>) for every <code style="user-select: auto;">(i, j)</code> pair where <code style="user-select: auto;">0 &lt;= i &lt; arr1.length</code> and <code style="user-select: auto;">0 &lt;= j &lt; arr2.length</code>.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the <strong style="user-select: auto;">XOR sum</strong> of the aforementioned list</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> arr1 = [1,2,3], arr2 = [6,5]
<strong style="user-select: auto;">Output:</strong> 0
<strong style="user-select: auto;">Explanation:</strong> The list = [1 AND 6, 1 AND 5, 2 AND 6, 2 AND 5, 3 AND 6, 3 AND 5] = [0,1,2,0,2,1].
The XOR sum = 0 XOR 1 XOR 2 XOR 0 XOR 2 XOR 1 = 0.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> arr1 = [12], arr2 = [4]
<strong style="user-select: auto;">Output:</strong> 4
<strong style="user-select: auto;">Explanation:</strong> The list = [12 AND 4] = [4]. The XOR sum = 4.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= arr1.length, arr2.length &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= arr1[i], arr2[j] &lt;= 10<sup style="user-select: auto;">9</sup></code></li>
</ul>
</div>