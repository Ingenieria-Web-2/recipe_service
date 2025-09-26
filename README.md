# Recipe Service

A FastAPI-based microservice that handles recipe management for the DolceIQ platform.

## API Endpoints

### `GET /`

Service health check endpoint.

### `POST /create`

Create a new recipe (requires authentication).

## Local Development

### Prerequisites

- Docker & Docker Compose

### Environment Configuration

Create a `.env` file in the service directory with four environment variables:

```
DATABASE_URL=postgresql://user:password@recipe_db:5432/recipe_db
JWT_SECRET_KEY=your_secret_key_here
JWT_ALGORITHM=HS256
JWT_EXPIRATION_MINUTES=expiration_minutes
```

## Running (Docker)

From the orchestrator root directory, with the rest of service repositories cloned inside:

```bash
# Build and run the service
docker compose up --build
```

The service will be available through the API Gateway at `http://localhost/api/<service>/`.

## Testing

From the orchestrator root:

```bash
make test-recipes
```
