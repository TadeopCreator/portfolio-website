from django.shortcuts import render
from google.cloud import firestore
from firestore_config import db

# Create your views here.
def render_projects(request):    
    # Get document from projects collection
    docs_ref = db.collection('projects').order_by('year', direction=firestore.Query.DESCENDING).stream()
    docs = [doc.to_dict() for doc in docs_ref]

    # Pasa los documentos al contexto
    context = {
        'projects': docs
    }

    return render(request, 'archive.html', context)


def storytelling_ai(request):
    return render(request, 'storytelling_ai.html')
