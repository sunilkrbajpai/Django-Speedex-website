from time import sleep
from django.shortcuts import render,redirect,reverse
import datetime
from . models import Notification,Consignment,City
from generalzone.models import Enquiry,Complain,Career

# Create your views here.
def adminhome(request):
    if request.session['userid']:
        nf = Notification.objects.all()
        return render(request,'adminhome.html',{'nf':nf})
    else:
        return render(request,'login.html')
def enquiries(request):
    if request.session['userid']:
        enq=Enquiry.objects.all()
        return render(request,'enquiries.html',{'enq':enq})
    else:
        return render(request,'login.html')
def complains(request):
    if request.session['userid']:
        comp=Complain.objects.all()
        return render(request,'complains.html',{'comp':comp})
    else:
        return render(request,'login.html')
def consignment(request):
    if request.session['userid']:
        city=City.objects.all()
        return render(request,'consignment.html',{'city':city})
    else:
        return render(request,'login.html')
def jobseekers(request):
    if request.session['userid']:
        car=Career.objects.all()
        return render(request,'jobseekers.html',{'car':car})
    else:
        return render(request,'login.html')
def logout(request):
    if request.session['userid']:
        request.session['userid']=None
        sleep(3)
        return render(request, 'login.html')
    else:
        return render(request,'login.html')
def addnotification(request):
    if request.session['userid']:
        notificationtext=request.POST['notificationtext']
        posteddate=datetime.datetime.now().strftime('%Y/%m/%d')
        nf=Notification(notificationtext=notificationtext,posteddate=posteddate)
        nf.save()
        return redirect('adminzone:adminhome')
    else:
        return render(request,'login.html')
def deletenotification(request,id):
    if request.session['userid']:
        nf=Notification.objects.get(id=id)
        nf.delete()
        return redirect('adminzone:adminhome')
    else:
        return render(request,'index.html')
def deleteenquiries(request,id):
    if(request.session['userid']):
        en=Enquiry.objects.get(id=id)
        en.delete()
        return redirect('adminzone:enquiries')
    else:
        return render(request,'login.html')
def deletecomplains(request,id):
    if (request.session['userid']):
        en = Complain.objects.get(id=id)
        en.delete()
        return redirect('adminzone:complains')
    else:
        return render(request, 'login.html')
def saveconsignment(request):
    if request.session['userid']:
        refNo=request.POST['refNo']
        sendername=request.POST['sendername']
        senderaddress=request.POST['senderaddress']
        source=request.POST['source']
        sendercontactno=request.POST['sendercontactno']
        receivername=request.POST['receivername']
        receiveraddress=request.POST['receiveraddress']
        currentcity=request.POST['currentcity']
        destination=request.POST['destination']
        status=request.POST['status']
        posteddate=datetime.datetime.now().strftime('%Y/%m/%d')

        if(Consignment.objects.filter(refNo=refNo).exists()):
            msg='This entry already exists'
        else:
            con=Consignment(refNo=refNo,status=status,senderaddress=senderaddress,sendercontactno=sendercontactno,sendername=sendername,source=source,receivername=receivername,receiveraddress=receiveraddress,currentcity=currentcity,destination=destination,posteddate=posteddate)
            con.save()
            msg='The entry is done!'
        return render(request,'consignment.html',{'msg':msg})
    else:
        return render(request,'login.html')
def deletejobseekers(request,emailaddress):
    if request.session['userid']:
        c=Career.objects.get(emailaddress=emailaddress)
        c.delete()
        return redirect('adminzone:jobseekers')
    else:
        return render(request,'login.html')
