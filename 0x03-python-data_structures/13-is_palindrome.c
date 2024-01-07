#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: pointer to the head of listint_t
 * @n: integer to add in listint_t list
 * Return: address of the new element, or NULL if it failed
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
    listint_t *new_node;

    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);
    new_node->n = n;
    new_node->next = *head;
    *head = new_node;
    return (new_node);
}

/**
 * is_palindrome - identify if a single linked list is palindrome
 * @head: pointer to the head of listint_t
 * Return: 1 if it is palindrome else 0
 */
int is_palindrome(listint_t **head)
{
    listint_t *temp_head = *head;
    listint_t *reversed_list = NULL, *temp_list = NULL;

    if (*head == NULL || temp_head->next == NULL)
        return (1);

    while (temp_head != NULL)
    {
        add_nodeint(&reversed_list, temp_head->n);
        temp_head = temp_head->next;
    }

    temp_list = reversed_list;

    while (*head != NULL)
    {
        if ((*head)->n != temp_list->n)
        {
            free_listint(&reversed_list); // Fix: added & before reversed_list
            return (0);
        }
        *head = (*head)->next;
        temp_list = temp_list->next;
    }

    free_listint(&reversed_list);
    return (1);
}
