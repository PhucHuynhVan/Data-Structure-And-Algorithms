# Linked List Interview Problems
1. Singly Linked List Cycle Check

    * **Problem**: Given a singly linked list, write a function which takes in the first node in a singly linked list and returns a boolean indicating if the linked list contains a "cycle".
      A cycle is when a node's next point actually points back to a previous node in the list. This is also sometimes known as a circularly linked list.


2. Linked List Reversal

    * **Problem**: Write a function to reverse a Linked List in place. The function will take in the head of the list as input and return the new head of the list.


3. Linked List Nth to Last Node

    * **Problem Statement**: Write a function that takes a head node and an integer value **n** and then returns the nth to last node in the linked list


You've been given the Linked List Node class code:

    class Node(object):
    
        def __init__(self,value):
            
            self.value = value
            self.nextnode = None