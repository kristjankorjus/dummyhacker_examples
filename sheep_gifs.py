#!/usr/bin/python

def display(a):
    result_string = ''
    for i in range(a):
        result_string += '<img src="https://img.buzzfeed.com/buzzfeed-static/static/2015-02/19/11/enhanced/webdr11/anigif_enhanced-6690-1424363569-2.gif">'
    return result_string

if __name__ == '__main__':
    print display(5)
