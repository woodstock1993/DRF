# Iterator와 Iterable
class Iterator(object):
    def __init__(self):
        self.index = 0
	
    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 10:
            raise StopIteration
        n = self.index
        self.index += 1
        return n

class Counter(object):
    def __iter__(self):
        iter = Iterator()
        return iter

    
# Iterable 객체는 내부에 __iter__ 메서드를 가지고 있어야한다. 이후 Iterator 객체 내부의 __next__ 메서드를 사용하는 것이다.
c = Counter()
iterator = c.__iter__()
print(iterator)

# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())


# while True:
#     try:
#         print(iterator.__next__())
#     except StopIteration:
#         break

# for _ in range(10):
#     i = iterator.__next__()
#     print(i)


# 3lazy nature. When an iterator is created, the elements are not yielded until they are requested. 

# 위 개념과 유사한 것이 generator 입니다. 함수 안에 `yield 반환값`만 작성해 주면 이터레이터와 같은 기능을 하는 함수를 손쉽게 만들 수 있습니다. 
def gen():
    for num in range(1, 2147483648):
        yield num

g = gen()
print(g.__next__())


# for i in generator():
#     print(i, end=' ')

# 에러 발생시 다음 yield로 넘어가지 않는 예시
def f():
    return 1/0

def g():
    yield f()
    yield 42

# gen = g()
# next(gen)
# next(gen)

def f():
    try:
        yield 1
        try:
            yield 2
            1/0
            yield 3  # never get here
        except ZeroDivisionError:
            yield 4
            yield 5
            raise
        except:
            yield 6
            yield 7     # the "raise" above stops this
    except:
        yield 8
    yield 9
    try:
        x = 12
    finally:
        yield 10
    yield 11

# print(list(f()))


def number_generator(stop):
    n = 0    
    while n < stop:    
        yield n        
        n += 1
    return 'Merry Christmas'
 
# g = number_generator(1)
# print(next(g))
# print(next(g))

# generator를 사용하여 두수 사이의 소수를 반환하는 로직
import math
def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def prime_number_generator(start, stop):
    for num in range(start, stop+1):
        if is_prime_number(num):
            yield num
 
# g = prime_number_generator(950, 1000)
# print(type(g))
# for i in g:
#     print(i, end=' ')


def number_coroutine():
    receiver = None
    while True:        ##코루틴을 계속 유지하기 위해 무한 루프 사용
        x = (yield receiver) ##코루틴 바깥에서 값을 받아옴, yield를 괄호로 묶어야 함
        receiver = x
 
# co = number_coroutine()
# co.__next__()
# co.send(None)      ##코루틴 안의 yield까지 코드 실행(최초 실행)


def number_coroutine():
    x = None
    while True:
        x = (yield x)    # 코루틴 바깥에서 값을 받아오면서 바깥으로 값을 전달
        if x == 3:
            return 3
 
def print_coroutine():
    while True:
        x = yield from number_coroutine()   # 하위 코루틴의 yield에 지정된 값을 다시 바깥으로 전달
        print('print_coroutine:', x)
 
# co = print_coroutine()
# next(co)
 
# x = co.send(1)    # number_coroutine으로 1을 보냄
# print(x)          # 1: number_coroutine의 yield에서 바깥으로 전달한 값
# x = co.send(2)    # number_coroutine으로 2를 보냄
# print(x)          # 2: number_coroutine의 yield에서 바깥으로 전달한 값
# x = co.send(4) 
# print(x)
# co.send(3)

import asyncio

async def main_2():
    for i in range(100):
        print(i)