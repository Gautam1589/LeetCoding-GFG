# Anagram
## Easy 
<div class="problem-statement" style="user-select: auto;">
                <p style="user-select: auto;"></p><p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Given two strings<strong style="user-select: auto;">a</strong>and<strong style="user-select: auto;">b</strong>consisting of lowercase characters. The task is to check whether two given strings are an anagram of each other or not. An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, act and tac are an anagram of each other.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></span></p>

<pre style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:</strong>a = geeksforgeeks, b = forgeeksgeeks
<strong style="user-select: auto;">Output: </strong>YES
<strong style="user-select: auto;">Explanation: </strong>Both the string have samecharacters with
        same frequency. So, both are anagrams.</span></pre>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></span></p>

<pre style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:</strong>a = allergy, b = allergic
<strong style="user-select: auto;">Output: </strong>NO
<strong style="user-select: auto;">Explanation:</strong>Characters in both the strings are 
&nbsp;       not same, so they are not anagrams.</span></pre>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Your Task:</strong></span><br style="user-select: auto;">
<span style="font-size: 18px; user-select: auto;">You don't need to read input or print anything. Your&nbsp;</span><span style="font-size: 18px; user-select: auto;">task is to complete the function&nbsp;<strong style="user-select: auto;">isAnagram()</strong> which takes the string <strong style="user-select: auto;">a</strong> and string <strong style="user-select: auto;">b</strong> as input parameter and check if the two strings are an anagram of each other. The function returns true if the strings are anagram else it returns false.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Note: In python, you have to return True or False.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Expected Time Complexity:</strong>O(|a|+|b|).<br style="user-select: auto;">
<strong style="user-select: auto;">Expected Auxiliary Space:</strong>O(Number of distinct characters).</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Note:</strong> |s| represents the length of string s.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Constraints:</strong><br style="user-select: auto;">
1 ≤ |a|,|b| ≤ 10<sup style="user-select: auto;">5</sup></span></p>
 <p style="user-select: auto;"></p>
            </div>