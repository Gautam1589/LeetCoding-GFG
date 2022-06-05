<h2><a href="https://leetcode.com/problems/grid-illumination/">1001. Grid Illumination</a></h2><h3>Hard</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">There is a 2D <code style="user-select: auto;">grid</code> of size <code style="user-select: auto;">n x n</code> where each cell of this grid has a lamp that is initially <strong style="user-select: auto;">turned off</strong>.</p>

<p style="user-select: auto;">You are given a 2D array of lamp positions <code style="user-select: auto;">lamps</code>, where <code style="user-select: auto;">lamps[i] = [row<sub style="user-select: auto;">i</sub>, col<sub style="user-select: auto;">i</sub>]</code> indicates that the lamp at <code style="user-select: auto;">grid[row<sub style="user-select: auto;">i</sub>][col<sub style="user-select: auto;">i</sub>]</code> is <strong style="user-select: auto;">turned on</strong>. Even if the same lamp is listed more than once, it is turned on.</p>

<p style="user-select: auto;">When a lamp is turned on, it <strong style="user-select: auto;">illuminates its cell</strong> and <strong style="user-select: auto;">all other cells</strong> in the same <strong style="user-select: auto;">row, column, or diagonal</strong>.</p>

<p style="user-select: auto;">You are also given another 2D array <code style="user-select: auto;">queries</code>, where <code style="user-select: auto;">queries[j] = [row<sub style="user-select: auto;">j</sub>, col<sub style="user-select: auto;">j</sub>]</code>. For the <code style="user-select: auto;">j<sup style="user-select: auto;">th</sup></code> query, determine whether <code style="user-select: auto;">grid[row<sub style="user-select: auto;">j</sub>][col<sub style="user-select: auto;">j</sub>]</code> is illuminated or not. After answering the <code style="user-select: auto;">j<sup style="user-select: auto;">th</sup></code> query, <strong style="user-select: auto;">turn off</strong> the lamp at <code style="user-select: auto;">grid[row<sub style="user-select: auto;">j</sub>][col<sub style="user-select: auto;">j</sub>]</code> and its <strong style="user-select: auto;">8 adjacent lamps</strong> if they exist. A lamp is adjacent if its cell shares either a side or corner with <code style="user-select: auto;">grid[row<sub style="user-select: auto;">j</sub>][col<sub style="user-select: auto;">j</sub>]</code>.</p>

<p style="user-select: auto;">Return <em style="user-select: auto;">an array of integers </em><code style="user-select: auto;">ans</code><em style="user-select: auto;">,</em><em style="user-select: auto;"> where </em><code style="user-select: auto;">ans[j]</code><em style="user-select: auto;"> should be </em><code style="user-select: auto;">1</code><em style="user-select: auto;"> if the cell in the </em><code style="user-select: auto;">j<sup style="user-select: auto;">th</sup></code><em style="user-select: auto;"> query was illuminated, or </em><code style="user-select: auto;">0</code><em style="user-select: auto;"> if the lamp was not.</em></p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/19/illu_1.jpg" style="width: 750px; height: 209px; user-select: auto;" naptha_cursor="text">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
<strong style="user-select: auto;">Output:</strong> [1,0]
<strong style="user-select: auto;">Explanation:</strong> We have the initial grid with all lamps turned off. In the above picture we see the grid after turning on the lamp at grid[0][0] then turning on the lamp at grid[4][4].
The 0<sup style="user-select: auto;">th</sup>&nbsp;query asks if the lamp at grid[1][1] is illuminated or not (the blue square). It is illuminated, so set ans[0] = 1. Then, we turn off all lamps in the red square.
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/19/illu_step1.jpg" style="width: 500px; height: 218px; user-select: auto;">
The 1<sup style="user-select: auto;">st</sup>&nbsp;query asks if the lamp at grid[1][0] is illuminated or not (the blue square). It is not illuminated, so set ans[1] = 0. Then, we turn off all lamps in the red rectangle.
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/19/illu_step2.jpg" style="width: 500px; height: 219px; user-select: auto;">
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,1]]
<strong style="user-select: auto;">Output:</strong> [1,1]
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> n = 5, lamps = [[0,0],[0,4]], queries = [[0,4],[0,1],[1,4]]
<strong style="user-select: auto;">Output:</strong> [1,1,0]
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= n &lt;= 10<sup style="user-select: auto;">9</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= lamps.length &lt;= 20000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= queries.length &lt;= 20000</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">lamps[i].length == 2</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= row<sub style="user-select: auto;">i</sub>, col<sub style="user-select: auto;">i</sub> &lt; n</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">queries[j].length == 2</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= row<sub style="user-select: auto;">j</sub>, col<sub style="user-select: auto;">j</sub> &lt; n</code></li>
</ul>
</div>