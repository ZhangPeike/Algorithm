#!/usr/bin/python2
class Node(object):
  def __init__(self, data, next=None):
    """Instantiates a node"""
    self.data=data
    self.next=next

node1=None
node2=Node('A',None)
node3=Node('B',node2)
node4=Node('C',node3)
head=node4
while head != None:
  print head.data
  head=head.next
