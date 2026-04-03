# Error-Specific Investigation Workflows

This reference provides detailed investigation procedures for common error types in OBCMS.

## Table of Contents

1. [HTMX Request Failures](#htmx-request-failures)
2. [Django ORM Performance Issues](#django-orm-performance-issues)
3. [Celery Task Failures](#celery-task-failures)
4. [Railway Deployment Issues](#railway-deployment-issues)
5. [PostgreSQL Database Issues](#postgresql-database-issues)
6. [Authentication/Authorization Issues](#authenticationauthorization-issues)
7. [Frontend JavaScript Errors](#frontend-javascript-errors)
8. [API Endpoint Failures](#api-endpoint-failures)

---

## HTMX Request Failures

### Investigation Steps

1. **Check Production Logs**
   - Run: `railway logs --tail 100` to see recent logs
   - Search for the specific request path and error traces
   - Look for HTTP status codes (500, 400, 403, etc.)

2. **Analyze Request/Response**
   - Examine the HTMX attributes (`hx-get`, `hx-post`, `hx-target`, etc.)
   - Check if the endpoint URL is correct
   - Verify CSRF token inclusion for POST requests
   - Check `hx-swap` strategy matches response type

3. **Review Django View**
   - Locate the view handling the HTMX request
   - Check for proper error handling
   - Verify template rendering logic
   - Check for missing context variables

4. **Research Online**
   - Search: "HTMX [specific error] Django"
   - Check HTMX official documentation
   - Look for similar issues in HTMX GitHub issues
   - Review Django HTMX integration patterns

5. **Common Causes**
   - CSRF token mismatch
   - Incorrect swap target selector
   - Missing view permissions/authentication
   - Template rendering errors
   - Incorrect content type in response

### Key Research Sources

- HTMX Official Docs: https://htmx.org/docs/
- Django-HTMX Library: https://github.com/adamchainz/django-htmx
- HTMX GitHub Issues: https://github.com/bigskysoftware/htmx/issues
- Stack Overflow: "django htmx [error]"

---

## Django ORM Performance Issues

### Investigation Steps

1. **Enable Query Logging**
   - Add Django Debug Toolbar or use `connection.queries`
   - Count queries executed for the slow page
   - Identify N+1 query patterns

2. **Analyze Query Patterns**
   - Look for missing `select_related()` on ForeignKey fields
   - Look for missing `prefetch_related()` on ManyToMany/reverse FK
   - Check for queries inside loops
   - Identify duplicate queries

3. **Check Database Indexing**
   - Review model fields used in filters
   - Check if `db_index=True` is set on frequently queried fields
   - Examine foreign key indexes
   - Review PostgreSQL query plans with `EXPLAIN ANALYZE`

4. **Research Online**
   - Search: "Django ORM N+1 optimization"
   - Search: "Django select_related vs prefetch_related"
   - Check Django documentation on query optimization
   - Look for PostgreSQL indexing best practices

5. **Benchmark Solutions**
   - Measure query count before/after optimization
   - Compare query execution time
   - Test with production-like data volume

### Key Research Sources

- Django Query Optimization: https://docs.djangoproject.com/en/stable/topics/db/optimization/
- Django Select Related: https://docs.djangoproject.com/en/stable/ref/models/querysets/#select-related
- PostgreSQL Performance: https://www.postgresql.org/docs/current/performance-tips.html
- Django Debug Toolbar: https://django-debug-toolbar.readthedocs.io/

---

## Celery Task Failures

### Investigation Steps

1. **Check Celery Worker Logs**
   - Railway: `railway logs --tail 200` and filter for Celery worker process
   - Look for task execution errors
   - Check for timeout issues
   - Identify retry patterns

2. **Examine Task Configuration**
   - Review task timeout settings (`time_limit`, `soft_time_limit`)
   - Check retry configuration (`max_retries`, `retry_backoff`)
   - Verify broker connection (Redis) settings
   - Check for proper task signatures

3. **Analyze Task Code**
   - Look for unhandled exceptions
   - Check for blocking operations
   - Verify database transaction handling
   - Review resource cleanup (connections, files)

4. **Research Online**
   - Search: "Celery intermittent failures [specific error]"
   - Check Celery best practices documentation
   - Look for similar issues in Celery GitHub issues
   - Review Redis connection reliability patterns

5. **Common Causes**
   - Task timeout exceeded
   - Redis connection drops
   - Database connection pool exhaustion
   - Memory leaks in long-running tasks
   - Unhandled exceptions in task code

### Key Research Sources

- Celery Best Practices: https://docs.celeryq.dev/en/stable/userguide/tasks.html#best-practices
- Celery Error Handling: https://docs.celeryq.dev/en/stable/userguide/tasks.html#error-handling
- Celery GitHub Issues: https://github.com/celery/celery/issues
- Redis Reliability: https://redis.io/docs/manual/patterns/distributed-locks/

---

## Railway Deployment Issues

### Investigation Steps

1. **Check Railway Deployment Logs**
   - View build logs for compilation errors
   - Check deployment logs for startup failures
   - Look for environment variable issues
   - Review resource limits (memory, CPU)

2. **Verify Configuration**
   - Check `railway.json` or `Procfile` configuration
   - Verify environment variables are set correctly
   - Review Django settings for production
   - Check static files collection

3. **Analyze Resource Usage**
   - Monitor memory consumption
   - Check for memory leaks
   - Review concurrent request handling
   - Verify worker/thread configuration

4. **Research Online**
   - Search: "Railway Django deployment [specific error]"
   - Check Railway documentation
   - Look for Django production deployment best practices
   - Review Gunicorn/WSGI server configuration

### Key Research Sources

- Railway Documentation: https://docs.railway.app/
- Django Deployment Checklist: https://docs.djangoproject.com/en/stable/howto/deployment/checklist/
- Gunicorn Configuration: https://docs.gunicorn.org/en/stable/configure.html

---

## PostgreSQL Database Issues

### Investigation Steps

1. **Check Database Logs**
   - Railway: Access PostgreSQL logs through Railway dashboard
   - Look for connection errors
   - Check for query timeouts
   - Review deadlock warnings

2. **Analyze Query Performance**
   - Use `EXPLAIN ANALYZE` on slow queries
   - Check for missing indexes
   - Review table statistics (`ANALYZE` command)
   - Identify sequential scans on large tables

3. **Check Connection Pool**
   - Verify `CONN_MAX_AGE` setting
   - Monitor active connections
   - Check for connection leaks
   - Review connection pool size

4. **Research Online**
   - Search: "PostgreSQL slow query optimization"
   - Check PostgreSQL official documentation
   - Look for Django PostgreSQL best practices
   - Review connection pooling patterns

### Key Research Sources

- PostgreSQL Performance: https://www.postgresql.org/docs/current/performance-tips.html
- Django PostgreSQL: https://docs.djangoproject.com/en/stable/ref/databases/#postgresql-notes
- PgBouncer (connection pooling): https://www.pgbouncer.org/

---

## Authentication/Authorization Issues

### Investigation Steps

1. **Check User Permissions**
   - Verify user role and organization assignment
   - Check model-level permissions
   - Review view decorator permissions (`@permission_required`, `@login_required`)
   - Examine RBAC configuration

2. **Analyze Request Context**
   - Check session data
   - Verify authentication middleware
   - Review user authentication backend
   - Check for CORS issues (if API)

3. **Review Django Auth Flow**
   - Trace authentication pipeline
   - Check custom authentication backends
   - Verify password validation
   - Review session configuration

4. **Research Online**
   - Search: "Django permission denied [specific scenario]"
   - Check Django authentication documentation
   - Look for multi-tenant permission patterns
   - Review Django Guardian (object permissions) docs

### Key Research Sources

- Django Authentication: https://docs.djangoproject.com/en/stable/topics/auth/
- Django Permissions: https://docs.djangoproject.com/en/stable/topics/auth/default/#permissions-and-authorization
- Django Guardian: https://django-guardian.readthedocs.io/

---

## Frontend JavaScript Errors

### Investigation Steps

1. **Check Browser Console**
   - Use Chrome DevTools to view console errors
   - Check for CSP violations
   - Look for missing resources (404s)
   - Review network tab for failed requests

2. **Verify CSP Compliance**
   - Check if inline scripts are blocked
   - Verify CSP headers in response
   - Review `django-csp` configuration
   - Check for `unsafe-inline` usage

3. **Analyze JavaScript Code**
   - Check for syntax errors
   - Verify variable scope issues
   - Review event listener bindings
   - Check for race conditions

4. **Research Online**
   - Search: "CSP violation [specific error]"
   - Check MDN Web Docs for JavaScript errors
   - Look for Django CSP best practices
   - Review HTMX JavaScript integration patterns

### Key Research Sources

- MDN JavaScript Errors: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors
- Django CSP: https://django-csp.readthedocs.io/
- CSP Reference: https://content-security-policy.com/

---

## API Endpoint Failures

### Investigation Steps

1. **Check API Response**
   - Review HTTP status code
   - Examine response body/error message
   - Check response headers
   - Verify content type

2. **Analyze DRF Configuration**
   - Check serializer validation
   - Review permission classes
   - Verify authentication classes
   - Check throttling settings

3. **Review Request Data**
   - Validate request payload format
   - Check required fields
   - Verify data types
   - Review nested relationships

4. **Research Online**
   - Search: "Django REST Framework [specific error]"
   - Check DRF official documentation
   - Look for serializer validation patterns
   - Review API design best practices

### Key Research Sources

- DRF Documentation: https://www.django-rest-framework.org/
- DRF Serializers: https://www.django-rest-framework.org/api-guide/serializers/
- REST API Best Practices: https://restfulapi.net/

---

## General Investigation Principles

1. **Start Local, Then Production**
   - Try to reproduce the error locally first
   - Compare local vs production configurations
   - Check environment-specific settings

2. **Gather Evidence Before Researching**
   - Collect logs, error messages, stack traces
   - Document the exact steps to reproduce
   - Note what was changed recently

3. **Prioritize Official Documentation**
   - Official docs over blog posts
   - GitHub issues for known bugs
   - Stack Overflow for common patterns
   - Recent sources over outdated ones

4. **Validate Hypotheses**
   - Don't assume - test each theory
   - Use minimal reproducible examples
   - Isolate variables one at a time
