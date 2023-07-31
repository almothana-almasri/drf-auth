## Lab: Class 33 - Authentication & Production Server

**Author: Almothana Almasri**

## Testing

### 1. Get Tokens (JWT Authentication)

**Route:** `/api/token/`

**Method:** POST

**Token Required:** No

**Request:**

```bash
http POST http://127.0.0.1:8000/api/token/ username=<username> password=<password>
```

**Response:**

```json
{
    "access": "<access_token>",
    "refresh": "<refresh_token>"
}
```

### 2. Refresh Tokens

**Route:** `/api/token/refresh/`

**Method:** POST

**Token Required:** Yes (Refresh Token)

**Request:**

```bash
http POST http://127.0.0.1:8000/api/token/refresh/ refresh=<refresh_token>
```

**Response:**

```json
{
    "access": "<new_access_token>"
}
```

### 3. CRUD Route for Resource

**Route:** `/api/tasks/`

**Method:** GET

**Token Required:** No

**Description:** This route retrieves a list of all tasks.

**Sample Request:**

```bash
http GET http://127.0.0.1:8000/api/tasks/
```