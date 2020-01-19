#include<iostream>
#include<stdlib.h>
int main(){
    int a=0;
    int b=1;
    if(a=b){
        std::cout<<"a=b returns true!"<<std::endl;
        std::cout<<"a: "<<a<<std::endl;
    }
    else{
        std::cout<<"a=b returns false!"<<std::endl;
    }
    char key;
    for(int i=0;i=a;i++){
        std::cout<<"loop"<<std::endl;
        _sleep(1000);
        std::cin>>key;
        if(key=='q'){
            break;
        }
    }
    return 0;
}