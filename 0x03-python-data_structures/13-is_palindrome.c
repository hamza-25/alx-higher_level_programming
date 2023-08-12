#include "lists.h"

/**
 * create_node - create node
 * @number: value int to add
 * Return: a struct node
*/

listint_t *create_node(int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	return (new_node);
}

/**
 * duplicate_list - duplicate list
 * @head: head of original list
 * Return: a duplicate list from original
*/

listint_t *duplicate_list(listint_t *head)
{
	listint_t *dup, *c_head, *first_node;

	if (!head)
		return (NULL);
	first_node = create_node(head->n);
	dup = first_node;
	c_head = head->next;
	while (c_head)
	{
		dup->next = create_node(c_head->n);
		dup = dup->next;
		c_head = c_head->next;
	}
	return (first_node);
}

/**
 * is_palindrome - func that check if palindrome
 * @head: head of linked list
 * Return: 1 if palindrome 0 if not
*/

int is_palindrome(listint_t **head)
{
	listint_t *current = *head, *next, *pre = NULL, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	dup = duplicate_list(*head);
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
			return (0);
		current = current->next;
		dup = dup->next;
	}
	return (1);
}
