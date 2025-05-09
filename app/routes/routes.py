@app.get("/")
async def root():
    return {"message": "Welcome to Todo app"} 

