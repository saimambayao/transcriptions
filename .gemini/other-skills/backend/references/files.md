# File Handling

Guide for file uploads, storage, and serving files.

## File Upload

```python
# models.py
class Document(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='documents/%Y/%m/')
    uploaded_by = models.ForeignKey(User, on_delete=models.PROTECT)
    uploaded_at = models.DateTimeField(auto_now_add=True)

# views.py
def upload_document(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        
        # Validate file size (10MB limit)
        if uploaded_file.size > 10 * 1024 * 1024:
            messages.error(request, 'File too large (max 10MB)')
            return redirect('documents:upload')
        
        # Validate file type
        allowed_types = ['.pdf', '.docx', '.xlsx']
        ext = os.path.splitext(uploaded_file.name)[1].lower()
        if ext not in allowed_types:
            messages.error(request, 'Invalid file type')
            return redirect('documents:upload')
        
        # Save document
        document = Document.objects.create(
            title=uploaded_file.name,
            file=uploaded_file,
            uploaded_by=request.user
        )
        
        messages.success(request, 'Document uploaded successfully')
        return redirect('documents:detail', pk=document.pk)
    
    return render(request, 'documents/upload.html')
```

## Serving Protected Files

```python
from django.http import FileResponse
from django.shortcuts import get_object_or_404

def download_document(request, pk):
    """Serve protected file."""
    document = get_object_or_404(
        Document,
        pk=pk,
        uploaded_by__organization=request.user.organization
    )
    
    file_handle = document.file.open()
    response = FileResponse(file_handle, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{document.file.name}"'
    return response
```

## Image Processing

```python
from PIL import Image
from django.core.files.base import ContentFile
from io import BytesIO

def process_image(uploaded_file):
    """Resize and optimize image."""
    image = Image.open(uploaded_file)
    
    # Resize if too large
    max_size = (1920, 1080)
    image.thumbnail(max_size, Image.Resampling.LANCZOS)
    
    # Convert to RGB if necessary
    if image.mode not in ('RGB', 'L'):
        image = image.convert('RGB')
    
    # Save to bytes
    output = BytesIO()
    image.save(output, format='JPEG', quality=85, optimize=True)
    output.seek(0)
    
    return ContentFile(output.read())
```

For testing patterns, see [testing.md](testing.md).
