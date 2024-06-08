from fastapi import FastAPI


app  = FastAPI()


@app.get("/")
def main():
    return {"msg": "Hello!"}


@app.get("/users")
def get_all_users():
    pass