from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreatedForm

@login_required
def image_create(request):
    '''
    View for creating an Image using the JavaScript Bookmarklet.
    :param request: request
    :return: a render
    '''
    if request.method=='POST':
        form = ImageCreatedForm(data=request.POST)
        if form.is_valid():
            #form data is valid
            cd = form.cleaned_data
            new_item=form.save(commit=False)
            new_item.user=request.user
            new_item.save()
            messages.success(request,'Image added successfully')
            return redirect(new_item.get_absolute_url())
    else:
        form=ImageCreatedForm(data=request.GET)

    return render(request,'image/create.html',{'section':'images',
                                                      'form':form})
