#include<stdio.h>
#include<conio.h>
#define SIZE 2
struct Student
{
    int sid;
    char name[30];
    float fees;
    float comp,maths,eng,total,per;
    char grade;
}s[SIZE];

//struct Student s[SIZE];
void createStudentDetails();
void displayStudentDetails();
//void displayParticularStudentDetails();
//void updateStudentDetails();
//int search(int id);

void main()
{
    int choice;
    textbackground(BLUE);
    while(1)
    {
        clrscr();
        gotoxy(40,13);
        sound(200);
        delay(200);
        nosound();
        textcolor(YELLOW);
        cprintf("1----CREATE");
        gotoxy(40,14);
        cprintf("2----Display All");
        gotoxy(40,15);
        cprintf("3----Exit");
        gotoxy(40,16);
        cprintf("\nEnter the choice: ");
        scanf("%d",&choice);
        switch(choice)
        {
            case 1:createStudentDetails();
            break;
            case 2:displayStudentDetails();
            break;
            case 3:exit(0);
        }//end of switch
        getch();
    }//end of while
}//end of main
void createStudentDetails()
{
    int i;
    float temp;
    for(i=0;i<SIZE;i++)
    {
        printf("\nEnter the sid and name: ");
        scanf("%d%s",&s[i].sid,s[i].name);
        printf("\nEnter the fees: ")
        scanf("%f",&temp);
        s[i].fees=temp;
        printf("\nEnter the comp: ");
        scanf("%f",&temp);
        s[i].comp=temp;
        printf("\nEnter the math: ");
        scanf("%f",&temp);
        s[i].maths=temp;
        printf("\nEnter the eng: ");
        scanf("%f",&temp);
        s[i].eng=temp;
        s[i].total=s[i].comp+s[i].maths+s[i].eng;
        s[i].per=s[i].total/3;
        if(s[i].per>=90)
        {
            s[i].grade='A';
        }
        else if(s[i].per>=80)
        {
            s[i].grade='B';
        }
        else
        {
            s[i].grade='C';
        }
    }//end of for
}//end of createStudentDetails

void displayStudentDetails()
{
    int i;
    clrscr();
    printf("\nsid\tname\tfees\tcomp\tmaths\teng\ttotal\tper\tgrade");
    for(i=0;i<SIZE;i++)
    {
        printf("\n%d\t%s\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%c",s[i].sid,s[i].name,s[i].fees,s[i].comp,s[i].maths,s[i].eng,s[i].total,s[i].per,s[i].grade);
    }
}
