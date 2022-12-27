# Chapter 5 - Running Time Analysis

Its hard to spot inefficent code when we are only running small tests on it, problems can be seen more clearly when we apply larger inputs.

#### Asymptotic Analysis

We start by measuring the time taken to run some programs.
You can observe how the runtime of the program is affect as the size of our inputs grow larger and larger.

As an example, if we have a program that uses a list as an input, it may run slower if it contained 1 million item than a list only containing ten items.

Now we count up the cost of the program, these costs will be evaluated depending on the different operations that it runs.
The cost of the entire program will be evaluted by the costs of all operations executed by the program.

The Big-O notation gives us a way to group up these functions based on their runtime so we can compare them to each other. This gives us away to discuss the efficency of the programs.

By thinking about and anaylzing the efficency of code, we can make better decisions when developing programs and allow us to build good habits. The goal of increasing the efficency of in our data structures will be our focus as we progress and are introduced to new data structures/ideas.

## Timing Programs

Here is a function that takes some basic input and returns true or false
How fast is the code?
Run the program and measure how long it takes

This is an example of our output:

```
Time taken for n =  1000 :  0.04281020164489746
Time taken for n =  1000 :  0.0424959659576416
Time taken for n =  1000 :  0.04193711280822754
Time taken for n =  1000 :  0.041748046875
Time taken for n =  1000 :  0.04205918312072754
```

There are slight varations in the time it takes the program to run due to many factors. The computer is running several different programs at the same time, also when running it on different computers the differences in hardward such as processors will also result in differing runtimes.

We will use one more general function to demonstrate the ideas we've discussed so far. This function takes an input and a length, it runs the given function on lists of the given length and averages the time per run.

This is an example of our output:

```
average = 0.0001064 for n = 50
average = 0.0004152 for n = 100
average = 0.0016477 for n = 200
average = 0.0066302 for n = 400
average = 0.0268360 for n = 800
average = 0.1074970 for n = 1600
average = 0.4329827 for n = 3200
```

It also should not be surprising to observe longer runtimes as the input continues to increase.

Now we should try and make our code faster with some simple improvements, eliminating code that is doing redundant or unnessesary work.

upon running duplicates1 and duplicates1 we can see a significant difference.

```
Duplicates 1                         Duplicates 2

average = 0.0001008 for n = 50       average = 0.0000436 for n = 50
average = 0.0004085 for n = 100      average = 0.0001644 for n = 100
average = 0.0015799 for n = 200      average = 0.0006566 for n = 200
average = 0.0065620 for n = 400      average = 0.0025097 for n = 400
average = 0.0270511 for n = 800      average = 0.0103761 for n = 800
average = 0.1073898 for n = 1600     average = 0.0422791 for n = 1600
average = 0.4320724 for n = 3200     average = 0.1703393 for n = 3200

```

There is another short cut we can take with the loops we used in our function
