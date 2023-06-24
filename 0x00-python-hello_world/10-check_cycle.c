#include "lists.h"

/**
 * check_cycle - checks in cycle of singly linked list.
 * @list:  singly linked list item. 
 * Return: 0 if there is no cycle,else 1. 
 */
int check_cycle(listint_t *list)
{
	listint_t *currentl = list;
	listint_t *temp = list;

	if (!list)
	{
		return (0);
	}

	while (temp != NULL && temp->next != NULL)
	{
		currentl = currentl->next;
		temp = temp->next->next;

		if (currentl == temp)
		{
			return (1);
		}
	}

	return (0);
}
