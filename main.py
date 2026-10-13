from app.main import app

# This file serves as the entry point for Vercel and Hugging Face
# It imports the FastAPI instance from the app package
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)
