#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - Reverses a singly linked list
 * @head: Pointer to the first node of the list
 *
 * Return: Pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
    }

    return (prev);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Double pointer to the head of the linked list
 *
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head;
    listint_t *first_half_end = NULL, *second_half_start = NULL;
    listint_t *first_half_start, *second_half_copy;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (fast != NULL && fast->next != NULL)
    {
        first_half_end = slow;
        slow = slow->next;
        fast = fast->next->next;
    }

    second_half_start = reverse_list(slow);

    first_half_start = *head;
    second_half_copy = second_half_start;

    while (second_half_start != NULL)
    {
        if (first_half_start->n != second_half_start->n)
        {
            reverse_list(second_half_copy);
            return (0);
        }
        first_half_start = first_half_start->next;
        second
