# Readme

Este repositório destina-se ao projeto de conclusão, também chamado de Capstone, do Quarter 3 - Backend.

Será implementado em python com framework Flask e utilização do banco relacional PostgreSQL.

A proposta do projeto baseia-se na construção da API de acesso de outro projeto realizado no Capstone de conclusão de Frontend.

Em resumo o projeto de Frontend, acessível [aqui](https://capstone-dusky.vercel.app/), chama-se Find Recipes. É um site culinário, em que os visitantes tem possibilidade de cadastrar suas receitas, com moderação do Admin, e encontrar outras que sejam compatíveis com sua disponibilidade de ingredientes.

## Rotas de acesso da API - Endpoints

A url base da API é [https://capstone-find-recipes.herokuapp.com](https://capstone-find-recipes.herokuapp.com/)

### **São rotas não autenticadas**

### **Recipes**

- **Listar**
    
    É devolvido uma lista de 10 receitas cadastradas. As query params *page* e *per_page* são opcionais.
    
    `GET /recipe?page=1&per_page=10 - FORMATO DA REQUISIÇÃO`
    
    Caso dê tudo certo a resposta será:
    
    `FORMATO DA RESPOSTA - STATUS 200 - OK`
    
    Caso não haja receitas cadastradas, o retorno deverá ser uma lista vazia
    
    ```json
    [
    ]
    ```
    
- **Lista por categoria**
    
    É devolvido a lista completa de receitas da categoria informada
    
    `GET /recipe/type/<nome_categoria> - FORMATO DA REQUISIÇÃO`
    
    Caso dê tudo certo a resposta será:
    
    `FORMATO DA RESPOSTA - STATUS 200 - OK`
    
    ```bash
    [
    ]
    ```
    
    Caso não haja receitas cadastradas na categoria especificada, será retornado um erro
    
    `FORMATO DA RESPOSTA - STATUS 404 - NOT FOUND`
    
    ```bash
    {
    	"msg": "category does not exist"
    }
    ```
    
- **Recuperar uma receita**
    
    `GET /recipes/:id - FORMATO DA REQUISIÇÃO`
    
    Caso dê tudo certo a resposta será:
    
    `FORMATO DA RESPOSTA - STATUS 200 - OK`
    
    ```json
    {
    }
    ```
    
    Se o id não existir:
    
    `FORMATO DA RESPOSTA - STATUS 404 - NOT FOUND`
    
    ```bash
    {
    	"msg": "recipe does not exist"
    }
    ```
    
- **Listar por ingredientes**
    
    O usuário poderá filtrar receitas por ingredientes contidos neles e uma lista de correspondências será revolvida
    
    `GET /recipe/ingredient?ingredient=nome,ingredientes,separados,por,virgulas - FORMATO DA REQUISIÇÃO`
    
    Caso dê tudo certo a resposta será:
    
    `FORMATO DA RESPOSTA - STATUS 200 - OK`
    
    ```bash
    {
    	"recipes found with informed ingredients": [
    	]
    }
    ```
    
    Caso não seja encontrado receitas pelos parâmetros passados
    
    `FORMATO DA RESPOSTA - STATUS 404 - NOT FOUND`
    
    ```bash
    {
    	"ingredients doesn't found in any recipe": [
    	]
    }
    ```
    

### Users

- **Criar**
    
    `POST /users - FORMATO DA REQUISIÇÃO`
    
    ```json
    {
    	"name": "Murillo",
    	"email": "murillo@gmail.com",
    	"password": "123456"
    }
    ```
    
    Caso dê tudo certo a resposta será:
    
    `FORMATO DA RESPOSTA - STATUS 201 - CREATED`
    
    ```json
    {
      "email": "murillo@gmail.com",
      "name": "Murillo"
    }
    ```
    
    Se for enviado valores inválidos ou faltando:
    
    `FORMATO DA RESPOSTA - STATUS 400 - BAD REQUEST`
    
    ```bash
    {
      "msg": "Insufficient keys! Must be at least this keys ['name', 'email', 'password']"
    }
    ```
    
- **Logar**
    
    `POST /signin - FORMATO DA REQUISIÇÃO`
    
    ```json
    {
    	"email": "murillo@gmail.com",
    	"password": "123456"
    }
    ```
    
    Caso dê tudo certo a resposta será:
    
    `FORMATO DA RESPOSTA - STATUS 200 - OK`
    
    ```json
    
    ```
    
    Se for enviado valores inválidos ou faltando:
    
    `FORMATO DA RESPOSTA - STATUS 400 - BAD REQUEST`
    
    ```bash
    {
      "msg": "Insufficient keys! Must be at least this keys ['email', 'password']"
    }
    ```
    
    Se a autenticação não ocorrer por divergência entre email e password:
    
    `FORMATO DA RESPOSTA - STATUS 401 - UNAUTHORIEZED`
    
    ```bash
    {
      "msg": "Invalid email or password!"
    }
    ```
    
    Se o email não existir:
    
    `FORMATO DA RESPOSTA - STATUS 401 - UNAUTHORIEZED`
    
    ```bash
    {
      "msg": "Invalid email or password!"
    }
    ```
    

### **São rotas autenticadas**

Rotas que necessitam de autorização deve ser informado no cabeçalho da requisição o campo "Authorization", dessa forma:

```json
Authorization: Bearer {token}
```

### **Recipes**

A atualização e deleção só poderá acontecer por usuários, ou que sejam admin, ou que tenham criado a receita.

- **Atualizar**
    
    Poderá atualizar um ou mais items.
    
    `PATCH /recipes/:id - FORMATO DA REQUISIÇÃO`
    
    ```json
    {
    
    }
    ```
    
    Caso dê tudo certo a resposta será:
    
    `FORMATO DA RESPOSTA - STATUS 204 - NO CONTENT`
    
    Se for enviado valores inválidos:
    
    `FORMATO DA RESPOSTA - STATUS 400 - BAD REQUEST`
    
    Se o id não existir:
    
    `FORMATO DA RESPOSTA - STATUS 404 - NOT FOUND`
    
- **Criar**
    
    `POST /recipes - FORMATO DA REQUISIÇÃO`
    
    ```json
    {
    }
    ```
    
    Caso dê tudo certo a resposta será:
    
    `FORMATO DA RESPOSTA - STATUS 201 - CREATED`
    
    ```json
    
    ```
    
    Se for enviado valores inválidos:
    
    `FORMATO DA RESPOSTA - STATUS 400 - BAD REQUEST`
    
- **Apagar**
    
    `DELETE /recipes/:id - FORMATO DA REQUISIÇÃO`
    
    Caso dê tudo certo a resposta será:
    
    `FORMATO DA RESPOSTA - STATUS 204 - NO CONTENT`
    
    Se o id não existir:
    
    `FORMATO DA RESPOSTA - STATUS 404 - NOT FOUND`
    

### **Users**

- **Atualizar**
    
    Poderá atualizar um ou mais items.
    
    `PATCH /users/:id - FORMATO DA REQUISIÇÃO`
    
    ```json
    {
    
    }
    ```
    
    Caso dê tudo certo a resposta será:
    
    `FORMATO DA RESPOSTA - STATUS 204 - NO CONTENT`
    
    Se for enviado valores inválidos:
    
    `FORMATO DA RESPOSTA - STATUS 400 - BAD REQUEST`
    
    Se o id não existir:
    
    `FORMATO DA RESPOSTA - STATUS 404 - NOT FOUND`
    
- **Recuperar**
    
    O usuário só poderá ler informações de si.
    
    `GET /users/:id - FORMATO DA REQUISIÇÃO`
    
    Caso dê tudo certo a resposta será:
    
    `FORMATO DA RESPOSTA - STATUS 200 - OK`
    
    ```json
    {
    }
    ```
    
    Se o id não existir:
    
    `FORMATO DA RESPOSTA - STATUS 404 - NOT FOUND`
    
- **Apagar**
    
    `DELETE /users/:id - FORMATO DA REQUISIÇÃO`
    
    Caso dê tudo certo a resposta será:
    
    `FORMATO DA RESPOSTA - STATUS 204 - NO CONTENT`
    
    Se o id não existir:
    
    `FORMATO DA RESPOSTA - STATUS 404 - NOT FOUND`
    

### **Aprovar receitas**

 Acessível apenas por usuários admin.

- **Listar receitas não aprovadas**
    
    `GET /recipes/acceptance - FORMATO DA REQUISIÇÃO`
    
    Caso dê tudo certo a resposta será:
    
    `FORMATO DA RESPOSTA - STATUS 200 - OK`
    
    Caso não haja receitas aguardando aprovação, a rota deverá retornar uma lista vazia
    
    ```json
    [
    ]
    ```
    
- **Aprovar uma receita**
    
    `POST /recipes/:id/acceptante - FORMATO DA REQUISIÇÃO`
    
    Caso dê tudo certo a resposta será:
    
    `FORMATO DA RESPOSTA - STATUS 204 - NO CONTENT`
    
    Caso tenha informado um id de receita já aprovada, nenhum erro deve ser apresentado
    
    Se o id não existir:
    
    `FORMATO DA RESPOSTA - STATUS 404 - NOT FOUND`
    
- **Desaprovar uma receita antes aprovada**
    
    `POST /recipes/:id/acceptance?status=false - FORMATO DA REQUISIÇÃO`
    
    Caso dê tudo certo a resposta será:
    
    `FORMATO DA RESPOSTA - STATUS 204 - NO CONTENT`
    
    Caso tenha informado um id de receita já aprovada, nenhum erro deve ser apresentado
    
    Se o id não existir:
    
    `FORMATO DA RESPOSTA - STATUS 404 - NOT FOUND`
    

### Favoritar receitas

- **Listar receitas favoritadas**
    
    `GET /favorites - FORMATO DA REQUISIÇÃO`
    
    Caso dê tudo certo a resposta será:
    
    `FORMATO DA RESPOSTA - STATUS 200 - OK`
    
    ```json
    [
    ]
    ```
    
- **Adicionar favorito**
    
    `POST /favorites/:id - FORMATO DA REQUISIÇÃO`
    
    Caso dê tudo certo a resposta será:
    
    `FORMATO DA RESPOSTA - STATUS 204 - NO CONTENT`
    
    Se o id não existir:
    
    `FORMATO DA RESPOSTA - STATUS 404 - NOT FOUND`
    
- **Excluir favorito**
    
    `DELETE /favorites/:id - FORMATO DA REQUISIÇÃO`
    
    Caso o usuário não tenha o id favoritado, ou não exista, nenhum erro deverá ser informado.
    
    Caso dê tudo certo a resposta será:
    
    `FORMATO DA RESPOSTA - STATUS 204 - NO CONTENT`
    

### **Feed**

- **Listar**
    
    Os query params *page* e *per_page* são opcionais
    
    `GET /feeds?page=1&per_page=10 - FORMATO DA REQUISIÇÃO`
    
    Caso dê tudo certo a resposta será:
    
    `FORMATO DA RESPOSTA - STATUS 200 - OK`
    
    ```bash
    [
      {
        "user_name": "Murillo",
        "publication_date": "2022-05-04 02:27:31.367181",
        "icon": null,
        "feed_id": 8,
        "publication": "Hoje fiz a receita do chá indiano que amei"
      },
      {
        "user_name": "Murillo",
        "publication_date": "2022-05-04 02:28:22.403055",
        "icon": null,
        "feed_id": 9,
        "publication": "Gente, super recomendo o rocombole de carne"
      },
      {
        "user_name": "Murillo",
        "publication_date": "2022-05-04 02:29:51.228712",
        "icon": null,
        "feed_id": 10,
        "publication": "Estava eu navegando pelo site, quando encontrei a receita de bobô-de-camarão. Gente! Todo mundo amou aqui em casa."
      }
    ]
    ```
    
    Se for enviado valores inválidos ou faltando:
    
    `FORMATO DA RESPOSTA - STATUS 400 - BAD REQUEST`
    
- Recuperar uma publicação
    
    `GET /feeds/:id - FORMATO DA REQUISIÇÃO`
    
    Caso dê tudo certo a resposta será:
    
    `FORMATO DA RESPOSTA - STATUS 200 - OK`
    
    ```bash
    {
      "user_name": "Murillo",
      "publication_date": "2022-05-04 02:27:31.367181",
      "icon": null,
      "feed_id": 8,
      "publication": "Hoje fiz a receita do chá indiano que amei"
    }
    ```
    
    Se o id não existir:
    
    `FORMATO DA RESPOSTA - STATUS 404 - NOT FOUND`
    
    ```bash
    {
      "error": "ID not found"
    }
    ```
    
- **Publicar**
    
    `POST /feed - FORMATO DA REQUISIÇÃO`
    
    ```json
    {
    	"publication": "Estava eu navegando pelo site, quando encontrei a receita de bobô-de-camarão. Gente! Todo mundo amou aqui em casa."
    }
    ```
    
    Caso dê tudo certo a resposta será:
    
    `FORMATO DA RESPOSTA - STATUS 201 - CREATED`
    
    ```bash
    {
      "user_name": "Murillo",
      "publication_date": "2022-05-04 02:29:51.228712",
      "icon": null,
      "feed_id": 10,
      "publication": "Estava eu navegando pelo site, quando encontrei a receita de bobô-de-camarão. Gente! Todo mundo amou aqui em casa."
    }
    ```
    
    Se for enviado valores inválidos ou faltando:
    
    `FORMATO DA RESPOSTA - STATUS 400 - BAD REQUEST`
    
    ```bash
    {
      "error": "There are invalid keys in your request",
      "required_keys": [
        "publication"
      ],
      "invalid_key": [
        "chave"
      ]
    }
    ```
    
- **Atualizar**
    
    Deverá ser possível atualizar um ou todos os campos.
    
    `PATCH /feeds/:id - FORMATO DA REQUISIÇÃO`
    
    ```json
    {
    	"publication": "Fiz com minhas próprias mãos"
    }
    ```
    
    Caso dê tudo certo a resposta será:
    
    `FORMATO DA RESPOSTA - STATUS 200 - OK`
    
    ```bash
    {
      "user_name": "Murillo",
      "publication_date": "2022-05-04 02:36:05.749856",
      "icon": null,
      "feed_id": 11,
      "publication": "Fiz com minhas próprias mãos"
    }
    ```
    
    Se for enviado valores inválidos ou faltando:
    
    `FORMATO DA RESPOSTA - STATUS 400 - BAD REQUEST`
    
    ```bash
    {
      "error": "There are invalid keys in your request",
      "required_keys": [
        "publication"
      ],
      "invalid_key": [
        "chave"
      ]
    }
    ```
    
    Se o id não existir:
    
    `FORMATO DA RESPOSTA - STATUS 404 - NOT FOUND`
    
    ```bash
    {
      "msg": "Id not found"
    }
    ```
    
- **Excluir**
    
    `DELETE /feeds/:id - FORMATO DA REQUISIÇÃO`
    
    Caso dê tudo certo a resposta será:
    
    `FORMATO DA RESPOSTA - STATUS 204 - NO CONTENT`
    
    Se o id não existir:
    
    `FORMATO DA RESPOSTA - STATUS 404 - NOT FOUND`
    
    ```bash
    {
      "msg": "Id not found"
    }
    ```