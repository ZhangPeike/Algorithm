// TODO: replace new with shared_ptr
#include <iostream>
#include <queue>
template <class T> class PK_Queue;
template <typename T> class PK_Node {
public:
  friend PK_Queue<T>;
  PK_Node() { next_ = nullptr; }
  PK_Node(T t) {
    data_ = t;
    next_ = nullptr;
  }

private:
  T data_;
  PK_Node<T> *next_;
};

// tail is the rear, remember the first in the queue is 0.
template <typename T> class PK_Queue {
public:
  PK_Queue() {
    tail_ = new PK_Node<T>();
    tail_->next_ = tail_;
  }
  // Get the front value
  T Front() const {
    if (Empty()) {
      std::cout << "Queue is empty.\n";
      return T(0);
    } else {
      return tail_->next_->next_->data_;
    }
  }
  bool Empty() const { return (tail_->next_ == tail_); }
  void Push(T t) {
    PK_Node<T> *p = new PK_Node<T>(t);
    p->next_ = tail_->next_;
    tail_->next_ = p;
    tail_ = p;
  }
  // Pop the front
  void Pop() {
    if (Empty()) {
      return;
    }
    PK_Node<T> *p = tail_->next_;
    PK_Node<T> *q = p->next_;
    p->next_ = q->next_;
    // for queue only has two value, tail is in the head, so removed.
    if (tail_ == q) {
      tail_ = p;
    }
    delete q;
  }

private:
  PK_Node<T> *tail_;
};

template <typename T> class ChildSiblingTree;

template <typename T> class ChildSiblingNode {
private:
  T data_;
  ChildSiblingNode<T> *ptr_left_first_child_;
  ChildSiblingNode<T> *ptr_right_next_sibling_;
  friend ChildSiblingTree<T>;
};
template <typename T> class ChildSiblingTree {
public:
  // root: created tree's root node.
  void Creat(ChildSiblingNode<T> *&root) {
    PK_Queue<ChildSiblingNode<T> *> queue_nodes;
    std::cout << "Input parent child pair, '#''#' means finish." << std::endl;
    T parent, child;
    for (std::cin >> parent >> child; (char)child != '#';
         std::cin >> parent >> child) {
      static int count = 0;
      ChildSiblingNode<T> *p = new ChildSiblingNode<T>();
      p->data_ = child;
      p->ptr_left_first_child_ = p->ptr_right_next_sibling_ = nullptr;
      queue_nodes.Push(p);
      std::cout << "Queue has pushed " << ++count << "times." << std::endl;
      if ((char)parent == '#') {
        root = p;
      } else {
        ChildSiblingNode<T> *r;
        std::cout << "r address: " << r << std::endl;
        ChildSiblingNode<T> *s = queue_nodes.Front();
        static int count_pop = 0;
        while (s->data_ != parent) {
          std::cout << "Queue has poped" << ++count_pop << "times."
                    << std::endl;
          queue_nodes.Pop();
          s = queue_nodes.Front();
        }
        if (!s->ptr_left_first_child_) {
          s->ptr_left_first_child_ = p;
          r = p;
        } else {
          // r in every loop is not initialized.
          r->ptr_right_next_sibling_ = p;
          r = p;
        }
      }
    }
  }
  //   https://blog.csdn.net/jkay_wong/article/details/6635984
  void Print(){};

private:
};

int main() {
  std::cout << "Test PK_Queue: \n";
  PK_Queue<int> my_queue;
  my_queue.Push(7);
  my_queue.Push(6);
  my_queue.Push(5);
  my_queue.Push(4);
  my_queue.Push(3);
  while (!my_queue.Empty()) {
    std::cout << "Head: " << my_queue.Front() << std::endl;
    my_queue.Pop();
  }
  if (my_queue.Empty()) {
    std::cout << "is empty.\n";
  }
  std::cout << "Front value: " << my_queue.Front() << std::endl;
  my_queue.Pop();
  if (my_queue.Empty()) {
    std::cout << "After pop, it is empty.\n";
  }
  ChildSiblingTree<char> test_cstree;
  ChildSiblingNode<char> *root;
  test_cstree.Creat(root);
  return 0;
}