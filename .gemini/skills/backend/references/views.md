# Django Views and URL Routing

Comprehensive guide for Django views, URL patterns, and request handling for OBCMS.

## Table of Contents

- [Function-Based Views](#function-based-views)
- [Class-Based Views](#class-based-views)
- [URL Configuration](#url-configuration)
- [Request and Response](#request-and-response)
- [View Decorators](#view-decorators)
- [View Mixins](#view-mixins)
- [HTMX Integration](#htmx-integration)

## Function-Based Views

### Basic Function View

```python
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from .models import Community
from .forms import CommunityForm

@login_required
def community_list(request):
    """List communities for current user's organization."""
    communities = Community.objects.filter(
        organization=request.user.organization
    ).select_related('region', 'municipality', 'barangay')

    context = {
        'communities': communities,
        'total_count': communities.count(),
    }
    return render(request, 'communities/list.html', context)


@login_required
def community_detail(request, pk):
    """Display community details."""
    community = get_object_or_404(
        Community,
        pk=pk,
        organization=request.user.organization
    )

    # Get related assessments
    assessments = community.assessment_set.select_related(
        'created_by'
    ).order_by('-assessment_date')[:5]

    context = {
        'community': community,
        'recent_assessments': assessments,
    }
    return render(request, 'communities/detail.html', context)
```

### Create View Pattern

```python
@login_required
def community_create(request):
    """Create new community."""
    if request.method == 'POST':
        form = CommunityForm(request.POST)
        if form.is_valid():
            community = form.save(commit=False)
            community.organization = request.user.organization
            community.created_by = request.user
            community.updated_by = request.user
            community.save()

            messages.success(request, f'Community "{community.name}" created successfully.')
            return redirect('communities:detail', pk=community.pk)
    else:
        form = CommunityForm()

    context = {'form': form}
    return render(request, 'communities/create.html', context)
```

### Update View Pattern

```python
@login_required
def community_update(request, pk):
    """Update existing community."""
    community = get_object_or_404(
        Community,
        pk=pk,
        organization=request.user.organization
    )

    if request.method == 'POST':
        form = CommunityForm(request.POST, instance=community)
        if form.is_valid():
            community = form.save(commit=False)
            community.updated_by = request.user
            community.save()

            messages.success(request, 'Community updated successfully.')
            return redirect('communities:detail', pk=community.pk)
    else:
        form = CommunityForm(instance=community)

    context = {
        'form': form,
        'community': community,
    }
    return render(request, 'communities/update.html', context)
```

### Delete View Pattern

```python
@login_required
@require_http_methods(['POST'])
def community_delete(request, pk):
    """Delete community (soft delete)."""
    community = get_object_or_404(
        Community,
        pk=pk,
        organization=request.user.organization
    )

    # Soft delete
    community.delete(user=request.user)

    messages.success(request, f'Community "{community.name}" deleted.')
    return redirect('communities:list')
```

## Class-Based Views

### ListView Example

```python
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class CommunityListView(LoginRequiredMixin, ListView):
    """List all communities for user's organization."""
    model = Community
    template_name = 'communities/list.html'
    context_object_name = 'communities'
    paginate_by = 20

    def get_queryset(self):
        """Filter by user's organization."""
        qs = super().get_queryset()
        return qs.filter(
            organization=self.request.user.organization
        ).select_related('region', 'municipality', 'barangay')

    def get_context_data(self, **kwargs):
        """Add extra context."""
        context = super().get_context_data(**kwargs)
        context['total_count'] = self.get_queryset().count()
        context['regions'] = Region.objects.all()
        return context
```

### DetailView Example

```python
class CommunityDetailView(LoginRequiredMixin, DetailView):
    """Display community details."""
    model = Community
    template_name = 'communities/detail.html'
    context_object_name = 'community'

    def get_queryset(self):
        """Ensure user can only view their org's communities."""
        qs = super().get_queryset()
        return qs.filter(organization=self.request.user.organization)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add recent assessments
        context['recent_assessments'] = self.object.assessment_set.select_related(
            'created_by'
        ).order_by('-assessment_date')[:5]

        return context
```

### CreateView Example

```python
class CommunityCreateView(LoginRequiredMixin, CreateView):
    """Create new community."""
    model = Community
    form_class = CommunityForm
    template_name = 'communities/create.html'
    success_url = reverse_lazy('communities:list')

    def form_valid(self, form):
        """Set organization and audit fields."""
        form.instance.organization = self.request.user.organization
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user

        messages.success(self.request, 'Community created successfully.')
        return super().form_valid(form)

    def get_success_url(self):
        """Redirect to detail page."""
        return reverse_lazy('communities:detail', kwargs={'pk': self.object.pk})
```

### UpdateView Example

```python
class CommunityUpdateView(LoginRequiredMixin, UpdateView):
    """Update existing community."""
    model = Community
    form_class = CommunityForm
    template_name = 'communities/update.html'

    def get_queryset(self):
        """Ensure user can only update their org's communities."""
        qs = super().get_queryset()
        return qs.filter(organization=self.request.user.organization)

    def form_valid(self, form):
        """Update audit fields."""
        form.instance.updated_by = self.request.user
        messages.success(self.request, 'Community updated successfully.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('communities:detail', kwargs={'pk': self.object.pk})
```

### DeleteView Example

```python
class CommunityDeleteView(LoginRequiredMixin, DeleteView):
    """Delete community (soft delete)."""
    model = Community
    template_name = 'communities/confirm_delete.html'
    success_url = reverse_lazy('communities:list')

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(organization=self.request.user.organization)

    def delete(self, request, *args, **kwargs):
        """Soft delete instead of hard delete."""
        self.object = self.get_object()
        self.object.delete(user=request.user)
        messages.success(request, f'Community "{self.object.name}" deleted.')
        return redirect(self.success_url)
```

## URL Configuration

### App URLs Pattern

```python
# communities/urls.py
from django.urls import path
from . import views

app_name = 'communities'

urlpatterns = [
    # List and detail
    path('', views.CommunityListView.as_view(), name='list'),
    path('<int:pk>/', views.CommunityDetailView.as_view(), name='detail'),

    # CRUD operations
    path('create/', views.CommunityCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.CommunityUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.CommunityDeleteView.as_view(), name='delete'),

    # HTMX partials
    path('partial/list/', views.community_list_partial, name='list_partial'),
    path('<int:pk>/partial/', views.community_detail_partial, name='detail_partial'),
]
```

### Main URLs Pattern

```python
# obc_management/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # App URLs
    path('communities/', include('communities.urls')),
    path('mana/', include('mana.urls')),
    path('programs/', include('programs.urls')),
    path('coordination/', include('coordination.urls')),

    # Auth URLs
    path('accounts/', include('django.contrib.auth.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### URL Reverse in Views

```python
from django.urls import reverse

# In function view
return redirect('communities:detail', pk=community.pk)

# Get URL without redirecting
url = reverse('communities:detail', kwargs={'pk': community.pk})

# With query parameters
from django.http import HttpResponseRedirect
url = reverse('communities:list') + '?region=IX'
return HttpResponseRedirect(url)
```

## Request and Response

### Accessing Request Data

```python
def my_view(request):
    """Access various request attributes."""

    # GET parameters
    region = request.GET.get('region')
    page = request.GET.get('page', 1)

    # POST data
    if request.method == 'POST':
        name = request.POST.get('name')
        files = request.FILES.get('document')

    # Current user
    user = request.user
    organization = request.user.organization

    # Request metadata
    method = request.method  # GET, POST, etc.
    path = request.path  # /communities/123/
    full_path = request.get_full_path()  # /communities/123/?page=2

    # Headers
    user_agent = request.META.get('HTTP_USER_AGENT')
    referer = request.META.get('HTTP_REFERER')

    # Is AJAX/HTMX?
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    is_htmx = 'HX-Request' in request.headers
```

### Response Types

```python
from django.http import (
    HttpResponse, JsonResponse, HttpResponseRedirect,
    HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotFound
)

def various_responses(request):
    # HTML response
    return HttpResponse('<h1>Hello</h1>')

    # JSON response
    data = {'status': 'success', 'count': 10}
    return JsonResponse(data)

    # JSON list (requires safe=False)
    data = [{'id': 1, 'name': 'Item 1'}, {'id': 2, 'name': 'Item 2'}]
    return JsonResponse(data, safe=False)

    # Redirect
    return HttpResponseRedirect('/communities/')

    # Error responses
    return HttpResponseBadRequest('Invalid request')
    return HttpResponseForbidden('Access denied')
    return HttpResponseNotFound('Not found')

    # File download
    response = HttpResponse(file_content, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    return response
```

## View Decorators

### Authentication Decorators

```python
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
def protected_view(request):
    """Requires user to be logged in."""
    return render(request, 'protected.html')


@login_required(login_url='/custom-login/')
def custom_login_redirect(request):
    """Custom login URL."""
    return render(request, 'protected.html')


def is_staff(user):
    """Check if user is staff."""
    return user.is_staff

@user_passes_test(is_staff)
def staff_only_view(request):
    """Only accessible to staff users."""
    return render(request, 'staff.html')
```

### Permission Decorators

```python
from django.contrib.auth.decorators import permission_required

@permission_required('communities.add_community')
def create_community(request):
    """Requires add_community permission."""
    return render(request, 'communities/create.html')


@permission_required(['communities.view_community', 'communities.change_community'])
def update_community(request, pk):
    """Requires multiple permissions."""
    community = get_object_or_404(Community, pk=pk)
    return render(request, 'communities/update.html', {'community': community})


@permission_required('communities.delete_community', raise_exception=True)
def delete_community(request, pk):
    """Raises PermissionDenied instead of redirecting to login."""
    community = get_object_or_404(Community, pk=pk)
    community.delete()
    return redirect('communities:list')
```

### HTTP Method Decorators

```python
from django.views.decorators.http import require_http_methods, require_GET, require_POST

@require_GET
def list_view(request):
    """Only allows GET requests."""
    return render(request, 'list.html')


@require_POST
def create_view(request):
    """Only allows POST requests."""
    form = MyForm(request.POST)
    # ...


@require_http_methods(['GET', 'POST'])
def form_view(request):
    """Allows GET and POST only."""
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'form.html')
```

### CSRF Decorators

```python
from django.views.decorators.csrf import csrf_exempt, csrf_protect

@csrf_exempt
def api_webhook(request):
    """Exempt from CSRF check (use carefully!)."""
    # Process webhook
    return JsonResponse({'status': 'received'})


@csrf_protect
def protected_view(request):
    """Enforce CSRF protection even if middleware disabled."""
    return render(request, 'form.html')
```

### Cache Decorators

```python
from django.views.decorators.cache import cache_page, never_cache

@cache_page(60 * 15)  # Cache for 15 minutes
def cached_view(request):
    """Response is cached."""
    expensive_data = perform_expensive_query()
    return render(request, 'cached.html', {'data': expensive_data})


@never_cache
def always_fresh(request):
    """Never cache this response."""
    current_time = timezone.now()
    return render(request, 'fresh.html', {'time': current_time})
```

## View Mixins

### Organization Scoped Mixin

```python
from django.core.exceptions import PermissionDenied

class OrganizationScopedMixin:
    """Mixin to filter querysets by user's organization."""

    def get_queryset(self):
        """Filter by organization."""
        qs = super().get_queryset()
        if hasattr(self.request.user, 'organization'):
            return qs.filter(organization=self.request.user.organization)
        return qs.none()


class CommunityListView(LoginRequiredMixin, OrganizationScopedMixin, ListView):
    model = Community
    template_name = 'communities/list.html'
```

### Permission Mixin

```python
from django.contrib.auth.mixins import PermissionRequiredMixin

class CommunityCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Community
    permission_required = 'communities.add_community'
    template_name = 'communities/create.html'


class CommunityUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Community
    permission_required = ['communities.view_community', 'communities.change_community']
    template_name = 'communities/update.html'
```

### Audit Fields Mixin

```python
class AuditFieldsMixin:
    """Automatically set audit fields on create/update."""

    def form_valid(self, form):
        """Set created_by and updated_by fields."""
        if not form.instance.pk:
            # Creating new object
            form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class ProgramCreateView(LoginRequiredMixin, AuditFieldsMixin, CreateView):
    model = Program
    form_class = ProgramForm
```

### Success Message Mixin

```python
from django.contrib import messages

class SuccessMessageMixin:
    """Add success message after form submission."""
    success_message = ''

    def form_valid(self, form):
        response = super().form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data


class CommunityCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Community
    success_message = 'Community "%(name)s" created successfully!'
```

## HTMX Integration

### HTMX Partial Views

```python
def community_list_partial(request):
    """Return HTML fragment for HTMX."""
    region = request.GET.get('region')

    communities = Community.objects.filter(
        organization=request.user.organization
    )

    if region:
        communities = communities.filter(region__code=region)

    # Return partial template (no base layout)
    return render(request, 'communities/partials/list.html', {
        'communities': communities
    })


def community_detail_partial(request, pk):
    """Return community detail fragment."""
    community = get_object_or_404(
        Community,
        pk=pk,
        organization=request.user.organization
    )

    return render(request, 'communities/partials/detail.html', {
        'community': community
    })
```

### HTMX Form Handling

```python
def community_create_htmx(request):
    """Handle HTMX form submission."""
    if request.method == 'POST':
        form = CommunityForm(request.POST)
        if form.is_valid():
            community = form.save(commit=False)
            community.organization = request.user.organization
            community.created_by = request.user
            community.updated_by = request.user
            community.save()

            # Return success fragment
            return render(request, 'communities/partials/success.html', {
                'community': community,
                'message': 'Community created successfully!'
            })
        else:
            # Return form with errors
            return render(request, 'communities/partials/form.html', {
                'form': form
            }, status=400)

    # GET request - return empty form
    form = CommunityForm()
    return render(request, 'communities/partials/form.html', {'form': form})
```

### HTMX Middleware Helper

```python
def is_htmx(request):
    """Check if request is from HTMX."""
    return request.headers.get('HX-Request') == 'true'


def htmx_required(view_func):
    """Decorator to require HTMX requests."""
    def wrapped(request, *args, **kwargs):
        if not is_htmx(request):
            return HttpResponseBadRequest('HTMX request required')
        return view_func(request, *args, **kwargs)
    return wrapped


@htmx_required
def htmx_only_view(request):
    """Only accessible via HTMX."""
    return render(request, 'partials/data.html')
```

### HTMX Response Headers

```python
from django.http import HttpResponse

def trigger_event_view(request):
    """Send HTMX trigger event."""
    response = render(request, 'partials/updated.html')

    # Trigger client-side event
    response['HX-Trigger'] = 'dataUpdated'

    # Trigger with data
    import json
    response['HX-Trigger'] = json.dumps({
        'dataUpdated': {'id': 123, 'status': 'success'}
    })

    return response


def redirect_htmx(request):
    """Redirect in HTMX request."""
    response = HttpResponse()
    response['HX-Redirect'] = '/communities/'
    return response
```

This covers the essential Django view patterns for OBCMS. For REST API views, see [apis.md](apis.md).
