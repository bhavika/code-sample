
### Welcome! 

This is a short code sample designed to show you that I can:
- Use Python & know several language features. 
- Use data structures & algorithms to solve a problem. 
- Write unit tests. 
- Write neat, well-documented code. 
- Break up a problem into steps & implement each of them. 
- Use Git. 

Complexity: The algorithm used is Levenshtein Distance. I use a graph and Dijkstra's algorithm to find the 
shortest route from one word to another given that each edge in the graph has a cost attached to it. This cost is calculated
using the Levenshtein Distance (or Edit Distance) logic. 

#### Problem: 

You’ve probably heard of the Levenshtein distance between strings. 
Your task is to transform one word into another, with four operations: add a letter, delete a letter, change a letter, and take an anagram of the existing word.  

Additionally, you have to obey the following rules:

- Every interim step between the first and the last word must also be a word
- No interim step can be less than three letters
- The first line of input will contain the “cost” of each operation in the order above
- The second line of input will contain the starting word
- The third line of input will contain the ending word

Your goal is to find the lowest possible “cost” of transforming the starting word into the ending word.  
You can use any word list you like. Depending on your word list, your answer might not be exactly the same as ours below.

Your solution should detect and handle invalid input, and return -1 if there is no solution.

#### Example input 1:

1 3 1 5

HEALTH

HANDS

(output: 7)  (HEALTH - HEATH - HEATS - HENTS - HENDS - HANDS)

#### Example input 2:

1 9 1 3

TEAM

MATE

(output: 3) (TEAM - MATE)

#### Example input 3:

7 1 5 2

OPHTHALMOLOGY

GLASSES

(output: -1)


### Files

1) edit_distance.py: Contains the entire algorithm with a function for taking & parsing user input.
2) tests.py: Unit tests - not meant to be comprehensive, but demonstrative. 
3) 20k.txt: The word list I test against. 


### Running 


You can directly several input cases present in `tests.py`. The code was written in Python 3 and uses nothing but the 
standard library for the main task. 

You can run `tests.py` using `pytest` in the terminal (under the code-sample directory) but pytest needs to be installed first. 

To install pytest, run:

`pip install -U pytest`
