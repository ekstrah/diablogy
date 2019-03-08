#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>


int main() {

	int fd = open("./man.log", O_WRONLY|O_CREAT,0640);
	write(fd, "hi\n", 3);
	close(fd);
	return 0;
}
