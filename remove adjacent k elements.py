
#include <stdio.h>

int main() {
	int a[100],n,x,y=0,sum=0;
	scanf("%d",&n);
	for(int i =0;i<n;i++)
	{
	    scanf("%d",&a[i]);
	}
	scanf("%d",&x);
	int j =0;
	if(n==2)
	{
	    if(a[0]==x||a[1]==x)
	    {
	        printf("0");
	    }
	    else
	    {
	        printf("%d",a[0]+a[1]);
	    }
	}
	else
	{
	    for(int i = 1;i<n-1;i++)
	    {
	        if(a[i]==x)
	        {
	            a[i] =0;
	            if(a[i+1]!=x)
	            {
	                a[i+1]=0;
	            }
	            a[i-1]=0;
	        }
	    }
	if(a[n-1]==x)
	{
	    a[n-1] = 0;
	    a[n-2] = 0;
	}
	if(a[0]==x)
	{
	    a[0] = 0;
	    a[1] = 0;
	}
	int sum =0;
	for(int i =0;i<n;i++)
	{
	    sum +=a[i];
	}
	printf("%d",sum);
	}
	
}
*//input:5
*//1 2 2 1 6 2
*//output:6
