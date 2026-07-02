import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from HO9app.routers import router

app = FastAPI(
    title="Secure Gateway Framework API",
    description="Implements robust user registration, secure bcrypt hashing, and dependency-guarded endpoints using signed JWTs.",
    version="1.0.0"
)

# 94. Configure Cross-Origin Resource Sharing (CORS) Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Permits local frontend dev servers to connect safely
    allow_credentials=True,
    allow_methods=["*"],  # Allows all standard methods (GET, POST, DELETE, etc.)
    allow_headers=["*"],  # Allows all authorization and validation headers
)

# Bind router components
app.include_router(router)

# =============================================================================
# 95. THEORETICAL ANALYSIS CODE COMMENT DISCUSSIONS:
# 
# How the OAuth2 Authorization Code Flow differs from Simple JWT Login:
#
# 1. Simple JWT Login (Our current implementation):
#    - The client app collects user credentials (email/password) directly via a form.
#    - The client sends them straight to the resource API backend server.
#    - The backend matches them and directly issues a signed JWT token access envelope.
#    - Best used for internal, first-party trust systems (like your company's own app).
#
# 2. OAuth2 Authorization Code Flow:
#    - Built specifically for third-party client integrations without exposing credentials.
#    - The client redirects the user to an external Authorization Server (e.g., Log in with Google).
#    - The user authenticates there, and that server issues a temporary authorization code back to the client.
#    - The client backend exchanges that short-lived code securely for an access token.
#    - Key Value: The third-party app handles the resource token but never sees or handles the user's password.
# =============================================================================

if __name__ == "__main__":
    # Launch uvicorn locally on port 8000
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)