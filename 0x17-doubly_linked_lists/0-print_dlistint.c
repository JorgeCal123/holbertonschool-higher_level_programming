#include <stddef.h>
#include "lists.h"

/**
 * print_dlistint - function that prints all the elements of a
 * dlistint_t list.
 * @h: type dlistint_t list.
 * Return: the number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *tmp;
        size_t conta = 0;

	tmp = h;

	while(tmp)
	{
		conta++;
		tmp =tmp->next;
	}
	return conta;
}
