struct ListNode* removeElements(struct ListNode* head, int val) {
    struct ListNode dummy;
    dummy.next = head;

    struct ListNode *prev = &dummy;

    while (prev->next != NULL) {
        if (prev->next->val == val) {
            struct ListNode *temp = prev->next;
            prev->next = temp->next;
            free(temp);
        }
        else {
            prev = prev->next;
        }
    }

    return dummy.next;
}