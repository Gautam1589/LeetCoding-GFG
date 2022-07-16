# Rotate by 90 degree
## Easy
<div class="problem-statement" style="user-select: auto;">
                <p style="user-select: auto;"></p><p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Given a<strong style="user-select: auto;"> </strong>square<strong style="user-select: auto;"> </strong>matrix&nbsp;of size <strong style="user-select: auto;">N x N</strong>. The task is to rotate it by<strong style="user-select: auto;"> 90 degrees in anti-clockwise</strong> direction without using any extra space.&nbsp;</span><br style="user-select: auto;">
<br style="user-select: auto;">
<span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></span></p>

<pre style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input</strong>:
N = 3 
matrix[][] = {{1, 2, 3},
&nbsp;             {4, 5, 6}
&nbsp;             {7, 8, 9}}
<strong style="user-select: auto;">Output</strong>: 
Rotated Matrix:
3 6 9
2 5 8
1 4 7
</span></pre>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></span></p>

<pre style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input</strong>:
N = 2
matrix[][] = {{1, 2},
&nbsp;             {3, 4}}
<strong style="user-select: auto;">Output</strong>: 
Rotated Matrix:
2 4
1 3</span>
</pre>

<p style="user-select: auto;"><br style="user-select: auto;">
<span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Your Task:</strong><br style="user-select: auto;">
You dont need to read input or print anything. Complete the function <strong style="user-select: auto;">rotateby90</strong>() which takes&nbsp;the matrix as input parameter and rotates it by 90 degrees in anti-clockwise direction without using any extra space. You have to modify the input matrix <strong style="user-select: auto;">in-place</strong>.&nbsp;<br style="user-select: auto;">
<br style="user-select: auto;">
<strong style="user-select: auto;">Expected Time Complexity</strong>: O(N<sup style="user-select: auto;">2</sup>)<br style="user-select: auto;">
<strong style="user-select: auto;">Expected Auxiliary Space</strong>: O(1)</span><br style="user-select: auto;">
<br style="user-select: auto;">
<span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Constraints:</strong><br style="user-select: auto;">
1 ≤ N ≤ 100<br style="user-select: auto;">
1 &lt;= matrix[][] &lt;= 1000</span></p>
 <p style="user-select: auto;"></p>
            </div>