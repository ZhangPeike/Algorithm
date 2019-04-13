ListNode* reverseList(ListNode* l) {
        if(l==NULL || l->next==NULL) {
            return l;
        }
        ListNode* p_cur = l->next;
        ListNode* p_prev = l;
        ListNode* p_tmp = l->next->next;
        while(p_cur!=NULL){
          p_tmp = p_cur->next;
          p_cur->next = p_prev;
          p_prev = p_cur;
          p_cur = p_tmp;
        }
        l->next = NULL;
        return p_prev;
      }
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
     unsigned int a = 0; 
     unsigned int b = 0; 
     unsigned int sum = 0; 
     ListNode* l_a = reverseList(l1);
     ListNode* l_b = reverseList(l2);
      while(l_a != NULL) {
        a = a*10 + l_a->val;
        l_a = l_a->next;
      }
      while(l_b != NULL) {
        b = b*10 + l_b->val;
        l_b = l_b->next;
      }
      sum = a + b;
      int top = sum % 10;
      //ListNode* p_result = (ListNode*)malloc(sizeof(ListNode));
      ListNode p_result(top);
      ListNode* p_rear = &p_result;
      sum = sum/10;
      while(sum != 0) {
        p_rear->next = new ListNode(sum%10);
        p_rear = p_rear->next;
        sum = sum/10;
      }
      p_rear->next = NULL;
      return &p_result;
    }
