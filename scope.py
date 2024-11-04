# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# %%
from turtle import title


print("")
title = " Lesson 11: Scope "
print(f"{title}".center(50, "="))
print("")

name = "Sisovin"
count = 1

def another():
  color = "blue"
  global count
  count += 1
  print(count)
  
  def greeting(name):
    nonlocal color
    color = "red"
    print(color)
    print(name)
    
  greeting("Sisovin")
  
another()

print("")
# %%
