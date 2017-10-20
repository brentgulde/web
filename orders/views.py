from django.shortcuts import render, redirect
from .models import Student, Section
from .forms import StudentForm, SectionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#@login_required
def index(request):
    student = Student.objects.all()
    return render(request, 'index.html', {'student': student})
def sectionlist(request):
    section = Section.objects.all()
    return render(request, 'sectionlist.html', {'section': section})

#@login_required
def show(request, section_id):
    student = Student.objects.filter(id=section_id)
    return render(request, 'show.html', {'order': order})

#@login_required
def new(request):
    if request.POST:
        form = StudentForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('/', messages.success(request, 'Student successfully created.', 'alert-success'))
            else:
                return redirect('/', messages.error(request, 'Student is not saved', 'alert-danger'))
        else:
            return redirect('/', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = StudentForm()
        return render(request, 'new.html', {'form':form})

#@login_required
def edit(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.POST:
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            if form.save():
                return redirect('/', messages.success(request, 'Student successfully updated.', 'alert-success'))
            else:
                return redirect('/', messages.error(request, 'Student is not saved', 'alert-danger'))
        else:
            return redirect('/', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = StudentForm(instance=student)
        return render(request, 'edit.html', {'form':form})

#@login_required
def destroy(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('/', messages.success(request, 'Student was successfully deleted.', 'alert-success'))


def section(request):
    if request.POST:
        form = SectionForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('/', messages.success(request, 'Section successfully created.', 'alert-success'))
            else:
                return redirect('/', messages.error(request, 'Section is not saved', 'alert-danger'))
        else:
            return redirect('/', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = SectionForm()
        return render(request, 'section.html', {'form':form})

#Product

#@login_required
def index_product(request):
    section = Section.objects.filter(active='1')
    return render(request, 'index_product.html', {'products': products})    

#@login_required
def new_product(request):
    if request.POST:
        form = SectionForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('/products', messages.success(request, 'Product was successfully created.', 'alert-success'))
            else:
                return redirect('/products', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/products', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        section = SectionForm()
        return render(request, 'new_product.html', {'product_form':product_form})    

#@login_required
def destroy_product(request, section_id):
    section = Section.objects.get(id=section_id)
    section.delete()
    return redirect('/', messages.success(request, 'Section was successfully deleted.', 'alert-success'))



        