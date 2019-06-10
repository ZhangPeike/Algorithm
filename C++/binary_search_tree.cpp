// #include "Log/log.hpp"
#include <iostream>
// TODO: 1. 实现BST 2.实现BST的前中后遍历 3. 实现非递归的遍历，提示利用栈
// TODO: 2. 智能指针
// template <typename T>

// class Node {
template <typename T> struct Node {
  // public:
  Node(T t) : data_(t){};
  Node(T t, Node *left, Node *right) {
    this->left_ = left;
    this->right_ = right;
    data_ = t;
  }
  Node *parent_;
  Node *left_;
  Node *right_;
  // private:
  T data_;
};

template <typename T> class BinarySearchTree {
public:
  void Insert(T data) { HelpInsert(root_, data); }
  void Delete() {}
  Node<T> *Search(T data) { return SearchValue(root, data, false); }
  void InOrderTreeWalk() { HelpInOrderTreeWalk(root_); }
  T Maximum() {
    auto x = HelpMaximum(root_);
    if (x) {
      return x->data_;
    } else {
      std::cout << "This is empty tree." << std::endl;
      return T(0);
    }
  }
  T Minimum() {
    auto x = HelpMinimum(root_);
    if (x) {
      return x->data_;
    } else {
      std::cout << "This is empty tree." << std::endl;
      return T(0);
    }
  }
  int NodesCount() { return HelpNodesCount(root_); }
  int Height() { return HelpHeight(root_); }
  void PrintMaxPath() { HelpPrintMaxPath(root_); }

private:
  Node<T> *root_;
  void HelpInOrderTreeWalk(Node<T> *root) {
    if (root != nullptr) {
      HelpInOrderTreeWalk(root->left_);
      // zpk::LOG(root->data_);
      std::cout << root->data_;
      HelpInOrderTreeWalk(root->right_);
    }
  }
  Node<T> *HelpMaximum(Node<T> *root) {
    if (root != nullptr) {
      if (root->right_ != nullptr) {
        return HelpMaximum(root->right);
      } else {
        return root;
      }
    }
  }
  Node<T> *HelpMinimum(Node<T> *root) {
    // Node<T> *root
    while (root->left_) {
      root = root->left;
    }
    return root;
  }
  int HelpNodesCount(Node<T> *root) {
    if (root == nullptr) {
      return 0;
    } else {
      return 1 + HelpNodesCount(root->left_) + HelpNodesCount(root->right_);
    }
  }
  int HelpHeight(Node<T> *root) {
    if (root == nullptr) {
      return 0;
    } else {
      return 1 + max(HelpHeight(root->left_), HelpHeight(root->right_));
    }
  }
  void HelpPrintMaxPath(Node<T> *root) {
    if (!root) {
      return;
    }
    std::cout << root->data_ << " ";
    if (HelpHeight(root->left) > HelpHeight(root->right)) {
      HelpPrintMaxPath(root->left_);
    } else {
      HelpPrintMaxPath(root->right_);
    }
  }
  Node<T> *HelpSuccessor(Node<T> *root) {
    if (root->right_) {
      return HelpMinimum(root->right_);
    } else {
      Node<T> *x = root;
      Node<T> *y = x->parent_;
      while (y &&x = y->right_) {
        x = y;
        y = y->parent_;
      }
      return y;
    }
  }
  Node<T> *HelpPredecessor(Node<T> *root) {
    if (root->left_) {
      return HelpMaximum(root->left_);
    } else {
      Node<T> *x = root;
      Node<T> *y = x->parent_;
      while (y &&x = y->left_) {
        x = y;
        y = y->parent_;
      }
      return y;
    }
  }
  Node<T> *SearchValue(Node<T> *root, T k, bool is_recursive = false) {
    Node<T> *x = root;
    if (is_recursive) {
      if (x == nullptr || k == x->data_) {
        return x;
      } else if (k < x->data_) {
        return SearchValue(x->left_, k, true);
      } else if (k > x - data_) {
        return SearchValue(x->right_, k, true);
      }
    } else {
      while (x && k != x->data_) {
        if (k > x->right_) {
          x = x->left_;
        } else {
          x = x->left_;
        }
      }
      return x;
    }
  }
  void HelpInsert(Node<T> *root, T data) {
    Node<T> *x = root;
    Node<T> *y = x;
    Node<T> *z = new Node<T>(data);
    while (x) {
      y = x;
      if (data < x->data_) {
        x = x->left_;
      } else {
        x = x->right_;
      }
    }
    z->parent_ = y;
    if (!y) {
      root_ = z;
    } else if (z->data_ < y->data_) {
      y->left_ = z;
    } else {
      y->right_ = z;
    }
  }
  // TODO
  void HelpTransplant(Node<T> *root, Node<T> *u, Node<T> *v) {
    if (u->parent_ == nullptr) {
      root = v;
    } else if (u == u->parent_->left_) {
      u->parent_->left_ = v;
    } else {
      u->parent_->right_ = v;
    }
    v->parent_ = u->parent_;
  }
  void HelpDelete(Node<T> *root, Node<T> *z) {
    if (!z->left_) {
      HelpTransplant(root, z, z->right_);
    } else if (!z->right_) {
      HelpTransplant(root, z, z->left_);
    } else {
      // equal y = HelpFindMinimum(z->right_);
      Node<T> *y = HelpSuccessor(z);
      if (y->parent_ != z) {
        HelpTransplant(root, y, y->right_);
        // Wrong
        // z->right_->parent_ = y;
        y->right_ = z->right_;
        y->right_->parent_ = y;
      }
      HelpTransplant(root, z, y);
      y->left_ = z->left_;
      y->left_->parent_ = y;
    }
  }
};

int main() {
  std::cout << "Constructing a BST tree..." << std::endl;
  // zpk::LogInit();
  return 0;
}