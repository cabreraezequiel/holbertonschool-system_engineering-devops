#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

/**
 * infinite_while - sleeps infinitely
 *
 * Return: 0
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
 * main - creates 5 zombie processes
 */

int main(void)
{
	int i = 0, pid;
	pid_t my_pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
		{
			my_pid = getpid();
			printf("Zombie process created, PID: %u\n", my_pid);
			return (0);
		}
	}
	infinite_while();
	return (0);
}
