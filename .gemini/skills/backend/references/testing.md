# Django Testing

Guide for testing Django applications with pytest and Django test framework.

## Test Setup

```python
# pytest.ini
[pytest]
DJANGO_SETTINGS_MODULE = obc_management.settings.test
python_files = tests.py test_*.py *_tests.py

# conftest.py
import pytest
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.fixture
def user(db):
    return User.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='testpass123'
    )

@pytest.fixture
def organization(db):
    return Organization.objects.create(
        name='Test Organization',
        code='TEST'
    )

@pytest.fixture
def community(db, organization):
    return Community.objects.create(
        organization=organization,
        name='Test Community',
        population=1000
    )
```

## Model Tests

```python
# tests/test_models.py
import pytest
from communities.models import Community

@pytest.mark.django_db
class TestCommunityModel:
    def test_create_community(self, organization):
        """Test creating a community."""
        community = Community.objects.create(
            organization=organization,
            name='New Community',
            population=500
        )
        assert community.id is not None
        assert community.name == 'New Community'
        assert community.population == 500

    def test_community_str(self, community):
        """Test string representation."""
        assert str(community) == f"{community.name}, {community.barangay.name}"

    def test_soft_delete(self, community, user):
        """Test soft delete."""
        community.delete(user=user)
        assert community.deleted_at is not None
        assert community.deleted_by == user
        assert Community.objects.count() == 0  # Default manager filters deleted
        assert Community.all_objects.count() == 1  # all_objects includes deleted
```

## View Tests

```python
# tests/test_views.py
import pytest
from django.urls import reverse
from django.test import Client

@pytest.mark.django_db
class TestCommunityViews:
    def test_list_view_requires_login(self):
        """Test that list view requires authentication."""
        client = Client()
        url = reverse('communities:list')
        response = client.get(url)
        assert response.status_code == 302  # Redirect to login

    def test_list_view_authenticated(self, user, community):
        """Test list view for authenticated user."""
        client = Client()
        client.force_login(user)
        url = reverse('communities:list')
        response = client.get(url)
        assert response.status_code == 200
        assert 'communities' in response.context

    def test_create_community(self, user, organization):
        """Test creating community via POST."""
        client = Client()
        client.force_login(user)
        url = reverse('communities:create')
        data = {
            'name': 'New Community',
            'organization': organization.id,
            'population': 1000,
        }
        response = client.post(url, data)
        assert response.status_code == 302  # Redirect after success
        assert Community.objects.filter(name='New Community').exists()
```

## API Tests

```python
# tests/test_api.py
import pytest
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

@pytest.mark.django_db
class TestCommunityAPI:
    def test_list_requires_authentication(self):
        """Test that API requires authentication."""
        client = APIClient()
        url = '/api/communities/'
        response = client.get(url)
        assert response.status_code == 401  # Unauthorized

    def test_list_authenticated(self, user, community):
        """Test API list for authenticated user."""
        client = APIClient()
        token = Token.objects.create(user=user)
        client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
        
        url = '/api/communities/'
        response = client.get(url)
        assert response.status_code == 200
        assert len(response.data['results']) == 1

    def test_create_community_api(self, user, organization):
        """Test creating community via API."""
        client = APIClient()
        token = Token.objects.create(user=user)
        client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
        
        url = '/api/communities/'
        data = {
            'name': 'API Community',
            'organization': organization.id,
            'population': 500,
        }
        response = client.post(url, data, format='json')
        assert response.status_code == 201
        assert Community.objects.filter(name='API Community').exists()
```

## Test Factories

```python
# factories.py
import factory
from communities.models import Community, Organization

class OrganizationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Organization

    name = factory.Sequence(lambda n: f'Organization {n}')
    code = factory.Sequence(lambda n: f'ORG{n}')

class CommunityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Community

    organization = factory.SubFactory(OrganizationFactory)
    name = factory.Sequence(lambda n: f'Community {n}')
    population = factory.Faker('random_int', min=100, max=10000)

# Usage in tests
@pytest.mark.django_db
def test_with_factory():
    community = CommunityFactory()
    assert community.id is not None
```

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=communities --cov-report=html

# Run specific test file
pytest tests/test_models.py

# Run specific test
pytest tests/test_models.py::TestCommunityModel::test_create_community

# Run tests matching pattern
pytest -k "test_create"

# Verbose output
pytest -v

# Stop on first failure
pytest -x
```

For code quality patterns, see [quality.md](quality.md).
