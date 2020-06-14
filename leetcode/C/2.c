/**
*
* I AM UGLY CODE
*
*/


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

#include <stdlib.h>

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode *head, *tail, *tmp;
    int i = 0;

    head = tail = NULL;
    // tmp = malloc(sizeof(struct ListNode), 1);

    for (;l1 != NULL && l2 != NULL; l1=l1->next, l2=l2->next) {
        tmp = (struct ListNode*)malloc(sizeof(struct ListNode));
        tmp->next = NULL;

        tmp->val = (l1->val + l2->val + i) % 10;
        i = (l1->val + l2->val + i) / 10;
        
        if (tail) {
            tail->next = tmp;
            tail = tmp;
        } else {
            head = tail = tmp;
        }
    }

    if (l1 != NULL) {
        for (;l1 != NULL; l1=l1->next) {
            tmp = (struct ListNode*)malloc(sizeof(struct ListNode));
            tmp -> next = NULL;
            tmp->val = (l1->val + i) % 10;
            i = (l1->val + i) / 10;
            if (tail) {
                tail->next = tmp;
                tail = tmp;
            } else {
                head=tail = tmp;
            }
        }
    }

    if (l2 != NULL) {
        for (;l2 != NULL; l2=l2->next) {
            tmp = (struct ListNode*)malloc(sizeof(struct ListNode));
            tmp -> next = NULL;
            tmp->val = (l2->val + i) % 10;
            i = (l2->val + i) / 10;
            if (tail) {
                tail->next = tmp;
                tail = tmp;
            } else {
                head=tail = tmp;
            }
        }
    }

    if (i) {
        tmp = (struct ListNode*)malloc(sizeof(struct ListNode));
        tmp->next = NULL;
        tmp->val = i;
        if (tail) {
            tail->next = tmp;
            tail = tmp;
        } else {
            head = tail = tmp;
        }
    }

    return head;
}
