#include <stdio.h>
#include <stdlib.h>

typedef struct listNode* listPointer;
typedef struct listNode {
    int data;
    listPointer link;
}listNode;

void printList(listNode *first);
void insert(listNode *first, int data);

/**
 * main -Entry point for program
 *
 * Return: On success, it returns 0. On error, it returns 1.
 */
int main(void)
{
	FILE *fp;
	int n;
	listNode *first = NULL;

	fp = fopen("in.txt", "r");
	if (fp == NULL)
	{
		fprintf(stderr, "Error: cannot open file");
		exit(EXIT_FAILURE);
	}

	while (fscanf(fp, "%d", &n) == 1)
	{
		insert(first, n);
	}

	printList(first);
	exit(EXIT_SUCCESS);
}

void insert(listNode *first, int data)
{
	listNode *temp;

	temp = malloc(sizeof(listNode));
	temp->data = data;
	temp->link = first;
	first = temp;
}

void printList(listNode *first)
{
	while (first)
	{
		fprintf(stdin, "%d", first->data);
		first = first->link;
	}
	putchar('\n');
}
