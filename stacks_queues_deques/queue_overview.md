# Queues Overview
In this lecture we will get an overview of what a Queue is, in the next lecture we will implement our own Queue class.

A **queue** is an ordered collection of items where the addition of new items happens at one end, called the “rear,” and the removal of existing items occurs at the other end, commonly called the “front.” As an element enters the queue it starts at the rear and makes its way toward the front, waiting until that time when it is the next element to be removed.

The most recently added item in the queue must wait at the end of the collection. The item that has been in the collection the longest is at the front. This ordering principle is sometimes called **FIFO, first-in first-out**. It is also known as “first-come first-served.”

The simplest example of a queue is the typical line that we all participate in from time to time. We wait in a line for a movie, we wait in the check-out line at a grocery store, and we wait in the cafeteria line. The first person in that line is also the first person to get serviced/helped.

Let's see a diagram which shows this and compares it to the Stack Data Structure:
![alt text](https://netmatze.files.wordpress.com/2014/08/queue.png)
Note how we have two terms here, **Enqueue** and **Dequeue**. The enqueue term describes when we add a new item to the rear of the queue. The dequeue term describes removing the front item from the queue.


Let's take a look at how pop and push methods would work with a Queue (versus that of a Stack):

# Implementation of Queue
In this lecture we will build on our previous understanding of Queues by implementing our own class of Queue!

# Queue Methods and Attributes
Before we begin implementing our own queue, let's review the attribute and methods it will have:

* Queue() creates a new queue that is empty. It needs no parameters and returns an empty queue.
* enqueue(item) adds a new item to the rear of the queue. It needs the item and returns nothing.
* dequeue() removes the front item from the queue. It needs no parameters and returns the item. The queue is modified.
* isEmpty() tests to see whether the queue is empty. It needs no parameters and returns a boolean value.
* size() returns the number of items in the queue. It needs no parameters and returns an integer.
