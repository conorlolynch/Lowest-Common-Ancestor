
class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def addChild(self, value):
        if (value < self.value):
            if (self.left != None):
                self.left.addChild(value)
            else:
                new_node = node(value)
                self.left = new_node
            return True

        elif (value > self.value):
            if (self.right != None):
                self.right.addChild(value)
            else:
                new_node = node(value)
                self.right = new_node
            return True

        else:
            # We dont add duplicates
            return False


class BT:
    def __init__(self):
        self.number_items = 0
        self.root = None

    def addHead(self, value):
        self.root = node(value)
        self.number_items += 1

    def addValue(self, value):
        if (self.root == None):
            self.addHead(value)
        else:
            if (self.root.addChild(value)):
                self.number_items += 1

    def printBT(self):
        root = self.root
        left = self.root.left
        right = self.root.right

        print(root)
        print(left)
        print(right)



bt = BT()
bt.addValue(2)
bt.addValue(1)
bt.addValue(3)

bt.printBT()
