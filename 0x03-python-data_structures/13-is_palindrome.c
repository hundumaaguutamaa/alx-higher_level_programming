#include "lists.h"
/*
 * is_palindrome - Checks if a linked list is palindrome.
 * @head: pointer to head of a list.
 * Return: 1 if it's palindrome, 0 if not.
 *
 */
int is_palindrome(listint_t **head)
{
	int array[2048];
	int no_dos = 0;
	int x = 0;

	if (*head == NULL || head == NULL)
		return (1);

	while (*head != NULL)
	{
		no_dos++;
		array[no_dos - 1] = (*head)->n;
		*head = (*head)->next;
	}

	for (x = 0; x < no_dos / 2; x++)
	{
		if (array[x != array[no_dos - x - 1])
		{
			return (0);
		}
	}

	return (1);
}
