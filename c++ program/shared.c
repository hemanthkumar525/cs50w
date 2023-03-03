#include<sys/types.h>
#include<sys/ipc.h>17-01-23 22:12
#include<sys/shm.h>
#include<unistd.h>
#include<errno.h>
int main()
{
pid_t pid;
int *shared;
int shmid;
shmid=shmget(IPC_PRIVATE,sizeof(int),IPC_CREAT | 0666);
printf("shared MemoryId=%u",shmid);
if(fork()==0)
{
shared=shmat(shmid,(void*)0,0);
printf("Child Pointer=%u\n", shared);
*shared=1;
printf("Child Value=%d\n",*shared);
sleep(2);
printf("Child value=%d\n",*shared);
}
else
{

shared=shmat(shmid,(void*)0,0);
printf("Parent Pointer %u\n",shared);
printf("Parent value=%d\n", *shared);
sleep(1);
*shared=42;
printf("parent value=%d\n", *shared);
sleep(5);
shmctl(shmid, IPC_RMID, 0);
}
}
