#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t)), *current = NULL;

	current = *head;
	if (!new)
		return (NULL);
	new->n = number;
	while(!current || current->n >= number)
	{
		new->next = current;
		*head = new;
		return (new);
	}
	while (current->next != NULL && current->next->n < number)
		current = current->next;
	new->next = current->next;
	current->next = new;
	return (new);

}
