#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[50];
    float math;
    float physics;
    float chemistry;
    float average;
}Student;

Student *create_student(char name[], float math, float physics, float chemistry){
    Student *s = (Student *)malloc(sizeof(Student));
    strcpy(s->name,name);
    s->math = math;
    s->physics = physics;
    s->chemistry = chemistry;
    s->average = (s->math + s->physics + s->chemistry)/3.0;

    return s;
}


void print_student(Student* s){
    printf("\nStudent Name: %s \nPhysics:%f\nChemistry:%f \nMath:%f \n",s->name, s->physics, s->chemistry, s->math);
    printf("\nAverage Mark: %.2f\n", s->average);

    if (s->average >= 60){
        printf("\nCongratulations %s, You Passed with an average of %.2f\n", s->name, s->average);
    }else {
        printf("\n Damn you %s, you failed with an average of %.2f\n", s->name, s->average);
    }

}   

Student *top_student(Student* s1, Student* s2, Student* s3) {
    
    Student* top = s1;

    if (s2->average > top->average){
        top = s2;
    }

    if (s3->average > top->average){
        top = s3;
    }
    
    return top;
}

int main () {

    Student *s1 = create_student("Ali", 40, 60, 80);
    Student *s2 = create_student("James", 10, 60, 99);
    Student *s3 = create_student("Ahmad", 70, 80,90);

    print_student(s1);
    print_student(s2);
    print_student(s3);

    Student* top  = top_student(s1,s2,s3);
    printf("\nThe toppest student is %s with an average of %.2f\n", top->name, top->average);

    free(s1);
    free(s2);
    free(s3);

    return 0;
}
