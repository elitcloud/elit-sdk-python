# ========================================================================
# Copyright 2018 Emory University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ========================================================================
import itertools

__author__ = "Gary Lai"


class Node(object):

    def __init__(self):
        self._parent = None
        self._left_sibling = None
        self._right_sibling = None
        self._children = []

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        if not isinstance(node, Node):
            raise ValueError('parent must be an Node')
        if self.has_parent():
            # not sure what's going on here?
            self.parent.remove_child(self)
        else:
            node.add_child(self)

    @property
    def left_sibling(self):
        return self._left_sibling

    @left_sibling.setter
    def left_sibling(self, node):
        if not isinstance(node, Node):
            raise ValueError('sibling must be an Node')
        if node is not None:
            self._left_sibling = node

    @property
    def right_sibling(self):
        return self.right_sibling

    @right_sibling.setter
    def right_sibling(self, node):
        if not isinstance(node, Node):
            raise ValueError('sibling must be an Node')
        if node is not None:
            self._right_sibling = node

    @property
    def children(self):
        return self._children

    def index_of(self, child):
        try:
            return self.children.index(child)
        except ValueError:
            return None

    # Child

    def child(self, index):
        try:
            return self.children[index]
        except IndexError:
            return None

    def first_child(self):
        # return self.child(0)
        return self.find_child_by(index=0)

    def last_child(self):
        # return self.child(-1)
        return self.find_child_by(index=-1)

    def find_child_by(self, matcher=lambda n: n, index=0):
        return self.find_children_by(matcher)[index]

    def add_child(self, node, index=None):
        if index is None:
            index = self.index_of(node)
        if self.is_parent_of(node):
            return False
        else:
            if node.has_parent():
                node.parent.remove_child(node)
            node.parent = self
            self.children.insert(index, node)
            self._siblings(self.child(index - 1), node)
            self._siblings(node, self.child(index + 1))
            return True

    def set_child(self, node, index):
        if not self.is_parent_of(node):
            if node.has_parent():
                node.parent.remove_child(node)
            node.parent = self
            old_node = self.children[index]
            self.children[index] = node
            self._siblings(self.child(index - 1), node)
            self._siblings(node, self.child(index + 1))
            old_node.isolate()
            return old_node
        else:
            return None

    def remove_child(self, node):
        index = self.index_of(node)
        if index is not None:
            self._siblings(self.child(index - 1), self.child(index + 1))
            self.children.remove(node)  #
            node.isolate()  # is isolation necessary ?
            return True
        else:
            return False

    def replace_child_from(self, old_node, new_node):
        index = self.index_of(old_node)
        if index is not None:
            self.children[index] = new_node
            self._siblings(self.child(index - 1), new_node)
            self._siblings(new_node, self.child(index + 1))
            old_node.isolate()
            return True
        else:
            return False

    def remove(self):
        node = self
        while node.has_parent():
            parent = node.parent
            parent.remove_child(node)
            if parent.has_child():
                break
            node = parent

    def has_child(self):
        return True if self.children else False

    def is_child_of(self, node):
        return node is not None and self.parent is node

    def contains_child(self, matcher=lambda n: n):
        return True if list(filter(matcher, self.children)) else False

    # Descendants

    def num_of_children(self):
        return len(self.children)

    def find_children_in(self, first_child_index=0, last_child_index=None):
        return self.children[first_child_index:last_child_index]

    def find_children_by(self, matcher=lambda n: n):
        return list(filter(matcher, self.children))

    def grand_children(self):
        return self.second_order('children')

    def find_first_descendant_by(self, matcher=lambda n: True):
        for node in self.children:
            if matcher(node):
                return node

            node = self.find_first_descendant_by(node.children, matcher)
            if node is not None:
                return node
        return None

    def find_first_lowest_chained_descendant_by(self, matcher):
        node = self.find_child_by(matcher)
        descendant = None

        while node is not None:
            descendant = node
            node = node.find_child_by(matcher)

        return descendant

    def descendants(self):
        result = []
        if not self.has_child():
            return [self]
        else:
            for child in self.children:
                result = result + child.descendants
            return result

    def find_descendants_in(self, depth):
        result = []
        if depth <= 0:
            return result
        else:
            for child in self.children:
                result = result + child.find_descendants_in(depth - 1)
            return result

    def find_single_chained_by(self, matcher=lambda n: True):
        node = self
        while node is not None:
            if matcher(node):
                return node
            if node.num_of_children() is 1:
                node = node.first_child()
            else:
                break
        return None

    def adapt_descendants_from(self, node):
        for child in node.children:
            child.parent = self

    def is_descendants_of(self, node):
        return self.find_nearest_node_by(
            getter='parent', matcher=lambda n: n is node) is not None

    # Ancestors

    def grand_parent(self):
        return self.ancestor(height=2)

    def ancestor(self, height):
        return self.find_node_in(order=height, getter='parent')

    def find_lowest_ancestor_by(self, matcher=lambda n: True):
        return self.find_nearest_node_by('parent', matcher)

    def find_highest_ancestor_by(self, matcher=lambda n: True):
        node = self.parent
        ancestor = None
        while node is not None:
            if matcher(node):
                ancestor = node
            else:
                break
            node = node.parent
        return ancestor

    def lowest_common_ancestor(self, node):
        ancestor_set = self.ancestor_set()
        ancestor_set.add(self)

        while node is not None:
            if node in ancestor_set:
                return node
            node = node.parent

        return None

    def ancestor_set(self):
        ancestor_set = set()
        node = self.parent
        while node is not Node:
            ancestor_set.add(node)
            node = node.parent
        return ancestor_set

    def is_parent_of(self, node):
        return node.is_child_of(self)

    def is_ancestor_of(self, node):
        return node.is_descendants_of(self)

    def has_parent(self, matcher=lambda n: True):
        return self.parent is not None and matcher(self)

    def has_grand_parent(self):
        return self.grand_parent() is not None

    # Siblings

    def siblings(self):
        return list(
            filter(
                lambda child: child is not self,
                self.parent.children)) if self.has_parent() else []

    def left_nearest_sibling(self, order=0):
        return self.find_node_in(
            order + 1, 'left_sibling') if order >= 0 else None

    def find_left_nearest_sibling_by(self, matcher=lambda x: True):
        return self.find_nearest_node_by('left_sibling', matcher)

    def right_nearest_sibling(self, order=0):
        return self.find_node_in(
            order + 1, 'right_sibling') if order >= 0 else None

    def find_right_nearest_sibling_by(self, matcher=lambda x: True):
        return self.find_nearest_node_by('right_sibling', matcher)

    def has_left_sibling(self, matcher=lambda x: True):
        return self.left_sibling is not None or self.find_left_nearest_sibling_by(
            matcher)

    def has_right_sibling(self, matcher=lambda x: True):
        return self.right_sibling is not None or self.find_right_nearest_sibling_by(
            matcher)

    def is_sibling_of(self, node):
        return node.is_child_of(self.parent)

    def is_left_sibling_of(self, node):
        return node is not None and self.parent is node.parent and self.find_nearest_node_by(
            'right_sibling', lambda n: n is node) is not None

    def is_right_sibling_of(self, node):
        return node.is_left_sibling_of(self)

    # Helpers

    def find_node_in(self, order, getter):
        node = self
        for _ in range(order):
            if node is None:
                return None
            node = getattr(node, getter)
        return node

    def find_nearest_node_by(self, getter, matcher=lambda n: True):
        node = getattr(self, getter)

        while node is not None:
            if matcher(node):
                return node
            node = getattr(node, getter)
        return None

    def isolate(self):
        self._parent = None
        self._left_sibling = None
        self._right_sibling = None

    def second_order(self, getter):
        return list(
            itertools.chain.from_iterable(
                list(
                    filter(
                        lambda n: getattr(
                            n, getter) if n is not self else None, getattr(
                            self, getter)))))

    def _siblings(self, left_node, right_node):
        right_node.left_sibling = left_node
        left_node.right_sibling = right_node


class NLPNode(Node):
    pass
