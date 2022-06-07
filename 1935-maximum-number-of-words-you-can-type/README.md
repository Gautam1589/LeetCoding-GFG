<h2><a href="https://leetcode.com/problems/maximum-number-of-words-you-can-type/">1935. Maximum Number of Words You Can Type</a></h2><h3>Easy</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.</p>

<p style="user-select: auto;">Given a string <code style="user-select: auto;">text</code> of words separated by a single space (no leading or trailing spaces) and a string <code style="user-select: auto;">brokenLetters</code> of all <strong style="user-select: auto;">distinct</strong> letter keys that are broken, return <em style="user-select: auto;">the <strong style="user-select: auto;">number of words</strong> in</em> <code style="user-select: auto;">text</code> <em style="user-select: auto;">you can fully type using this keyboard</em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> text = "hello world", brokenLetters = "ad"
<strong style="user-select: auto;">Output:</strong> 1
<strong style="user-select: auto;">Explanation:</strong> We cannot type "world" because the 'd' key is broken.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> text = "leet code", brokenLetters = "lt"
<strong style="user-select: auto;">Output:</strong> 1
<strong style="user-select: auto;">Explanation:</strong> We cannot type "leet" because the 'l' and 't' keys are broken.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> text = "leet code", brokenLetters = "e"
<strong style="user-select: auto;">Output:</strong> 0
<strong style="user-select: auto;">Explanation:</strong> We cannot type either word because the 'e' key is broken.
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= text.length &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= brokenLetters.length &lt;= 26</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">text</code> consists of words separated by a single space without any leading or trailing spaces.</li>
	<li style="user-select: auto;">Each word only consists of lowercase English letters.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">brokenLetters</code> consists of <strong style="user-select: auto;">distinct</strong> lowercase English letters.</li>
</ul>
</div>