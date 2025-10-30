# 28. Find the Index of the First Occurrence in a String

## Problem Description
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

## Examples

Example 1:
Input: haystack = "sadbutsad", needle = "sad" Output: 0 
Explanation: "sad" occurs at index 0 and 6. The first occurrence is at index 0, so we return 0. 

Example 2: 
Input: haystack = "leetcode", needle = "leeto" Output: -1 
Explanation: "leeto" did not occur in "leetcode", so we return -1. 

## Constraints

1 <= haystack.length, needle.length <= 104

## Approach

1. Use the built-in string search function:
   - In C++ → `haystack.find(needle)`
   - In Python → `haystack.find(needle)`
2. If `needle` is not found, `find()` returns `-1`.
3. Return the found index directly.