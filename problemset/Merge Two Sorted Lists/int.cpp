/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
 
class Solution {
public:
    void addNode(ListNode **head,int data)
    {
        ListNode *b = new ListNode;
        b->val = data;
        b->next = *head;
        *head = b;
    }

    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
         ListNode *temp = list1;
        ListNode *newList = NULL;
        ListNode *temp2 = list2;
        if(list1 != NULL && list2 != NULL)
        {
            while(temp != NULL)
            {
                addNode(&newList,temp->val);
                temp = temp->next;
            }
            //merging the two list based in the last element : 
            temp = newList;
            //getting last Node of the merged list :
            while(temp->next != NULL)
                temp = temp->next;
            //connecting the last element with second list : 
            while(temp2 != NULL)
            {
                addNode(&temp->next,temp2->val);
                temp2 = temp2->next;
            }
            //now sorting the list :
            sortList(newList); 
        } else if(list1 == NULL) 
            return list2;
          else return list1;
        return newList;
     }
    void sortList(ListNode* list) 
    {
        ListNode *temp = list;
        ListNode *temp2 = NULL;
        int buffer = 0;
        while(temp != NULL)
        {
            temp2 = temp->next;
            while(temp2 != NULL)
            {
                if(temp->val > temp2->val)
                {
                    buffer = temp2->val;
                    temp2->val = temp->val;
                    temp->val = buffer;
                }
                temp2 = temp2->next;
            }
            temp = temp->next;
        }
    }
};