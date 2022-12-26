from stacks_queues_deques.stack import Stack


def test_stacks():
    obj = Stack()
    assert obj.is_empty() == True
    obj.push(3)
    obj.push(4)
    assert obj.is_empty() == False
    assert obj.size() == 2
    assert obj.peek() == 4
    obj.pop()
    assert obj.size() == 1
    assert obj.peek() == 3
