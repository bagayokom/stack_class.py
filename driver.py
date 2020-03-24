from stack_code import *

# Stack Driver

def test_push():
    colors = Stack()
    colors.push("Hot dog")
    assert colors.count() == 1
    colors.push("Banana")
    assert colors.count() == 2

def test_pop():
    colors = Stack()
    colors.push("Rose")
    colors.push("Violet")
    assert colors.pop() == "Rose"
    assert colors.pop() == "Violet"
    assert colors.pop() == None

def test_top():
    colors = Stack()
    colors.push("Couch")
    assert colors.first() == "Couch"
    colors.push("Table")
    assert colors.first() == "Table"
    colors.push("Desk")
    assert colors.first() == "Desk"

