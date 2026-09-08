struct ListNode* removeElements(struct ListNode* head, int val) {
    while (head != NULL && head->val == val) {
        struct ListNode *temp = head;
        head = head->next;
        free(temp);
    }

    struct ListNode *prev = head;

    while (prev != NULL && prev->next != NULL) {
        if (prev->next->val == val) {
            struct ListNode *temp = prev->next;
            prev->next = temp->next;
            free(temp);
        }
        else {
            prev = prev->next;
        }
    }

    return head;
}