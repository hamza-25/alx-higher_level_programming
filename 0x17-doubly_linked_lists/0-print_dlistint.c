#include "lists.h"
/**
 * print_dlistint - print each node
 * @h: head of dlist
 * Return: number of node
*/

size_t print_dlistint(const dlistint_t *h)
{
	int i = 0;
	const dlistint_t *current = h;

	while (current)
	{
		printf("%d\n", current->n);
		current = current->next;
		i++;
	}
	return (i);
}
