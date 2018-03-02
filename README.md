
1. `compression_postings ... Program that compresses the postings of a retrieval system. The keys are saved in a dictionary while their posting lists are saved as the value
                            of those keys in a linked list. The program uses "variable byte" encoding and saves the posting lists in file called "comp_post.txt". The program
                            also lets you retrieve a posting list of any key after ot has compressed the postings. It uses "linecache" library for faster access of posting
                            list of a given key saved on a file in disk.
