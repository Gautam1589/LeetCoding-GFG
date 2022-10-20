<h2><a href="https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/">1703. Minimum Adjacent Swaps for K Consecutive Ones</a></h2><h3>Hard</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">You are given an integer array, <code style="user-select: auto;">nums</code>, and an integer <code style="user-select: auto;">k</code>. <code style="user-select: auto;">nums</code> comprises of only <code style="user-select: auto;">0</code>'s and <code style="user-select: auto;">1</code>'s. In one move, you can choose two <strong style="user-select: auto;">adjacent</strong> indices and swap their values.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">the <strong style="user-select: auto;">minimum</strong> number of moves required so that </em><code style="user-select: auto;">nums</code><em style="user-select: auto;"> has </em><code style="user-select: auto;">k</code><em style="user-select: auto;"> <strong style="user-select: auto;">consecutive</strong> </em><code style="user-select: auto;">1</code><em style="user-select: auto;">'s</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong class="example" style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,0,0,1,0,1], k = 2
<strong style="user-select: auto;">Output:</strong> 1
<strong style="user-select: auto;">Explanation:</strong> In 1 move, nums could be [1,0,0,0,<u style="user-select: auto;">1</u>,<u style="user-select: auto;">1</u>] and have 2 consecutive 1's.
</pre>

<p style="user-select: auto;"><strong class="example" style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,0,0,0,0,0,1,1], k = 3
<strong style="user-select: auto;">Output:</strong> 5
<strong style="user-select: auto;">Explanation:</strong> In 5 moves, the leftmost 1 can be shifted right until nums = [0,0,0,0,0,<u style="user-select: auto;">1</u>,<u style="user-select: auto;">1</u>,<u style="user-select: auto;">1</u>].
</pre>

<p style="user-select: auto;"><strong class="example" style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> nums = [1,1,0,1], k = 2
<strong style="user-select: auto;">Output:</strong> 0
<strong style="user-select: auto;">Explanation:</strong> nums already has 2 consecutive 1's.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= nums.length &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">nums[i]</code> is <code style="user-select: auto;">0</code> or <code style="user-select: auto;">1</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= k &lt;= sum(nums)</code></li>
</ul>
</div>