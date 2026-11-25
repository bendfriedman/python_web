from django.shortcuts import render, redirect
from HolidayHousings.models import HolidayHousing
from HolidayHousings.forms import HolidayHousingForm

def housing_list(request):

    all_housings = HolidayHousing.objects.all()

    # print('DEBUGGING in housing list function based view')
    # print('Complete Queryset:', all_housings)
    # print('1st item: ', all_housings[0])
    # print('Special field of 1st item: ', all_housings[0].specials)

    context = {'all_housings': all_housings}

    return render(request, 'housing-list.html', context)


def housing_detail(request, **kwargs):

    housing_id = kwargs['pk']  # pk refers to "primary key"
    current_single_housing = HolidayHousing.objects.get(id=housing_id)

    context = {'single_housing': current_single_housing}

    # print('DEBUGGING in housing detail function based view')
    # print('All keyword arguments: ', kwargs)
    # print('Current housing ID / primary key: ', housing_id)
    # print('Data of current housing: ', current_single_housing)
    # print('Context: ', context)
    # print('Object type of housing object: ', type(context['single_housing']))
    # print('Data in Context: ', context['single_housing'])

    return render(request, 'housing-detail.html', context)


def housing_create(request):

    if request.method == 'POST':
        # print('DEBUGGING in POST (after pressing submit button) in create view')

        form_in_function_based_view = HolidayHousingForm(request.POST)
        form_in_function_based_view.instance.user = request.user  # add also user to data

        # print('POST data: ', request.POST)
        # print('User: ', request.user)
        # print('Django form: ', form_in_function_based_view)

        if form_in_function_based_view.is_valid():
            # create new housing instance, but do not save, yet
            new_housing = form_in_function_based_view.save(commit=False)

            # add user to new housing instance
            new_housing.user = request.user

            # save
            new_housing.save()

            # print('SAVED a new housing in DB, redirecting')
            return redirect('housing-list')

        else:
            # print(form_in_function_based_view.errors)
            pass

        # print('REDIRECTING to housing list view.')
        return redirect('housing-list')

    else:  # request.method == 'GET'
        # print('DEBUGGING in GET (before submitting form) in create view')

        form_in_my_function_based_view = HolidayHousingForm()
        context = {'form': form_in_my_function_based_view}

        return render(request, 'housing-create.html', context)