#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# test_modula.py
PI = 3.14
print('test program name -> ', __name__)

def number_input():
    output = input('숫자 입력 > ')
    return float(output)

def get_circumference(radius):
    return PI * 2 * radius

def get_circle_area(radius):
    return PI * radius * radius

