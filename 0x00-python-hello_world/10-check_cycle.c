#include "lists.h"

/**
 * check_cycle - function that check if there is infinite loop
 * @list: head of node
 * Return: 0 if no node and 1 if there is
*/

int check_cycle(listint_t *list)
{
	listint_t *one_step = list;
	listint_t *two_step = list;

	while (two_step && one_step && two_step->next)
	{
		one_step = one_step->next;
		two_step = two_step->next->next;
		if (one_step == two_step)
			return (1);
	}
	return (0);
}
