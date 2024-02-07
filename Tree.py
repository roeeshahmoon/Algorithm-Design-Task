from collections import deque

class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Queue:

    def __init__(self):
        self.q = deque()

    def enq(self, value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)

    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"


class Tree:

    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq((node, level))
        while (len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append(("<empty>", level))
                continue
            visit_order.append((node, level))
            if node.has_left_child():
                q.enq((node.get_left_child(), level + 1))
            else:
                q.enq((None, level + 1))

            if node.has_right_child():
                q.enq((node.get_right_child(), level + 1))
            else:
                q.enq((None, level + 1))

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level

        return s


def inorder_traversal(root, lst_res: []):
    if root:
        inorder_traversal(root.left, lst_res)
        lst_res.append(root.value)
        inorder_traversal(root.right, lst_res)


def preorder_traversal(root, lst_res: []):
    if root:
        lst_res.append(root.value)
        preorder_traversal(root.left, lst_res)
        preorder_traversal(root.right, lst_res)


def return_frequency(data):
    # Take a string and determine the relevant frequencies of the characters
    frequency = {}
    for char in data:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    lst = [(v, k) for k, v in frequency.items()]
    # Build and sort a list of tuples from lowest to highest frequencies
    lst.sort(reverse=True)
    return lst

def Build_Tree_Traversal(inorder, preorder):
    if not preorder or not inorder:
        return None

    root_val = preorder.pop(0)
    root = Node(root_val)
    root_idx = inorder.index(root_val)

    root.left = Build_Tree_Traversal(inorder[:root_idx], preorder[:root_idx])
    root.right = Build_Tree_Traversal(inorder[root_idx + 1:], preorder[root_idx:])

    return root

def inorder_traversal(root, lst_res: []):
    if root:
        inorder_traversal(root.left, lst_res)
        lst_res.append(root.value)
        inorder_traversal(root.right, lst_res)


def preorder_traversal(root, lst_res: []):
    if root:
        lst_res.append(root.value)
        preorder_traversal(root.left, lst_res)
        preorder_traversal(root.right, lst_res)

root = Node(5)
root.left = Node(6)
root.right = Node(12)
root.right.left = Node(11)
root.right.right = Node(4)
root.left.left = Node(2)
root.left.right = Node(1)

lst_inorder = []
lst_preorder = []
inorder_traversal(root, lst_inorder)
tree = Tree()
tree.root = root
print('lst_inorder: ', lst_inorder, '\n')

preorder_traversal(root, lst_preorder)
print("lst_preorder: ", lst_preorder, '\n')

root = Build_Tree_Traversal(lst_inorder, lst_preorder)

tree = Tree()
tree.root = root

print(tree)
