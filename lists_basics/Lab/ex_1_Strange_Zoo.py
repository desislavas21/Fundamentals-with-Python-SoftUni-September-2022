# You are at the zoo, and the meerkats look strange.
# You will receive 3 strings on separate lines, representing the tail, the body, and the head of an animal in that order.
# Your task is to re-arrange the elements in a list so that the animal looks normal again:
# •	On the first position is the head;
# •	On the second position is the body;
# •	On the last one is the tail.
# Input	                            Output
# my tail
# my body seems on place
# my head is on the wrong end!	    ['my head is on the wrong end!', 'my body seems on place', 'my tail']
#
# tail
# body
# head	                            ['head', 'body', 'tail']
#
# T
# B
# H	                                ['H', 'B', 'T']

result = []
tail = input()
body = input()
head = input()
result.append(head)
result.append(body)
result.append(tail)
print(result)