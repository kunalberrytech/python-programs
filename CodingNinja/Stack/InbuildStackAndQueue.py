import queue


# ## Inbuilt stack
# q = queue.Queue()
#
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)
# q.put(5)
# #
# while not q.empty():
#     print(q.get())
#
q = queue.LifoQueue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)

while not q.empty():
    print(q.get())