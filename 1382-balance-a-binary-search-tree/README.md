<h2><a href="https://leetcode.com/problems/balance-a-binary-search-tree/">1382. Balance a Binary Search Tree</a></h2><h3>Medium</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given the <code style="user-select: auto;">root</code> of a binary search tree, return <em style="user-select: auto;">a <strong style="user-select: auto;">balanced</strong> binary search tree with the same node values</em>. If there is more than one answer, return <strong style="user-select: auto;">any of them</strong>.</p>

<p style="user-select: auto;">A binary search tree is <strong style="user-select: auto;">balanced</strong> if the depth of the two subtrees of every node never differs by more than <code style="user-select: auto;">1</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/08/10/balance1-tree.jpg" style="width: 500px; height: 319px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = [1,null,2,null,3,null,4,null,null]
<strong style="user-select: auto;">Output:</strong> [2,1,3,null,null,null,4]
<b style="user-select: auto;">Explanation:</b> This is not the only correct answer, [3,1,4,null,2] is also correct.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/08/10/balanced2-tree.jpg" style="width: 224px; height: 145px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> root = [2,1,3]
<strong style="user-select: auto;">Output:</strong> [2,1,3]
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">The number of nodes in the tree is in the range <code style="user-select: auto;">[1, 10<sup style="user-select: auto;">4</sup>]</code>.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= Node.val &lt;= 10<sup style="user-select: auto;">5</sup></code></li>
</ul>
</div>