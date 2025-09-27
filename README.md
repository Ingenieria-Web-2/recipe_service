# Recipe Service

A FastAPI-based microservice that handles recipe management for the DolceIQ platform.

## API Endpoints

The root of the endpoint is /api/recipe

### Public Endpoints

#### `GET /`

Service health check endpoint.

### Protected Endpoints

#### `POST /create`

Create a new recipe (requires authentication).

## Running (Docker)

From the orchestrator root directory, with the rest of service repositories cloned inside:

```bash
docker compose up --build
```

## Testing

From the orchestrator root:

```bash
make test-recipes
```
