bool isPalindrome(struct ListNode* head) {
    struct ListNode *temp = head, *rev = NULL, *newNode, *p;

    while(temp != NULL) {
        newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
        newNode->val = temp->val;
        newNode->next = rev;
        rev = newNode;
        temp = temp->next;
    }

    temp = head;
    p = rev;

    while(temp != NULL) {
        if(temp->val != p->val)
            return false;
        temp = temp->next;
        p = p->next;
    }

    return true;
}