# Chapter 4 - Testing

## Writing Tests

To test our code we have to write more code that will check to make sure that it behaves as we need it to.
It is important that we test the behavior, not its implementation.

The assert statement will check if the code being run matches our desired end behavior.
It does this with a boolean value, raising an error when the assertion returns False.

We should be trying to eliminate the possibility of errors arising in our code at a later stage in our production.

## Unit Testings with Unittest

An assertion statement is fine enough for testing small pieces of code and tiny programs however when we are dealing with more serious code, were gonna need to use more tools.
We will need to write proper unit tests for our code.
Unit tests are supposed to test for a specific behavior of a special function.

Because there are so many behaviors to test for we will have to write many tests, and run these tests each time we change our code to ensure it still behaves the way that we want it to.

Theres a standard package we use for writing unit tests in Python, called `unittest`.
It gives us a way to write our tests and run them all together.

We import the following package in our test file and import the code that we will be testing.
The tests will be methods of a class that extends the `unittest.TestCase` class.
Every test method should start with the word "test", if it does not start with "test" then its not gonna run.
Finally tests are run all together by calling the `unittest.main()` function.

## Test-Driven Development

This is the idea that we write our tests before ever writing the code.
Writing tests forces you to do 2 thing:

1. Decide how the function is supposed to be used. (what are its paramters and what should it be returning?)

2. Write only the code that we need. If theres code written that doesnt contribute to the behavior were testing for, then it isnt code that we need.

There are 3 phases of the test-driven development process:

- Red: The test fails
- Green: You get the test to pass by changing code
- Refactor: You clean up the code, remove duplications

Refactoring is the process of cleaning up your code, it most often refers to the process of removing duplications in the program.
Duplication in code can be the source the many errors, if code is duplicated containing a bug, we now how to debug to find the error twice.

## What to Test

Take a moment and step away from the computer, dont write any code.
Just think.
Think about the methods you will be writing.
Ask yourself "what should happen when I run this code?" and "How do I want to use this code?".

- Write tests that use code the way its supposed to be used.
- Then write some tests that use your code incorrectly.
- Test the edge cases, those cases that rarely come up but will eventually without a doubt.
- A bug or incorrect behavior can come up as an error again, you can use these cases to create a scenerio we can test for.

## Testing and Object-Oriented Design

In OOP we divide code into classes that have public methods, we call these public methods the interface to the class.

To start a design we first identify our classes and methods.
Our unit tests will check that the behavior of the code matches the expected behavior.

When writing a class we can reduce the number of things we need to focus on by assuming each class works the way that it should.
We can do this by testing each class individually so that once our classes become more complex and an error arises, we can assume that it is not from coming from a previous written class.

You can save yourself a lot of time in the development phase by not having to worry about debugging untested code.
When you have lots of untested code in a large code base, the error could come from anywhere, these tests help you narrow down your search.
