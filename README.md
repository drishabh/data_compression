
1. compression_postings ... Program that compresses the postings of a retrieval system. The keys are saved in a dictionary while their posting lists are saved as the value
                             of those keys in a linked list. The program uses "variable byte" encoding and saves the posting lists in file called "comp_post.txt". The program
                             also lets you retrieve a posting list of any key after ot has compressed the postings. It uses "linecache" library for faster access of posting
                             list of a given key saved on a file in disk.

2. compression_Gamma ... Program that compresses the postings of a retrieval system. The keys are saved in a dictionary while their posting lists are saved as the value of 
                         those keys in a linked list. THe program uses "Gamma" encoding and saves the posting lists in a file called "comp_post.txt". This program also uses
                         "linecache" library for faster access to a given line in a file on disk.

3. dictionary.txt ... Set of space separated vocabulory for the IR system used in 1 and 2.

4. linkedlist.py ... Implementation of ordered linked list.
 
