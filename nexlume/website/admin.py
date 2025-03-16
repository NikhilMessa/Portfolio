from django.contrib import admin
from .models import Contact
from .models import TeamMember
from django.utils.html import format_html
from .models import EmailSubmission
from .models import Project

#-------------------------------------------------------CONTACT ADMIN PANEL-------------------------------------------------------------------

class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'organization', 'email', 'contact_number', 'services', 'investment', 'source', 'message')
    list_display = ('name', 'organization', 'email', 'contact_number', 'services', 'investment', 'source', 'message')

    def has_add_permission(self, request):
        return False  # This will remove the ability to add new contacts manually
    
    def has_change_permission(self, request, obj=None):
        return False  # This will remove the ability to change existing contacts
    
    def has_delete_permission(self, request, obj=None):
        return True  # This will remove the ability to delete contacts
admin.site.register(Contact, ContactAdmin)

#-------------------------------------------------------TEAM ADMIN PANEL-------------------------------------------------------------------

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'linkedin_link', 'view_profile')  # Removed image_size
    search_fields = ('name', 'role')  # Search functionality
    list_filter = ('role',)  # Filter by role
    ordering = ('name',)  # Default sorting (alphabetical order)

    def view_profile(self, obj):
        if obj.image:
            return format_html(
                '<a href="{}" onclick="window.open(this.href,\'popup\',\'width=600,height=600\'); return false;" '
                'style="padding:5px 10px; background:#007bff; color:white; border-radius:5px; text-decoration:none;">View Profile</a>',
                obj.image.url
            )
        return "No Image"
    view_profile.short_description = "Profile Image"
    
    def linkedin_link(self, obj):
        if obj.linkedin:
            return format_html('<a href="{}" target="_blank">LinkedIn</a>', obj.linkedin)
        return "No Link"
    linkedin_link.short_description = "LinkedIn"
admin.site.register(TeamMember, TeamMemberAdmin)


class EmailSubmissionAdmin(admin.ModelAdmin):
    list_display = ('email',)  
    readonly_fields = ('email',) 
    
    def has_delete_permission(self, request, obj=None):
        return False    # Disables delete functionality in the admin panel
    def has_add_permission(self, request):
        return False     # Disables add functionality in the admin panel
    def has_change_permission(self, request, obj=None):
        return False    # Disables change functionality in the admin panel
admin.site.register(EmailSubmission, EmailSubmissionAdmin)


from django.contrib import admin
from .models import Project, ProjectDetails

# Admin configuration for the Project model
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'project_type')  # Fields to be shown in the list view
    search_fields = ('title', 'category')  # Fields to be searchable
    list_filter = ('category',)  # Filter options based on category

# Admin configuration for the ProjectDetails model
class ProjectDetailsAdmin(admin.ModelAdmin):
    list_display = ('project', 'client_name', 'date', 'design_team')  # Fields to be shown in the list view
    search_fields = ('project__title', 'client_name')  # Fields to be searchable (project title can be accessed using `project__title`)
    list_filter = ('date', 'design_team')  # Filter options based on date and design team

# Registering the models and their admin configurations
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectDetails, ProjectDetailsAdmin)




