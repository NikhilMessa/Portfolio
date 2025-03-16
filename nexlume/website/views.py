from django.shortcuts import render
from .models import Contact
from .models import TeamMember
from .models import EmailSubmission, TeamMember
from django.views.decorators.csrf import csrf_protect
from .utils.email_service import send_contact_email 
from .utils.send_internship_email import send_internship_email
from .models import Project, ProjectDetails
from django.shortcuts import render, get_object_or_404

def home(request):
    return render(request, 'main/home.html')

def projects(request):
    projects_list = Project.objects.all()
    return render(request, 'main/projects.html', {'projects': projects_list})

def project_details(request, project_name):
    project = get_object_or_404(Project, title=project_name)
    details = project.details
    return render(request, 'main/project_details.html', {'project': project,'details': details,})

def services(request):
    return render(request, 'main/services.html')

@csrf_protect
def contact_form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        organization = request.POST.get('organization')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact')
        services = ', '.join(request.POST.getlist('services'))
        investment = request.POST.get('investment')
        source = request.POST.get('source')
        message = request.POST.get('message')
        # Save the data to the database
        Contact.objects.create(
            name=name,
            organization=organization,
            email=email,
            contact_number=contact_number,
            services=services,
            investment=investment,
            source=source,
            message=message
        )
        # Send email
        send_contact_email(name, organization, email, contact_number, services, investment, message)
        return render(request, 'main/contact.html', {'success': True})
    return render(request, 'main/contact.html')

def team_view(request):
    team_members = TeamMember.objects.all()
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            # Save email to database
            EmailSubmission.objects.create(email=email)
            # Send internship email
            send_internship_email(email)
    return render(request, 'main/team.html', {'team_members': team_members})




