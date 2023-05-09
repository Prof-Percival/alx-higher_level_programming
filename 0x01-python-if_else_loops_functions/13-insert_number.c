#include "lists.h"

/**
 * insert_node - inserts a new node
 * at a given position.
 * @head: head of a list.
 * @number: index of the list where the new node is
 * added.
 * Return: the address of the new node, or NULL if it
 * failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *head_dup;
	listint_t *h_prev;

	head_dup = *head;
	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	while (head_dup != NULL)
	{
		if (head_dup->n > number)
			break;
		h_prev = head_dup;
		head_dup = head_dup->next;
	}

	new->n = number;

	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
	}
	else
	{
		new->next = head_dup;
		if (head_dup == *head)
			*head = new;
		else
			h_prev->next = new;
	}

	return (new);
}
