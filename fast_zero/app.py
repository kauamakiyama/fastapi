from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from fast_zero.schemas import Message, UserDB, UserList, UserPublic, UserSchema

database = []

app = FastAPI()


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Olá Mundo!"}


@app.post("/users/", status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_users(user: UserSchema):  # entrada
    user_com_id = UserDB(
        id=len(database) + 1,
        **user.model_dump(),  # converte obj do pydentic em um dicionario
    )

    database.append(user_com_id)
    return user_com_id


@app.get("/users/", response_model=UserList)
def read_users():
    return {"users": database}


@app.put("/users/{user_id}", response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    # Valida se o usuário existe no banco de dados
    if user_id > len(database) or user_id <= 0:
        raise HTTPException(status_code=404, detail="User not found")

    # Cria o novo objeto de usuário com o ID existente
    user_com_id = UserDB(**user.model_dump(), id=user_id)

    # Atualiza o banco de dados
    database[user_id - 1] = user_com_id

    # Retorna o objeto atualizado
    return user_com_id


@app.delete("/users/{user_id}", response_model=Message)
def delete_user(user_id: int):
    # Validar se o usuário existe no banco
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="User not found"
        )

    database.pop(user_id - 1)

    # Retornar mensagem de sucesso
    return {"message": "User deleted"}

@app.get('/users/{id}', response_model=UserPublic)
def get_user(id: int):
    if id < 1 or id > len(database):  # Valida se o ID está dentro do intervalo válido
        raise HTTPException(
            status_code=404, 
            detail="User not found"
        )
    
    return database[id - 1]  # Subtrai 1 para acessar o índice correto



