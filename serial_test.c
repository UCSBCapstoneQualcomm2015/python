#include <errno.h>
#include <termios.h>
#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>

int
set_interface_attribs (int fd, int speed, int parity)
{
        struct termios tty;
        memset (&tty, 0, sizeof tty);
        if (tcgetattr (fd, &tty) != 0)
        {
                printf ("error %d from tcgetattr", errno);
                return -1;
        }

        cfsetospeed (&tty, speed);
        cfsetispeed (&tty, speed);

        tty.c_cflag = (tty.c_cflag & ~CSIZE) | CS8;     // 8-bit chars
        // disable IGNBRK for mismatched speed tests; otherwise receive break
        // as \000 chars
        tty.c_iflag &= ~IGNBRK;         // disable break processing
        tty.c_lflag = 0;                // no signaling chars, no echo,
                                        // no canonical processing
        tty.c_oflag = 0;                // no remapping, no delays
        tty.c_cc[VMIN]  = 0;            // read doesn't block
        tty.c_cc[VTIME] = 5;            // 0.5 seconds read timeout

        tty.c_iflag &= ~(IXON | IXOFF | IXANY); // shut off xon/xoff ctrl

        tty.c_cflag |= (CLOCAL | CREAD);// ignore modem controls,
                                        // enable reading
        tty.c_cflag &= ~(PARENB | PARODD);      // shut off parity
        tty.c_cflag |= parity;
        tty.c_cflag &= ~CSTOPB;
        tty.c_cflag &= ~CRTSCTS;

        if (tcsetattr (fd, TCSANOW, &tty) != 0)
        {
                printf ("error %d from tcsetattr", errno);
                return -1;
        }
        return 0;
}

void
set_blocking (int fd, int should_block)
{
        struct termios tty;
        memset (&tty, 0, sizeof tty);
        if (tcgetattr (fd, &tty) != 0)
        {
                printf ("error %d from tggetattr", errno);
                return;
        }

        tty.c_cc[VMIN]  = should_block ? 1 : 0;
        tty.c_cc[VTIME] = 5;            // 0.5 seconds read timeout

        if (tcsetattr (fd, TCSANOW, &tty) != 0)
                printf ("error %d setting term attributes", errno);
}


int main(int argc, char ** argv)
{
	char *portname = "/dev/ttyUSB0";
	int i;
	int n;
	int byte_length;
	int x = 0;								 // incrementer for timeout
	int switch_arg;
	char buf [1000];
	char cmd[100];
	char  *r_cmd = "r";
	char *i_cmd = "i";
	char *t_cmd = "t";
	char *f_cmd = "f";
	int fd = open (portname, O_RDWR | O_NOCTTY | O_SYNC);

	// Error catch for open
	if (fd < 0)
	{
		printf ("error %d opening %s: %s", errno, portname, strerror (errno));
		return;
	}

	set_interface_attribs (fd, B9600, 0); 			// set speed to 9600 bps, 8n1 (no parity)
	set_blocking (fd, 0);               			 						// set no blocking


	// Error catch for no arguments 
	if (argc == 1) {
		printf("No command given, exiting program.\n");
		exit(1);
	}

	if (strcmp(i_cmd, argv[1]) == 0) {
			printf("Entered i cmd\n");
			// inventory cmd
			cmd[0] = 0X31;     					
			cmd[1] = 0X03;   		
			cmd[2] = 0X01;
	}
	if(strcmp(f_cmd, argv[1])==0)
	{
	// inventory cmd
	cmd[0] = 0x33;
	cmd[1] = 0x0F;
	cmd[2] = 0x0C;
	cmd[3] = 0x30;
	cmd[4] = 0x08;
	cmd[5] = 0x33;
	cmd[6] = 0xb2;
	cmd[7] = 0xdd;
	cmd[8] = 0xd9;
	cmd[9] = 0x06;
	cmd[10] = 0xc0;
	cmd[11] = 0x00;
	cmd[12] = 0x00;
	cmd[13] = 0x00;
	cmd[14] = 0x00;
	}
	if (strcmp(r_cmd, argv[1]) == 0) {
			printf("Entered r cmd\n");
			// inventory rssi 
			cmd[0] = 0x43;   
			cmd[1] = 0x03;    
			cmd[2] = 0x01;  
	}

	if (strcmp(t_cmd, argv[1]) == 0) {
			printf("Entered t cmd\n");
			// Isolate tag
			cmd[0] = 0x33;
			cmd[1] = 0x0F;
			cmd[2] = 0x0C;
	}


	// Write to command to file 
	byte_length = sizeof(cmd) / sizeof(cmd[0]);
	
	write (fd, cmd, 3);
	

	while(1)
	{
		n= read (fd, buf, sizeof buf);  			// read up to 1000 characters if ready to read
		//printf("\nin while\n");
		if (n > 0) {
			for (i = 0; i<n; i++) {
				printf("0x%.2x ", buf[i]);
			}
			printf("\n");	
		}		
		sleep(1);
	    if(n==0) { x += 1;  break; }
		if (x==5) {break;}
	}
}
