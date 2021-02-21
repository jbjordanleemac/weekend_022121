#!/usr/bin/python

class weekend():
  day_off="yes day off"
  fix_stuff="yes extra time to fix stuff"

  def __init__(self, whatday, dowhat):
    self.whatday=whatday
    self.dowhat=dowhat

w1=weekend('Sat', 'Fix shower door')
print(w1.dowhat)  

