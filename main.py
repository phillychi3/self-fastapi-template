from app.core.app import app

if __name__ == "__main__":
    import uvicorn

    print("\n" + "=" * 60)
    print("FastAPI Server Starting...")
    print("=" * 60)
    print("API Documentation: http://localhost:8000/docs")
    print("Alternative Docs:  http://localhost:8000/redoc")
    print("API Base URL:      http://localhost:8000/api")
    print("=" * 60 + "\n")

    uvicorn.run(app, host="0.0.0.0", port=8000)
