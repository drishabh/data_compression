"""
File:          compressing_Gamma.py
Author:        Rishabh Dalal
Date:          2/03/2018
Description:   Enoding and decoding postings of a retrieval system using
               Gamma byte encoding.

Modified:      
Change:        

"""

#!/usr/bin/env python3

import sys
import linecache
from collections import OrderedDict
from linkedList import LinkedList
import random
import math

def main():

  vocab = OrderedDict()
  indexDict = {}

  filename = "comp_posting.txt" ##File to save the compressed postings to
  file_write = open(filename, 'w')
  
  file = open("dictionary.txt", 'r')  ##File containings the terms

  for word in file:
    word = word.strip()
    vocab[word] = None

  file = file.close()

  curr = 0
  for i in vocab.keys():
    indexDict[i] = curr
    curr += 1

  for key in vocab.keys():
    vocab[key] = createRandomPosting()  ##Randomly creating the posting list for eacj
                                        ##term in the vocab
  print("Printing all the keys along with its posting list:\n")
  for key in vocab.keys():
    print(key,":", end=" ")
    printLinkedList(vocab[key])
 
  print("\nCompressing the postings into file:", filename) 
  comp_post = ""
  for postings in vocab.keys():
    comp_post = compressPosting(vocab[postings])
    file_write.write(comp_post)
    file_write.write("\n")
  print("Posting lists compressed!\n")
  
  file_write.close()

  while True:
    retrieve = input("Enter the term to get its posting list from the compressed data: " )
    retrieve = retrieve.strip().lower()
  
    if not retrieve in vocab:
      print(retrieve, "is not in the dictionary")
    else:
      data = retrievePosting(indexDict[retrieve], filename)
      print("Retrieved posting:", data)
      break

def printLinkedList(lst):
  ##Printing a linked list

  top = lst._head
  print(top.getData(), end=" ")

  while top:
    top = top.getNext()
    if not top:
      break
    print(top.getData(), end=" ")
  print()

def retrievePosting(lineNumber, filename):
  ##Retrieving a line from compressed posting list saved in disk

  line = linecache.getline(filename, lineNumber+1)
  if not line:
    print("Some error in fetching line")
    sys.exit()
  
  return gammaDecode(line.strip())

def gammaDecode(data):
  ##Uncompressing a compressed posting list and returning a linked list 
  
  curr = 0
  full_list = []
  posting_list = LinkedList()

  byte = ""
  number = ""
  total = 0
  flag = False


  for bit in range(len(data)):        ##Reading the stream of bits
    if data[bit] == '1' and flag == False:
      total += 1
    elif data[bit] == '0' and flag == False:
      flag = True
    else:
      number += data[bit]
      total -= 1
      if total == 0:
        full_list.append(binaryToDecimal(('1' + number), len(number), 0))
        number = ""
        flag = False
  
  posting_list.add(full_list[0])
  for i in range(1, len(full_list)):
    posting_list.add(full_list[i] + full_list[0])

  return posting_list
   
def binaryToDecimal(binary, length, init):
  ##Recursive function to convert binary to decimal

  if not binary:
    return init
  else:
    return binaryToDecimal(binary[1:], length-1, init + (2**length)*(int (binary[0])))

def VBDecode_helper(lst, length, init):
  ##Helper fucntion to convert VB encoding into decimal  


  if not lst:
    return init
  else:
    return VBDecode_helper(lst[1:], length - 1, (init + ((128**length)*lst[0])))
      
def createRandomPosting():
  ##Creating a randomly generated posting list of given size
  ##between given integers

  SIZE = 3
  START = 1
  END = 10000
  lyst = LinkedList()

  for i in range(SIZE):
    lyst.add(random.randint(START, END))
  return lyst

def compressPosting(linkedlist):
  ##Compressing a posting list

  net = ""  ##List containg all the bytes encoding of the gaps
  lyst = []
  top = linkedlist._head
  lyst.append(top.getData())

  while True:
    top = top.getNext()
    if not top:
      break
    lyst.append(top.getData() - lyst[0])
  
  for gaps in lyst:
    byte = gammaEncode(gaps)
    net += byte
  
  return net

def gammaEncode(gap):
  ##Encoding a given integer in variable byte encoding

  if gap == 0:
    return 0
  result = int(math.log(gap, 2))*'1'
  result += "0" 
  result += str(decimal2binary(gap))[1:]
 
  return result

def decimal2binary(number):
  ##Converting a dcimal to binary

  if (number <= 1):
    return str(number)
  else:
    return str(decimal2binary(number//2)) + str(number % 2)

if __name__ == "__main__":
  main()
