#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has
 * a cycle in it
 * @list: pointer to the list
 * Return: 0 if there is no cycle,
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *present;
	listint_t *previous;

	present = list;
	previous = list;
	while (list && present && present->next)
	{
		list = list->next;
		present = present->next->next;

		if (list == present)
		{
			list = previous;
			previous =  present;
			while (1)
			{
				present = previous;
				while (present->next != list && present->next != previous)
				{
					present = present->next;
				}
				if (present->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
