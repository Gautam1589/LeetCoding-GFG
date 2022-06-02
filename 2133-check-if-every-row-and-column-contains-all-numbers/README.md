<h2><a href="https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/">2133. Check if Every Row and Column Contains All Numbers</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">An <code style="user-select: auto;">n x n</code> matrix is <strong style="user-select: auto;">valid</strong> if every row and every column contains <strong style="user-select: auto;">all</strong> the integers from <code style="user-select: auto;">1</code> to <code style="user-select: auto;">n</code> (<strong style="user-select: auto;">inclusive</strong>).</p>

<p style="user-select: auto;">Given an <code style="user-select: auto;">n x n</code> integer matrix <code style="user-select: auto;">matrix</code>, return <code style="user-select: auto;">true</code> <em style="user-select: auto;">if the matrix is <strong style="user-select: auto;">valid</strong>.</em> Otherwise, return <code style="user-select: auto;">false</code>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/21/example1drawio.png" style="width: 250px; height: 251px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> matrix = [[1,2,3],[3,1,2],[2,3,1]]
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.
Hence, we return true.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/21/example2drawio.png" style="width: 250px; height: 251px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> matrix = [[1,1,1],[1,2,3],[1,2,3]]
<strong style="user-select: auto;">Output:</strong> false
<strong style="user-select: auto;">Explanation:</strong> In this case, n = 3, but the first row and the first column do not contain the numbers 2 or 3.
Hence, we return false.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">n == matrix.length == matrix[i].length</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 100</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= matrix[i][j] &lt;= n</code></li>
</ul>
</div>