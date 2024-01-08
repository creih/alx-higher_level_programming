#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of the list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *second_half, *prev_slow = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}
	if (fast != NULL)
		slow = slow->next;
	second_half = reverse_list(slow);
	slow = *head;
	while (second_half != NULL)
	{
		if (second_half->n != slow->n)
			return (0);
		second_half = second_half->next;
		slow = slow->next;
	}
	return (1);
}
