#include "lists.h"

/**
 * is_palindrome - func that check if palindrome
 * @head: head of linked list
 * Return: 1 if palindrome 0 if not
*/

int is_palindrome(listint_t **head)
{
	listint_t *current = *head, *next, *pre = NULL, *dup = NULL, *f;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	dup = duplicate_list(*head);
	f = dup;
	if (!dup)
		return (1);
	while (current)
	{
		next = current->next;
		current->next = pre;
		pre = current;
		current = next;
	}
	*head = pre;
	current = *head;
	while (dup)
	{
		if (current->n != dup->n)
		{
			free_listint(f);
			return (0);
		}
		current = current->next;
		dup = dup->next;
	}
	free_listint(f);
	return (1);
}
