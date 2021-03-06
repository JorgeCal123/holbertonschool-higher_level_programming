#include "lists.h"
/**
 * check_cycle - check if a loop exists within a linked list
 * @list: linked list type listint_t to check
 * Return: 1 if exist loop and if not exist loop
 */
int check_cycle(listint_t *list)
{
	listint_t *copy = list;

	if (list == NULL)
		return (0);

	copy = copy->next;
	while (copy && copy->next)
	{
		copy = copy->next;
		if (list->n == copy->n)
		{

			return (1);
		}
	}
	return (0);
}
