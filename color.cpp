#include <iostream>
#include <windows.h> //WinApi header
using namespace std;


int main()
{	
	HANDLE hConsole;
	int i = 1;

	hConsole = GetStdHandle(STD_OUTPUT_HANDLE);

	for(int k=1; k <16; k++) //try from 255 and see what happens
	{
		if (i ==16)
		{
			cin.get();
			i = 0;
		}
		SetConsoleTextAttribute(hConsole, k);
		cout <<k<<" This is my color " << endl;
		i += 1;
	}

SetConsoleTextAttribute(hConsole, 4); cout<<"\n\t\tno readers firing"; SetConsoleTextAttribute(hConsole, 8);
cout<<"\n"<<"###########################################";
cout<<"\n"<<"#"<<"                /rA\\                     "<<"#";	
cout<<"\n"<<"#"<<"                                          "<<"#";	
cout<<"\n"<<"#"<<"                  1                       "<<"#";
cout<<"\n"<<"#"<<"                                          "<<"#";
cout<<"\n"<<"#"<<"        2                    3            "<<"#";
cout<<"\n"<<"#"<<"                                          "<<"#";			
cout<<"\n"<<"#"<<"                  4                       "<<"#";
cout<<"\n"<<"#"<<"                                          "<<"#";
cout<<"\n"<<"#"<<" /rB\\  5                    6   /rD\\      "<<"#";  
cout<<"\n"<<"#"<<"                                          "<<"#";
cout<<"\n"<<"#"<<"                 7                        "<<"#";
cout<<"\n"<<"#"<<"                                          "<<"#";
cout<<"\n"<<"#"<<"      8                     9             "<<"#";
cout<<"\n"<<"#"<<"                                          "<<"#";
cout<<"\n"<<"#"<<"                 10                       "<<"#";
cout<<"\n"<<"#"<<"                                          "<<"#";
cout<<"\n"<<"#"<<"                 /rC\\                     "<<"#";
cout<<"\n"<<"###########################################";

cin.get();
cout<<"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n";
//fire off rA
SetConsoleTextAttribute(hConsole, 4); cout<<"\n\t\tReader A firing"; SetConsoleTextAttribute(hConsole, 8);
cout<<"\n"<<"###########################################";
cout<<"\n"<<"#"; SetConsoleTextAttribute(hConsole, 12);cout<<"                /rA\\                     ";SetConsoleTextAttribute(hConsole, 8);cout<<"#";	
cout<<"\n"<<"#"<<"                                          "<<"#";	
cout<<"\n"<<"#"<<"                  1                       "<<"#";
cout<<"\n"<<"#"<<"                                          "<<"#";
cout<<"\n"<<"#"<<"        2                    3            "<<"#";
cout<<"\n"<<"#"<<"                                          "<<"#";			
cout<<"\n"<<"#"<<"                  4                       "<<"#";
cout<<"\n"<<"#"<<"                                          "<<"#";
cout<<"\n"<<"# /rB\\  5                    6   /rD\\      "<<"#";  
cout<<"\n"<<"#"<<"                                          "<<"#";
cout<<"\n"<<"#"<<"                 7                        "<<"#";
cout<<"\n"<<"#"<<"                                          "<<"#";
cout<<"\n"<<"#"<<"      8                     9             "<<"#";
cout<<"\n"<<"#"<<"                                          "<<"#";
cout<<"\n"<<"#"<<"                 10                       "<<"#";
cout<<"\n"<<"#"<<"                                          "<<"#";
cout<<"\n"<<"#"<<"                 /rC\\                     "<<"#";
cout<<"\n"<<"###########################################";



cin.get();
cout<<"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n";
//fire off rB
SetConsoleTextAttribute(hConsole, 4); cout<<"\n\t\tReader B firing"; SetConsoleTextAttribute(hConsole, 8);
cout<<"\n"<<"###########################################";
cout<<"\n"<<"#                /rA\\                     #";	
cout<<"\n"<<"#"<<"                                          "<<"#";	
cout<<"\n"<<"#"<<"                  1                       "<<"#";
cout<<"\n"<<"#"<<"                                          "<<"#";
cout<<"\n"<<"#"<<"        2                    3            "<<"#";
cout<<"\n"<<"#"<<"                                          "<<"#";			
cout<<"\n"<<"#"<<"                  4                       "<<"#";
cout<<"\n"<<"#"<<"                                          "<<"#";
cout<<"\n"<<"#";SetConsoleTextAttribute(hConsole, 12);cout<<" /rB\\";SetConsoleTextAttribute(hConsole, 8);cout<<"  5                    6   /rD\\      "<<"#";  
cout<<"\n"<<"#"<<"                                          "<<"#";
cout<<"\n"<<"#"<<"                 7                        "<<"#";
cout<<"\n"<<"#"<<"                                          "<<"#";
cout<<"\n"<<"#"<<"      8                     9             "<<"#";
cout<<"\n"<<"#"<<"                                          "<<"#";
cout<<"\n"<<"#"<<"                 10                       "<<"#";
cout<<"\n"<<"#"<<"                                          "<<"#";
cout<<"\n"<<"#"<<"                 /rC\\                     "<<"#";
cout<<"\n"<<"###########################################";


cin.get();
cout<<"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n";
//fire off rC
SetConsoleTextAttribute(hConsole, 4); cout<<"\n\t\tReader C firing"; SetConsoleTextAttribute(hConsole, 8);
cout<<"\n"<<"###########################################";
cout<<"\n"<<"#                /rA\\                     #";	
cout<<"\n"<<"#"<<"                                          "<<"#";	
cout<<"\n"<<"#"<<"                  1                       "<<"#";
cout<<"\n"<<"#"<<"                                          "<<"#";
cout<<"\n"<<"#"<<"        2                    3            "<<"#";
cout<<"\n"<<"#"<<"                                          "<<"#";			
cout<<"\n"<<"#"<<"                  4                       "<<"#";
cout<<"\n"<<"#"<<"                                          "<<"#";
cout<<"\n"<<"# /rB\\  5                    6   /rD\\      "<<"#";
cout<<"\n"<<"#"<<"                 7                        "<<"#";
cout<<"\n"<<"#"<<"                                          "<<"#";
cout<<"\n"<<"#"<<"      8                     9             "<<"#";
cout<<"\n"<<"#"<<"                                          "<<"#";
cout<<"\n"<<"#"<<"                 10                       "<<"#";
cout<<"\n"<<"#"<<"                                          "<<"#";
cout<<"\n"<<"#";SetConsoleTextAttribute(hConsole, 12);cout<<"                 /rC\\                     ";SetConsoleTextAttribute(hConsole, 8);cout<<"#";
cout<<"\n"<<"###########################################";
	


cin.get();
cout<<"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n";
//fire off rD
SetConsoleTextAttribute(hConsole, 4); cout<<"\n\t\tReader D firing"; SetConsoleTextAttribute(hConsole, 8);
cout<<"\n"<<"###########################################";
cout<<"\n"<<"#                /rA\\                     #";	
cout<<"\n"<<"#"<<"                                          "<<"#";	
cout<<"\n"<<"#"<<"                  1                       "<<"#";
cout<<"\n"<<"#"<<"                                          "<<"#";
cout<<"\n"<<"#"<<"        2                    3            "<<"#";
cout<<"\n"<<"#"<<"                                          "<<"#";			
cout<<"\n"<<"#"<<"                  4                       "<<"#";
cout<<"\n"<<"#"<<"                                          "<<"#";
cout<<"\n"<<"# /rB\\  5                    6";SetConsoleTextAttribute(hConsole, 12);cout<<"   /rD\\      ";SetConsoleTextAttribute(hConsole, 8);cout<<"#";  
cout<<"\n"<<"#"<<"                                          "<<"#";
cout<<"\n"<<"#"<<"                 7                        "<<"#";
cout<<"\n"<<"#"<<"                                          "<<"#";
cout<<"\n"<<"#"<<"      8                     9             "<<"#";
cout<<"\n"<<"#"<<"                                          "<<"#";
cout<<"\n"<<"#"<<"                 10                       "<<"#";
cout<<"\n"<<"#"<<"                                          "<<"#";
cout<<"\n"<<"#"<<"                 /rC\\                     "<<"#";
cout<<"\n"<<"###########################################";


cin.get();

	return 0;


}