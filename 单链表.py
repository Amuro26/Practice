# -*- coding: utf-8 -*-


# 节点类，每一个节点由表元素域(elem)和下一节点链接域(next_)组成
class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LinkedListUnderflow(ValueError):
    pass


class LList:
    _num = 0

    @classmethod
    def get_num(cls):
        return cls._num

    def __init__(self):
        self._head = None
        LList._num += 1

    def is_empty(self):
        return self._head is None

    # 在表的前端进行操作
    def prepend(self, elem):  # 在表头添加，新增一个节点，元素是elem(也是现在的表头)，链接到之前的头_head
        self._head = LNode(elem, self._head)
        LList._num += 1

    def pop(self):
        if not self._head:
            raise LinkedListUnderflow("in pop")
        e_pop = self._head.elem
        self._head = self._head.next
        LList._num -= 1
        print('{} has been deleted.'.format(e_pop))

    # 在表的后端进行操作
    def append(self, elem):
        if not self._head:  # 判断当前节点是不是最后节点，如果是，直接添加
            self._head = LNode(elem)
            return
        p = self._head  # 如果不是，循环到最后一个节点
        while p.next:
            p = p.next
        p.next = LNode(elem)
        LList._num += 1

    def pop_last(self):
        if not self._head:  # 如果当前节点为空，则是空表，无法进行删除操作
            raise LinkedListUnderflow
        p = self._head
        if p.next is None:  # 如果表中只有一个元素，删除当前元素
            e = p.elem
            self._head = None
            print('{} has been deleted.'.format(e))
        while p.next.next is not None:  # 如果表中有多个元素，循环到倒数第二个元素（即p.next是末尾元素）
            p = p.next
        e = p.next.elem  # 删掉的e是最后的元素
        p.next = None  # 将最后一个节点归空
        LList._num -= 1
        print('{} has been deleted.'.format(e))

    def find(self, pred):
        p = self._head
        while p:  # 往后循环
            if pred(p.elem):
                return p.elem
            p = p.next

    def print_all(self):
        p = self._head
        while p:
            print(p.elem, end='')
            if p.next:
                print(', ', end='')
            p = p.next
        print(' END')
        print(' %s elements in total.' % LList._num)

    def delete(self, index):
        try:
            ind = int(index)
            if LList._num <= ind:
                raise LinkedListUnderflow("Index is beyond the LList.", ind)
            elif ind < 0:
                raise LinkedListUnderflow("Index is a negative int.", ind)
        except:
            raise LinkedListUnderflow("Index is not an int.", index)
        p = self._head
        while ind > 0:
            ind -= 1
            p = p.next
        e = p.elem
        p.elem = None
        LList._num -= 1
        print('{} has been deleted.'.format(e))


class DLnode(LNode):
    def __init__(self, elem, prev=None, next_=None):
        LNode.__init__(self, elem, next_)
        self.prev = prev



'''
mlist1 = LList()
for i in range(10):
    mlist1.prepend(i)
mlist1.print_all()
for i in range(11, 30):
    mlist1.append(i)
mlist1.print_all()
mlist1.pop()
mlist1.print_all()
mlist1.pop_last()
mlist1.print_all()
mlist1.delete(0)
mlist1.delete(mlist1.get_num()-1)
mlist1.delete(-2)
'''



