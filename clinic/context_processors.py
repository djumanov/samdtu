from .models import Department, Info, DocCategory

def global_context(request):
    return {
        'departments': Department.objects.all(),
        'info_items': Info.objects.all(),
        'doc_categories': DocCategory.objects.all(),
    }
