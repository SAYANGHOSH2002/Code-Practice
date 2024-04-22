#include<stdio.h>
#include<conio.h>
#include<stdlib.h>

struct Linked_list
{
    int data;
    struct Linked_list *next;
};

struct Linked_list *head = NULL;
typedef struct Linked_list *new;

new createNode(){
    new node;
    node = malloc(sizeof(struct Linked_list));
    node->next = NULL;
    return node;
}

void createList(){    
    
    int i, n, val;
    new temp, p;
    printf("Enter how many elements do you need to insert: ");
    scanf("%d",&n);
    printf("\nEnter the elements: \n");
    
    for(i=0;i<n;i++){
        scanf("%d",&val);
        temp = createNode();
        temp->data = val;
        
        if(head == NULL){
            head = temp;
        }
        
        else{
            p = createNode();
            p = head;
            while(p->next != NULL){
                p = p->next;
            }
            p->next = temp;
        }
    }

}

void insert_at_begin(){
    
    new temp;
    int val;
    temp = createNode();
    
    printf("\nEnter the value: ");
    scanf("%d",&val);
    
    temp->data = val;
    temp->next = head;
    head = temp;
    
}

void insert_at_end(){
    
    new temp, p;
    int val;
    temp = createNode();
    
    printf("\nEnter the value: ");
    scanf("%d",&val);
    
    temp->data = val;
    
    p = createNode();
    p = head;
    while(p->next != NULL){
        p = p->next;
    }
    p->next = temp;
    
}

void insert_at_mid(){
    
    new temp, p;
    int i, val, n;
    temp = createNode();
    
    printf("\nEnter the position: ");
    scanf("%d",&n);
    printf("\nEnter the value: ");
    scanf("%d",&val);
    
    temp->data = val;
    
    p = createNode();
    p = head;
    for (i = 0; i < (n-2); i++){
        p = p->next;
    }
    temp->next = p->next;
    p->next = temp;
    
}

void delete_from_begin(){
    head = head->next;
    printf("\nElement Deleted");
}

void delete_from_end(){
    new p;
    p = createNode();
    p = head;
    while((p->next)->next != NULL){
        p = p->next;
    }
    p->next = NULL;
    printf("\nElement Deleted");
}

void delete_from_mid(){
    new p;
    int n, i;
    printf("\nEnter the position: ");
    scanf("%d",&n);
    
    p = createNode();
    p = head;
    for (i = 0; i < (n-2); i++){
        p = p->next;
    }
    p->next = (p->next)->next;
    printf("\nElement Deleted");
    
}

void display(){
    struct Linked_list *list = malloc(sizeof(struct Linked_list));
    list = head;
    printf("\nYour list is: ");
    while(list !=NULL){
        printf("%d ", list->data);
        list = list->next;
    }
}

int main()
{
    createList();
    int c;
    while(1){
        printf("\nPress the numbers: \n1. Insert at Begining\n2. Insert at End\n3. Insert at Middle\n4. Delete from Begining\n5. Delete from End\n6. Delete from Middle\n7. Display the Linked List\n8. Exit\n");
        scanf("%d",&c);
        switch(c){
            case 1:
                insert_at_begin();
                break;
            case 2:
                insert_at_end();
                break;
            case 3:
                insert_at_mid();
                break;
            case 4:
                delete_from_begin();
                break;
            case 5:
                delete_from_end();
                break;
            case 6:
                delete_from_mid();
                break;
            case 7:
                display();
                break;
            case 8:
                exit(0);
            default:
                printf("\nInvalid Choice, Try Again !!");
                break;
        }
    }
    
    return 0;
}
