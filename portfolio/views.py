from django.shortcuts import render
from google.cloud import firestore
from firestore_config import db

# Create your views here.
def home(request):
    # Get document from projects collection
    docs_ref = db.collection('projects').order_by('rank', direction=firestore.Query.ASCENDING).stream()
    docs = [doc.to_dict() for doc in docs_ref]

    # Pasa los documentos al contexto
    context = {
        'projects': docs
    }

    return render(request, 'home.html', context)