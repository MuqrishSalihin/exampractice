#include <stdio.h>
#include <stdlib.h> 
#include <string.h>
#include <time.h> 

int main (){
    char name[50];
    char answer[10];
    srand(time(NULL)); 
    int x; 
    

    printf("Welcome to the Lucky Number Game.\n Can I get your name: "); //dont put in any of variable yet, since we havent even recieved any of the output yet
    fgets(name, sizeof(name), stdin);
    name[strcspn(name,"\n")] = '\0';

    printf("Hello %s \n", name);

    int randnum = 1 + rand() % 100;


    do {
        int counter = 0;
        do {

            printf("Guess a number (1-100): \n");
            scanf("%d",&x);

            while(getchar() != '\n'); // cleans the x so that the buffer is ready to receive input
            
            counter++;

            if (x == randnum){
                printf("Correct!, You guessed the lucky number in %d attempts\n", counter);
                break;
            } else {
                printf("You got the wrong number, Try Again\n");
                
            }

        } while(1);
        
        printf("Do you want to play again ?(Y/N): \n");
        fgets(answer, sizeof(answer), stdin);
        answer[strcspn(answer,"\n")] = '\0';

        if (answer[0] == 'N' || answer[0] == 'n'){
            break;
        }

    } while (answer[0] == 'Y' || answer[0] =='y');

    printf("Thanks for playing\n");
    return 0;

}
