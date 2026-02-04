from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="방화벽 로그 모니터링 API",
    description="방화벽 로그 모니터링 웹 어드민 백엔드 API",
    version="1.0.0"
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "방화벽 로그 모니터링 API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
