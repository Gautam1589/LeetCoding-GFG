<h2><a href="https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/">109. Convert Sorted List to Binary Search Tree</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given the <code style="user-select: auto;">head</code> of a singly linked list where elements are <strong style="user-select: auto;">sorted in ascending order</strong>, convert it to a height balanced BST.</p>

<p style="user-select: auto;">For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of <em style="user-select: auto;">every</em> node never differ by more than 1.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/17/linked.jpg" style="width: 500px; height: 388px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> head = [-10,-3,0,5,9]
<strong style="user-select: auto;">Output:</strong> [0,-3,9,-10,null,5]
<strong style="user-select: auto;">Explanation:</strong> One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> head = []
<strong style="user-select: auto;">Output:</strong> []
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">The number of nodes in <code style="user-select: auto;">head</code> is in the range <code style="user-select: auto;">[0, 2 * 10<sup style="user-select: auto;">4</sup>]</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">-10<sup style="user-select: auto;">5</sup> &lt;= Node.val &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
</ul>
</div>