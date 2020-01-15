 int reverse(int x) 
    {
        const int int_max=0x7fffffff;
        const int int_min=0x80000000;
        long long anwser=0;
        while(x!=0)
        {
            anwser=anwser*10+(x%10);
            x/=10;
        }
        if(anwser<int_min || anwser>int_max)
        {
            anwser=0;
        }
        return anwser;
    }