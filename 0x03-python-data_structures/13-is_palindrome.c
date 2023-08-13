#include "lists.h"

/**
 * is_palindrome - func that check if palindrome
 * @head: head of linked list
 * Return: 1 if palindrome 0 if not
*/

int is_palindrome(listint_t **head)
{
	listint_t *current = *head, *next, *pre = NULL;
	listint_t *slow = *head, *fast = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	while (slow)
	{
		next = slow->next;
		slow->next = pre;
		pre = slow;
		slow = next;
	}
	slow = pre;
	current = *head;
	while (current && slow)
	{
		if (current->n != slow->n)
		{
			return (0);
		}
		current = current->next;
		slow = slow->next;
	}
	return (1);
}
