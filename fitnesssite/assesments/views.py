import calendar
from django.shortcuts import render
from django.utils import timezone

from .forms import BaselineAssesmentForm

def assesment_admin(request):
    current_year = timezone.now().year
    calendar_html = calendar.HTMLCalendar().formatyear(current_year)

    return render(request, 'assesments/admin.html', {
        'current_year': current_year,
        'calendar_html': calendar_html,
    })


def index(request):
    if request.method == 'POST':
        pass
    else:
        form = BaselineAssesmentForm()
        return render(
            request,
            'assesments/index.html',
            {
                'form' : form
            }

        )
