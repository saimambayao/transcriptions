"""
Complete Pytest Test Template for Django

Copy this template for comprehensive testing.
"""

import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from TODO_app.models import TODOModelName


# ============================================================================
# FIXTURES
# ============================================================================

@pytest.fixture
def api_client():
    """API client for making requests."""
    return APIClient()


@pytest.fixture
def authenticated_client(api_client, user):
    """Authenticated API client."""
    token = Token.objects.create(user=user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
    return api_client


@pytest.fixture
def todo_instance(db, user, organization):
    """Create test TODOModelName instance."""
    return TODOModelName.objects.create(
        name='Test Instance',
        organization=organization,
        created_by=user,
        updated_by=user,
        status='DRAFT'
    )


# ============================================================================
# MODEL TESTS
# ============================================================================

@pytest.mark.django_db
class TestTODOModelName:
    """Test TODOModelName model."""
    
    def test_create_instance(self, user, organization):
        """Test creating instance."""
        instance = TODOModelName.objects.create(
            name='New Instance',
            organization=organization,
            created_by=user,
            updated_by=user
        )
        assert instance.id is not None
        assert instance.name == 'New Instance'
        assert instance.status == 'DRAFT'
    
    def test_string_representation(self, todo_instance):
        """Test __str__ method."""
        assert str(todo_instance) == 'Test Instance'
    
    def test_soft_delete(self, todo_instance, user):
        """Test soft delete."""
        todo_instance.delete(user=user)
        assert todo_instance.deleted_at is not None
        assert todo_instance.deleted_by == user
        assert TODOModelName.objects.count() == 0
    
    def test_restore(self, todo_instance, user):
        """Test restoring soft-deleted instance."""
        todo_instance.delete(user=user)
        todo_instance.restore()
        assert todo_instance.deleted_at is None
        assert TODOModelName.objects.count() == 1
    
    # TODO: Add model-specific tests
    # def test_validation(self):
    #     """Test model validation."""
    #     pass
    
    # def test_custom_method(self, todo_instance):
    #     """Test custom method."""
    #     result = todo_instance.custom_method()
    #     assert result is not None


# ============================================================================
# API TESTS
# ============================================================================

@pytest.mark.django_db
class TestTODOModelNameAPI:
    """Test TODOModelName API endpoints."""
    
    def test_list_requires_authentication(self, api_client):
        """Test list endpoint requires auth."""
        url = reverse('app:todomodelname-list')  # TODO: Update URL name
        response = api_client.get(url)
        assert response.status_code == 401
    
    def test_list_instances(self, authenticated_client, todo_instance):
        """Test listing instances."""
        url = reverse('app:todomodelname-list')  # TODO: Update URL name
        response = authenticated_client.get(url)
        assert response.status_code == 200
        assert len(response.data['results']) >= 1
    
    def test_create_instance(self, authenticated_client, organization):
        """Test creating instance via API."""
        url = reverse('app:todomodelname-list')  # TODO: Update URL name
        data = {
            'name': 'API Instance',
            'organization': organization.id,
            'status': 'DRAFT',
        }
        response = authenticated_client.post(url, data, format='json')
        assert response.status_code == 201
        assert TODOModelName.objects.filter(name='API Instance').exists()
    
    def test_retrieve_instance(self, authenticated_client, todo_instance):
        """Test retrieving single instance."""
        url = reverse('app:todomodelname-detail', args=[todo_instance.id])  # TODO: Update
        response = authenticated_client.get(url)
        assert response.status_code == 200
        assert response.data['name'] == 'Test Instance'
    
    def test_update_instance(self, authenticated_client, todo_instance):
        """Test updating instance."""
        url = reverse('app:todomodelname-detail', args=[todo_instance.id])  # TODO: Update
        data = {'name': 'Updated Name'}
        response = authenticated_client.patch(url, data, format='json')
        assert response.status_code == 200
        
        todo_instance.refresh_from_db()
        assert todo_instance.name == 'Updated Name'
    
    def test_delete_instance(self, authenticated_client, todo_instance):
        """Test deleting (soft delete) instance."""
        url = reverse('app:todomodelname-detail', args=[todo_instance.id])  # TODO: Update
        response = authenticated_client.delete(url)
        assert response.status_code == 204
        
        todo_instance.refresh_from_db()
        assert todo_instance.deleted_at is not None
    
    def test_filter_by_status(self, authenticated_client, todo_instance):
        """Test filtering by status."""
        url = reverse('app:todomodelname-list')  # TODO: Update URL name
        response = authenticated_client.get(url, {'status': 'DRAFT'})
        assert response.status_code == 200
        assert all(item['status'] == 'DRAFT' for item in response.data['results'])
    
    def test_search(self, authenticated_client, todo_instance):
        """Test search functionality."""
        url = reverse('app:todomodelname-list')  # TODO: Update URL name
        response = authenticated_client.get(url, {'search': 'Test'})
        assert response.status_code == 200
        assert len(response.data['results']) >= 1
    
    # TODO: Test custom actions
    # def test_approve_action(self, authenticated_client, todo_instance):
    #     """Test custom approve action."""
    #     url = reverse('app:todomodelname-approve', args=[todo_instance.id])
    #     response = authenticated_client.post(url)
    #     assert response.status_code == 200
    #     
    #     todo_instance.refresh_from_db()
    #     assert todo_instance.status == 'APPROVED'


# ============================================================================
# PERMISSION TESTS
# ============================================================================

@pytest.mark.django_db
class TestTODOModelNamePermissions:
    """Test permissions and access control."""
    
    def test_user_can_only_access_own_organization(
        self, authenticated_client, user, todo_instance
    ):
        """Test organization scoping."""
        # Create instance in different organization
        other_org = Organization.objects.create(name='Other Org', code='OTHER')
        other_instance = TODOModelName.objects.create(
            name='Other Instance',
            organization=other_org,
            created_by=user,
            updated_by=user
        )
        
        # Should not be able to access
        url = reverse('app:todomodelname-detail', args=[other_instance.id])
        response = authenticated_client.get(url)
        assert response.status_code == 404  # Or 403 depending on implementation
    
    # TODO: Add permission-specific tests
    # def test_only_staff_can_approve(self):
    #     """Test only staff can approve."""
    #     pass
