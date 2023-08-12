#include "lists.h"

/**
 * is_palindrome - func that check if palindrome
 * @head: head of linked list
 * Return: 1 if palindrome 0 if not
*/

int is_palindrome(listint_t **head)
{
	listint_t *current = *head, *next, *pre = NULL, *rev;

	while (current)
	{
		next = current->next;
		current->next = pre;
		pre = current;
		current = next;
	}
	rev = pre;
	current = *head;
	while (current)
	{
		if (current->n != rev->n)
			return (0);
		current = current->next;
		rev = rev->next;
	}
	return (1);
}
