<h2><a href="https://leetcode.com/problems/regular-expression-matching/">10. Regular Expression Matching</a></h2><h3>Hard</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">Given an input string <code style="user-select: auto;">s</code>&nbsp;and a pattern <code style="user-select: auto;">p</code>, implement regular expression matching with support for <code style="user-select: auto;">'.'</code> and <code style="user-select: auto;">'*'</code> where:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">'.'</code> Matches any single character.​​​​</li>
	<li style="user-select: auto;"><code style="user-select: auto;">'*'</code> Matches zero or more of the preceding element.</li>
</ul>

<p style="user-select: auto;">The matching should cover the <strong style="user-select: auto;">entire</strong> input string (not partial).</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "aa", p = "a"
<strong style="user-select: auto;">Output:</strong> false
<strong style="user-select: auto;">Explanation:</strong> "a" does not match the entire string "aa".
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "aa", p = "a*"
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "ab", p = ".*"
<strong style="user-select: auto;">Output:</strong> true
<strong style="user-select: auto;">Explanation:</strong> ".*" means "zero or more (*) of any character (.)".
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= s.length&nbsp;&lt;= 20</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= p.length&nbsp;&lt;= 30</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> contains only lowercase English letters.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">p</code> contains only lowercase English letters, <code style="user-select: auto;">'.'</code>, and&nbsp;<code style="user-select: auto;">'*'</code>.</li>
	<li style="user-select: auto;">It is guaranteed for each appearance of the character <code style="user-select: auto;">'*'</code>, there will be a previous valid character to match.</li>
</ul>
</div>