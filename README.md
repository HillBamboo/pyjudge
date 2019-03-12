# pyjudge
A simple testing utility to quickly compare a solution with its reference implementation.


Example use:
```python
from pyjudge import judge

fib_tests = [
    (0,),
    (1,),
    (2,),
    (10,),
    (22,),
    (31,)
]

def fib(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return fib(index - 1) + fib(index - 2)

@judge(reference_solution=fib, tests=fib_tests)
def my_fib(index):
    results = [0, 1]
    if index <= 1:
        return results[index]
    else:
        cur_index = 1
        while cur_index < index:
            cur_index += 1
            results += [results[-1] + results[-2]]
        return results[index]

```

Output:
```
Test #0 : my_fib : SUCCESS - expected: 0, got: 0
Test #1 : my_fib : SUCCESS - expected: 1, got: 1
Test #2 : my_fib : SUCCESS - expected: 1, got: 1
Test #3 : my_fib : SUCCESS - expected: 55, got: 55
Test #4 : my_fib : SUCCESS - expected: 17711, got: 17711
Test #5 : my_fib : SUCCESS - expected: 1346269, got: 1346269
```
