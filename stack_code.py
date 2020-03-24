# Mohamed Bagayoko
# Stack Class

class StackNode(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"


class Stack(object):
    def __init__(self):
        self.top = None

    def push(self, obj):
        self.top = StackNode(obj, self.top)

    def pop(self):
        if self.top:
            node = self.top
            self.top = node.next
            return node.value
        else:
            return None

    def first(self):
        return self.top != None and self.top.value or None

    def count(self):
        count = 0
        node = self.top
        while node:
            count += 1
            node = node.next
        return count

    def dump(self):
        node = self.top
        while node:
            print(node)
