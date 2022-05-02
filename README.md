# API - CAPSTONE - FIND MY RECIPES

O Find my Recipes é uma aplicação, para cadastrar receitas juntamente com seus ingredientes, podendo tambem favorita-los e escrever comentários.

<br />

#### URL DA API

https://capstone-find-recipes.herokuapp.com

<br />

# Enpoints

A API tem N endpoints diferentes, para criação, atualização, deleção e obtenção de usuários, receitas, ingredientes, favorito e comentários.

<br />













## **Users**

---

<br />


## Post/Register

<br />

`POST/user`

```json
{
	"name": "kenzinho",
	"email": "kenzinho@mail.com",
	"password": "kenzie123"
}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 201 - CREATED`

```json
{
	"name": "kenzinho",
	"email": "kenzinho@mail.com"
}
```

---

## Post/Login

<br />

`POST/user/login`

```json
{
	"email": "kenzinho@mail.com",
	"password": "kenzie123"
}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 200 - OK`

```json
{
	"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1MTM2MTY2NSwianRpIjoiYTA2ZWMyNWMtYWU5Mi00MTIxLWE3ZWUtOWY5Yjk4Y2YxYjAwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJ1c2VyX2lkIjoiNGZlMWQxNzctMGFmOS00ZDA2LThlYzUtY2Q3NTIxZTMxOWFlIiwibmFtZSI6ImtlbnppbmhvIiwiZW1haWwiOiJrZW56aW5ob0BtYWlsLmNvbSJ9LCJuYmYiOjE2NTEzNjE2NjUsImV4cCI6MTY1MTM2MjU2NX0.0mX4CyLuC1D5qOQH-dQOA1qT7JexEuou1hy1Xcrcki0"
}
```

---

## Get

<br />

**Rota necessita de autenticação**

`GET/user/<user_id>`

```json
No body
```

Requisição **bem sucedida**, retorna a seguinte resposta.

`STATUS 200 - OK`

```json
{}
```

---

## Get All

<br />


`GET/user`

```json
{}
```

Requisição **bem sucedida**, retorna a seguinte resposta.

`STATUS 200 - OK`

```json
{}
```

---

<br />

<!-- ## Update

<br />

**Rota necessita de autenticação**

`PATCH/user`

```json
{
	"email": "kenzinho@mail.com"
}
```

Requisição **bem sucedida** , sem retorno.

`STATUS 204 - NO CONTENT`

---

## Delete

<br />

**Rota necessita de autenticação**

`DELETE/user`

{}

Requisição **bem sucedida** , sem retorno.

`STATUS 204 - NO CONTENT` -->




















<br />

## **Recipes**

---

<br />


## Post

<br />

**Rota necessita de autenticação**

`POST/recipe`

```json
{
	"title": "arroz",
	"time": "20 minutos",
	"type": "fácil",
	"method": "coloca na panela e deixa lá",
	"serves": 3,
	"img_link": "google.com",
	"user_id": "897a3c7e-6ef9-428d-b729-076016fe1a30"
}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 201 - CREATED`

```json
{}
```

---


## Get All

<br />

**Rota necessita de autenticação**

`GET/recipe`

```json
No body
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 200 - OK`

```json
{}
```

---

## Get by Id

<br />

**Rota necessita de autenticação**

`GET/recipe/<recipe_id>`

```json
No body
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 200 - OK`

```json
{}
```

---

## Patch

<br />

**Rota necessita de autenticação**

`PATCH/recipe`

```json
{}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 200 - OK`

```json
{}
```

---


## Delete

<br />

**Rota necessita de autenticação**

`DELETE/recipe/<recipe_id>`

```json
{}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 204 - NO CONTENT`

```json
{}
```

---


<br />

















## **Favorites**

---

<br />


## Post

<br />

**Rota necessita de autenticação**

`POST/favorites`

```json
{}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 201 - CREATED`

```json
{}
```

---

## Get

<br />

**Rota necessita de autenticação**

`GET/favorites`

```json
{}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 200 - OK`

```json
[{}]
```

---

## Patch

<br />

**Rota necessita de autenticação**

`PATCH/favorites/<user_id>`

```json
{}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 200 - OK`

```json
{}
```

---

## Delete

<br />

**Rota necessita de autenticação**

`DELETE/favorites/<user_id>`

```json
{}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 204 - NO CONTENT`

```json
{}
```

---

<br />



















## **Feeds**

---

<br />

## Post

<br />

**Rota necessita de autenticação**

`POST/feed/<recipe-id>`

```json
{}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 201 - CREATED`

```json
{}
```

---

## Get by Id

<br />

**Rota necessita de autenticação**

`GET/feed/<recipe-id>`

```json
{}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 200 - OK`

```json
{}
```

---

## Patch

<br />

**Rota necessita de autenticação**

`PATCH/feed/...`

```json
{}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 200 - OK`

```json
{}
```

---

## Delete

<br />

**Rota necessita de autenticação**

`DELETE/feed/...`

```json
{}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 204 - NO CONTENT`

```json
{}
```

---