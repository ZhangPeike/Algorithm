#include <iostream>
template <typename T> struct Node {
  T data_;
  Node<T> *next_;
  Node() { next_ = nullptr; }
  Node(T t) {
    data_ = t;
    next_ = nullptr;
  }
};

// template <typename T> Node<T> *CreatStack(T data) {
//   // error
//   return &static Node<T>(data);
// };
template <typename T> void Push(Node<T> *&head, T data) {
  Node<T> *p = new Node<T>(data);
  // ERROR
  // head->next_ = p;
  // head = p;
  p->next_ = head;
  head = p;
};
template <typename T> void Pop(Node<T> *&head) {
  if (head) {
    Node<T> *p = head;
    head = head->next_;
    delete p;
  }
};
template <typename T> int Length(Node<T> *head) {
  int count = 0;
  Node<T> *ptr = head;
  while (ptr) {
    count++;
    ptr = ptr->next_;
  }
  return count;
};
template <typename T> T Pick(Node<T> *head) {
  if (Length<T>(head) == 0) {
    return (T)0;
  }
  return head->data_;
};
template <typename T> void Print(Node<T> *head) {
  while (head) {
    std::cout << head->data_ << std::endl;
    head = head->next_;
  }
}

int main() {
  std::cout << "Test single-linked-list stack" << std::endl;
  Node<int> *head = nullptr;
  // Node<int> *head;
  // Node<int> *head = new Node<int>(-1);
  std::cout << "Address: " << head << std::endl;
  Push<int>(head, 7);
  Push<int>(head, 8);
  Push<int>(head, 9);
  Push<int>(head, 1);
  Push<int>(head, 0);
  Node<int> *ptr = head;
  std::cout << "Address of ptr : " << ptr << std::endl;
  std::cout << "Address of head: " << head << std::endl;
  Print<int>(head);
  Pop<int>(head);
  Pop<int>(head);
  Pop<int>(head);
  Pop<int>(head);
  std::cout << "After popping: " << std::endl;
  Print<int>(head);
  return 0;
}