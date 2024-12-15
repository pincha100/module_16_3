from fastapi import FastAPI, Path
from typing import Annotated

# Создаем приложение FastAPI
app = FastAPI()

# Инициализируем словарь пользователей
users = {"1": "Имя: Example, возраст: 18"}

# GET-запрос для получения всех пользователей
@app.get("/users")
def get_users():
    return users

# POST-запрос для добавления нового пользователя
@app.post("/user/{username}/{age}")
def create_user(
    username: Annotated[str, Path(title="Enter username", min_length=5, max_length=20)],
    age: Annotated[int, Path(title="Enter age", ge=18, le=120)],
):
    # Генерируем новый ключ (максимальный + 1)
    new_id = str(max(map(int, users.keys())) + 1)
    # Добавляем пользователя в словарь
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return {"message": f"User {new_id} is registered"}

# PUT-запрос для обновления данных пользователя
@app.put("/user/{user_id}/{username}/{age}")
def update_user(
    user_id: Annotated[str, Path(title="Enter user ID")],
    username: Annotated[str, Path(title="Enter username", min_length=5, max_length=20)],
    age: Annotated[int, Path(title="Enter age", ge=18, le=120)],
):
    if user_id in users:
        # Обновляем данные пользователя
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return {"message": f"The user {user_id} is updated"}
    return {"error": f"User {user_id} not found"}

# DELETE-запрос для удаления пользователя
@app.delete("/user/{user_id}")
def delete_user(
    user_id: Annotated[str, Path(title="Enter user ID")]
):
    if user_id in users:
        # Удаляем пользователя
        del users[user_id]
        return {"message": f"User {user_id} has been deleted"}
    return {"error": f"User {user_id} not found"}