#include <stddef.h>
#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: is a linked list type listint_t
 * @number: number into a sorted
 * Return: linked list updated
 */
listint_t *insert_node(listint_t **head, int number)
{	
	listint_t *original = *head;
	listint_t *new_n; 
	listint_t *before;
	listint_t *temp_Next;

	new_n = malloc(sizeof(listint_t));
	if (!new_n)
		return (NULL);
	if (*head == NULL)
	{
		new_n->n = number;
		new_n->next = NULL;
		*head = new_n;
		return (new_n);
	}

	while(original)
	{
		if(original->n < number)
			before = original;
	original = original->next; 
	}
	temp_Next = before->next;
	new_n->n = number;
	new_n->next = temp_Next;
	before->next = new_n;

	return(original);
}
