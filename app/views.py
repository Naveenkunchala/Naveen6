from django.shortcuts import render

# Create your views here.



def conditions(request):
    d={'a':2000,'b':300,'c':500}
    return render(request,'conditions.html',context=d)



def loops(request):
    d={'name':'NAVEEN ROI'}
    return render(request,'loops.html',context=d)
