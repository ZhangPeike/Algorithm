#!/usr/bin/python3
from TwoWayNode import TwoWayNode

head = TwoWayNode(1)
tail = head
for data in range(2, 6):
  tail.next = TwoWayNode(data, tail);
  tail = tail.next
probe = tail
while probe != None:
  print(probe.data)
  probe=probe.previous
