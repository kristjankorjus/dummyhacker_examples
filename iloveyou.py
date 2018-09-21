#!/usr/bin/python
import random

def test(a):
    result_string = ''
    for i in range(100):
        result_string += '<p style="color:rgb({}, {}, {});font-size:{}px;">I love you {}!</p>'.format(
            random.randint(0,255),
            random.randint(0,255),
            random.randint(0,255),
            random.randint(5,20),
            a)
    return result_string

if __name__ == '__main__':
    print test('Laura')
