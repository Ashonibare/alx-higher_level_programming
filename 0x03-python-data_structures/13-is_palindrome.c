#include "lists.h"
#include <stdio.h>

/* Function prototypes */
void reverse(listint_t **head);
int compare_lists(listint_t *head, listint_t *middle, int len);

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
    int len, i;
    listint_t *tmp;
    listint_t *middle;

    if (head == NULL || *head == NULL)
        return (1);

    tmp = *head;
    middle = *head;

    // Calculate the length of the list
    for (len = 0; tmp != NULL; len++)
        tmp = tmp->next;

    len = len / 2;

    // Move middle to the middle of the list
    for (i = 0; i < len; i++)
        middle = middle->next;

    // If the length is odd, move middle one step further
    if (len % 2 != 0)
    {
        middle = middle->next;
        len = len - 1;
    }

    // Reverse the second half of the list
    reverse(&middle);

    // Compare the two halves
    i = compare_lists(*head, middle, len);

    return (i);
}

/**
 * compare_lists - Compares two halves of a list to check for palindrome.
 * @head: The start of the first half of the list.
 * @middle: The start of the reversed second half of the list.
 * @len: The length of the list to compare.
 *
 * Return: 1 if the lists are the same, 0 otherwise.
 */
int compare_lists(listint_t *head, listint_t *middle, int len)
{
    int i;

    if (head == NULL || middle == NULL)
        return (1);

    for (i = 0; i < len; i++)
    {
        if (head->n != middle->n)
            return (0);
        head = head->next;
        middle = middle->next;
    }
    return (1);
}

/**
 * reverse - Reverses a singly linked list.
 * @head: A pointer to the pointer to the head of the list.
 */
void reverse(listint_t **head)
{
    listint_t *current;
    listint_t *next;
    listint_t *prev;

    if (head == NULL || *head == NULL)
        return;

    prev = NULL;
    current = *head;
    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    *head = prev;
}
