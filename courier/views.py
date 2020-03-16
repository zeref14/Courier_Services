from django.shortcuts import render,redirect
from .models import *
from .forms import OrderForm
from django.forms import inlineformset_factory
from .filters import *
# Create your views here.

def home(request):
    orders = Order.objects.all().order_by('-date_created')
    students = Student.objects.all().order_by('id')


    total_students = students.count()
    total_orders = orders.count()

    myFilter = StudentFilter(request.GET, queryset=students)
    students=myFilter.qs

    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'students': students, 'total_students': total_students, 'total_orders': total_orders
        , 'delivered': delivered, 'pending': pending,'myFilter':myFilter}

    return  render(request,'courier/dashboard.html',context)

def student(request,pk_test):
    student= Student.objects.get(id=pk_test)
    orders=student.order_set.all().order_by('-date_created')
    total_order=orders.count()

    myFilter=OrderFilter(request.GET,queryset=orders)
    orders=myFilter.qs

    context={'student':student,'orders':orders,'total_order':total_order,'myFilter':myFilter}
    return render(request,'courier/student.html',context)

def company(request):
    companys=Company.objects.all()
    return render(request,'courier/company.html',{'companys':companys})

def createCourier(request,pk):


    OrderFormSet= inlineformset_factory(Student,Order,fields=('company','status'),extra=1)
    student=Student.objects.get(id=pk)
    formset=OrderFormSet(queryset=Order.objects.none(),instance=student)
    if request.method == 'POST':
        # form= OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=student)
        if formset.is_valid():
            formset.save()
            return redirect('/')


    context={'formset':formset,'student':student}

    return render(request,'courier/courier_form.html',context)

def updateCourier(request,pk):

    order= Order.objects.get(id=pk)
    form= OrderForm(instance=order)
    if request.method == 'POST':
        form= OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'courier/update_form.html',context)

def deleteOrder(request, pk):

	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item':order}
	return render(request, 'courier/remove_courier.html', context)