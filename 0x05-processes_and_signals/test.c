#include <stdio.h>
#include <stdlib.h>

extern char **environ;

/**
 * main - Entry point for my program
 * @argc: this is the argument count
 * @argv: this is the argument vector
 *
 * Return: Always Zero
 */
int main(void)
{
	int count;
	char *val;

	count = 0;
	while (environ[count] != NULL)
	{
		printf("[%s] :: ", environ[count]);
		count++;
	}

	putchar('\n');

	val = getenv("SHELL");
	printf("\t\t\nCurrent value of the enviroment variable SHELL is: %s\n", val);

	return (0);
}
