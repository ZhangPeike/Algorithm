#include<iostream>
using namespace std;

class BaseA{
public:
    BaseA(){cout<<"BaseA founed"<<endl;}
};
class BaseB{
public:
    BaseB(){cout<<"BaseB founed"<<endl;}
};
template<typename T, int rows>
class BaseC{
private:
    T data;
public:
    BaseC():data(rows){
        cout<<"BaseC founed "<< data << endl;}
};
template<class T>
class Derived:public T{
public:
    Derived():T(){cout<<"Derived founed"<<endl;}
};

int main()
{
    Derived<BaseA> x;// BaseA作为基类
    Derived<BaseB> y;// BaseB作为基类
    Derived<BaseC<int, 3> > z; // BaseC<int,3>作为基类
    return 0;
}
