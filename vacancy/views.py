from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_detail
from django.shortcuts import get_object_or_404 
from models import EnableOpening, Opening, Candidate
from forms import ApplyForm

def index(request):
    eopen = EnableOpening.objects.all()
    d = {"opens": eopen}
    return direct_to_template(request,
            template="vacancy/index.html",
            extra_context = d,
            )

def detail(request, id):
    qs = EnableOpening.objects.all()
    d = {"queryset": qs, 'object_id': int(id), 'template_name': "vacancy/opening_detail.html" }
    return object_detail(request,**d)

def show_form(request, id):
    opening = get_object_or_404(EnableOpening, id = id)
    init = {'opening': opening.id}
    applyform = ApplyForm()
    if request.method == "POST":
        applyform = ApplyForm(data = request.POST, files = request.FILES)
        if applyform.is_valid():
            can = applyform.get_candidate(opening)
            d = {'candidate': can, 'open': opening}
            return direct_to_template(request, template="vacancy/job_submit_success.html")
    d = {"open": opening , "form": applyform}
    return direct_to_template(request, template = "vacancy/job_form.html", extra_context = d)
