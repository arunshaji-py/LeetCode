# Notes from my studies


## Python interpreter

When people say “Python interpreter”, they usually mean 'CPython', which is:

A program written in C that executes Python code.






## Meaning of 'ordered' when it comes to data structures.

It means the data stucture remembers the order in which the elements were inserted.
for eg: List( 5,1,2) remembers it. When you print it print list you gets the output as 5,1,2. Where as if you 
use Set(5,1,2) and print it the output might be 1, 2, 5 . That's because set() is unordered. 

Ordered doesn't mean sorted.

# List Vs Set 

Feature                 list                                        set

Type of C array         sequential pointer array            hash table array

Position logic          index order                         hash-based index

Access method           arr[i]                              hash → index

Purpose                 ordered storage                     fast membership test

Ordering                preserved                           not preserved

Both list and set are C-level structures ( struct ) in CPython.
A list is a dynamic array of references, while a set is a hash table implemented using an array of slots with hashing and collision handling.