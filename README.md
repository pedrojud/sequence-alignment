# sequence-alignment

The computational challenge I wish to address is the one associated with comparing 2 sequences, more specifically, from 2 sequence of characters representative of genes (strings), I aim to find the optimal alignment between the 2 strings. 

This means aiming to present and implement an efficient algorithm that takes 2 sequences and determines the best alignmen tbetween them by introducing spaces in either one of the sequences so that the difference between the 2 is the ‘shortest’ possible, considering insertion, deletion and substitution operations. 

Alignment can be defined as ‘the insertion of spaces in arbitrary locations along the sequences sothat they end up with the same size’ (Setubal and Meidanis, 1997). I aim to implement a dynamic programming algorithm to solve this problem, in a memoized and bottom-up approach. To do so, I will use bidimensional arrays as data structures to save and find optimal solutions.
