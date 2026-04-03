#!/usr/bin/env python3
"""
Generate pytest test boilerplate for Django models and APIs.

Usage:
    ./create_test.py <app_name> <model_name>
    ./create_test.py communities Community
"""

import sys

TEST_TEMPLATE = '''import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from {app_name}.models import {model_name}


@pytest.fixture
def {model_name_lower}(db, user, organization):
    """Create test {model_name_lower}."""
    return {model_name}.objects.create(
        name='Test {model_name}',
        organization=organization,
        created_by=user,
        updated_by=user
    )


@pytest.mark.django_db
class Test{model_name}Model:
    """Test {model_name} model."""
    
    def test_create_{model_name_lower}(self, user, organization):
        """Test creating {model_name_lower}."""
        {model_name_lower} = {model_name}.objects.create(
            name='New {model_name}',
            organization=organization,
            created_by=user,
            updated_by=user
        )
        assert {model_name_lower}.id is not None
        assert {model_name_lower}.name == 'New {model_name}'
    
    def test_{model_name_lower}_str(self, {model_name_lower}):
        """Test string representation."""
        assert str({model_name_lower}) == {model_name_lower}.name
    
    def test_soft_delete(self, {model_name_lower}, user):
        """Test soft delete."""
        {model_name_lower}.delete(user=user)
        assert {model_name_lower}.deleted_at is not None
        assert {model_name_lower}.deleted_by == user


@pytest.mark.django_db
class Test{model_name}API:
    """Test {model_name} API endpoints."""
    
    def test_list_requires_auth(self):
        """Test list requires authentication."""
        client = APIClient()
        url = reverse('{app_name}:{model_name_lower}-list')
        response = client.get(url)
        assert response.status_code == 401
    
    def test_list_{model_name_lower}s(self, user, {model_name_lower}):
        """Test listing {model_name_lower}s."""
        client = APIClient()
        token = Token.objects.create(user=user)
        client.credentials(HTTP_AUTHORIZATION=f'Token {{token.key}}')
        
        url = reverse('{app_name}:{model_name_lower}-list')
        response = client.get(url)
        assert response.status_code == 200
        assert len(response.data['results']) >= 1
    
    def test_create_{model_name_lower}(self, user, organization):
        """Test creating {model_name_lower} via API."""
        client = APIClient()
        token = Token.objects.create(user=user)
        client.credentials(HTTP_AUTHORIZATION=f'Token {{token.key}}')
        
        url = reverse('{app_name}:{model_name_lower}-list')
        data = {{
            'name': 'API {model_name}',
            'organization': organization.id,
            'status': 'ACTIVE',
        }}
        response = client.post(url, data, format='json')
        assert response.status_code == 201
        assert {model_name}.objects.filter(name='API {model_name}').exists()
    
    def test_update_{model_name_lower}(self, user, {model_name_lower}):
        """Test updating {model_name_lower} via API."""
        client = APIClient()
        token = Token.objects.create(user=user)
        client.credentials(HTTP_AUTHORIZATION=f'Token {{token.key}}')
        
        url = reverse('{app_name}:{model_name_lower}-detail', args=[{model_name_lower}.id])
        data = {{'name': 'Updated Name'}}
        response = client.patch(url, data, format='json')
        assert response.status_code == 200
        
        {model_name_lower}.refresh_from_db()
        assert {model_name_lower}.name == 'Updated Name'
'''

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    
    app_name = sys.argv[1]
    model_name = sys.argv[2]
    
    output = TEST_TEMPLATE.format(
        app_name=app_name,
        model_name=model_name,
        model_name_lower=model_name.lower()
    )
    
    print(output)
