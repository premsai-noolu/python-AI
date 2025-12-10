"""Generators always come up with yield as keyword

with the help of generators:
You save memory.
you dont want to save the results immediately.
lazy evaluation
"""

"""The next() method is used with generators in Python to retrieve the next value from the generator's sequence of values. Here's how it works:

Generator Initialization: When you define a generator function with yield, it does not execute any of its code until you call the function to create a generator object.

Using the next() Method: Once you have a generator object, you can call next(generator_object) to execute the generator function until it reaches the next yield statement. At this point, the generator will pause and return the value specified in the yield.

Continued Execution: Every time you call next(generator_object), the generator resumes execution from where it last paused (after the most recent yield) and continues until it hits the next yield.

Stopping Iteration: If the generator function runs to completion without more yield statements, it raises a StopIteration exception, which indicates that there are no more values to yield.

Handling Exceptions: You can also catch exceptions thrown by the generator, including StopIteration, to control the iteration process or handle cleanup.

In essence, next() allows you to traverse generator sequences step-by-step, enabling more efficient memory use since values are generated on-the-fly rather than stored in memory all at once."""

def get_chai_gen():
    yield "cup 1:lemon tea"
    yield "cup 2: Elaichi chai"
    yield "cup 3: Ginger chai"

chai=get_chai_gen() #It will create a generator object
print(chai)

print(next(chai))
print(next(chai))
print(next(chai))
print(next(chai)) # Give stopIteration error