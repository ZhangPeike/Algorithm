#!/usr/bin/python
class Node(object):
  def __init__(self, data, next = None):
    self.data=data
    self.next=next

class TwoWayNode(object):
  def __init__(self, data, previous = None, next = None):
    Node.__init__(self, data, next)
    self.previous = previous


