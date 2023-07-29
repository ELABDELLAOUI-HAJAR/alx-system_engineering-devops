#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - create an infinite loop
 * Return: 0 Success
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - the entry point
 * Return: 0 Success
 */

int main(void)
{
	int i;

	for (i = 0; i < 5; i++)
	{
		/* Check if it's the child process */
		if (fork() == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}

	infinite_while();
	return (0);
}
