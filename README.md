# API - CAPSTONE - FIND MY RECIPES

<br />

Este repositório destina-se ao projeto de conclusão, também chamado de Capstone, do Quarter 3 - Backend.

Será implementado em python com framework Flask e utilização do banco relacional PostgreSQL.

A proposta do projeto baseia-se na construção da API de acesso de outro projeto realizado no Capstone de conclusão de Frontend.

Em resumo o projeto de Frontend, acessível [aqui](https://capstone-dusky.vercel.app/), chama-se Find Recipes. É um site culinário, em que os visitantes tem possibilidade de cadastrar suas receitas, com moderação do Admin, e encontrar outras que sejam compatíveis com sua disponibilidade de ingredientes.

---

<br />

### URL DA API

A url base da API é [https://capstone-find-recipes.herokuapp.com](https://capstone-find-recipes.herokuapp.com/)

---

<br />

# Enpoints

A API tem N endpoints diferentes, para criação, atualização, deleção e obtenção de usuários, receitas, ingredientes, favorito e comentários.

---

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

<br />

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

<br />

## Get

<br />

**Rota necessita de autenticação**

`GET/user`

```json
NO BODY
```

Requisição **bem sucedida**, retorna a seguinte resposta.

`STATUS 200 - OK`

```json
{
	"user_id": "11a881f9-ddcc-4d5b-8ad8-704bdfc6217a",
	"name": "kenzinho jonson",
	"email": "kenzinho@mail.com",
	"links": {
		"recipes": "/user/11a881f9-ddcc-4d5b-8ad8-704bdfc6217a/recipe_by_user",
		"favorites_recipes": "/user/11a881f9-ddcc-4d5b-8ad8-704bdfc6217a/favorite_recipe",
		"feed": "/user/11a881f9-ddcc-4d5b-8ad8-704bdfc6217a/feed"
	}
}
```

---

<br />

## Update

<br />

**Rota necessita de autenticação**

`PATCH/user`

```json
{
	"name": "kenzinho jonson da silva"
}
```

Requisição **bem sucedida** , sem retorno.

`STATUS 204 - OK`

```json
{
	"user_id": "11a881f9-ddcc-4d5b-8ad8-704bdfc6217a",
	"name": "kenzinho jonson da silva",
	"email": "kenzinho@mail.com",
	"links": {
		"recipes": "/user/11a881f9-ddcc-4d5b-8ad8-704bdfc6217a/recipe_by_user",
		"favorites_recipes": "/user/11a881f9-ddcc-4d5b-8ad8-704bdfc6217a/favorite_recipe",
		"feed": "/user/11a881f9-ddcc-4d5b-8ad8-704bdfc6217a/feed"
	}
}
```

---

<br />

## Delete

<br />

**Rota necessita de autenticação**

`DELETE/user/<user_id>`

```json
NO BODY
```

Requisição **bem sucedida** , sem retorno.

`STATUS 204 - NO CONTENT`




















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
		"title": "Arroz Doce",
		"time": "40 minutos",
		"type": "Sobremesa",
		"method": "Coloca arroz e leite dentro da panela e ferve",
		"serves": 5,
		"img_link": "https://claudia.abril.com.br/wp-content/uploads/2020/02/receita-arroz-doce-light.jpg?quality=85&strip=info",
		"ingredients":[
			{
				"title": "arroz",
				"unit": "GRAMA",
				"amount": 100
			},
			{
				"title": "leite",
				"unit": "LITRO",
				"amount": 2
			}
		]
}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 201 - CREATED`

```json
{
	"recipe_id": 7,
	"title": "Arroz doce do jonson",
	"time": "40 minutos",
	"type": "Sobremesa",
	"method": "Coloca arroz e leite dentro da panela e ferve",
	"status": "MyEnum.NOT_VERIFIED",
	"serves": 5,
	"img_link": "https://claudia.abril.com.br/wp-content/uploads/2020/02/receita-arroz-doce-light.jpg?quality=85&strip=info",
	"user_id": 23471818027871931346858999649384407418,
	"ingredients": [
		{
			"ingredient_id": 1,
			"title": "arroz",
			"unit": [
				"g"
			],
			"amount": [,
				100.0
			]
		},
		{
			"ingredient_id": 6,
			"title": "leite",
			"unit": [
				"l"
			],
			"amount": [
				2.0,
			]
		}
	],
	"links": {
		"Show more": "/recipe/7"
	}
}
```

---

<br />

## Get

<br />

`GET/recipe`

```json
No body
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 200 - OK`

```json
[
	{
		"recipe_id": 6,
		"title": "Arroz Doce",
		"time": "40 minutos",
		"type": "Sobremesa",
		"method": "Coloca arroz e leite dentro da panela e ferve",
		"status": "MyEnum.NOT_VERIFIED",
		"serves": 5,
		"img_link": "https://claudia.abril.com.br/wp-content/uploads/2020/02/receita-arroz-doce-light.jpg?quality=85&strip=info",
		"user_id": 23471818027871931346858999649384407418,
		"ingredients": [
			{
				"ingredient_id": 1,
				"title": "arroz",
				"unit": [
					"kg",
					"g"
				],
				"amount": [
					2.0,
					100.0
				]
			},
			{
				"ingredient_id": 6,
				"title": "leite",
				"unit": [
					"l"
				],
				"amount": [
					2.0
				]
			}
		],
		"links": {
			"Show more": "/recipe/6"
		}
	}
]
```

---

<br />

## Get by Id

<br />

`GET/recipe/<recipe_id>`

```json
No body
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 200 - OK`

```json
{
	"recipe_id": 6,
	"title": "Arroz Doce",
	"time": "40 minutos",
	"type": "Sobremesa",
	"method": "Coloca arroz e leite dentro da panela e ferve",
	"status": "MyEnum.NOT_VERIFIED",
	"serves": 5,
	"img_link": "https://claudia.abril.com.br/wp-content/uploads/2020/02/receita-arroz-doce-light.jpg?quality=85&strip=info",
	"ingredients": [
		{
			"ingredient_id": 1,
			"title": "arroz",
			"unit": [
				"kg",
				"g"
			],
			"amount": [
				2.0,
				100.0
			]
		},
		{
			"ingredient_id": 6,
			"title": "leite",
			"unit": [
				"l"
			],
			"amount": [
				2.0
			]
		}
	]
}
```

---

<br />

## Get by Ingredient

<br />

`GET/recipe/ingredient?ingredient=leite`

```json
No body
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 200 - OK`

```json
{
	"recipes found with informed ingredients": [
		{
			"title": "Arroz Doce",
			"time": "40 minutos",
			"type": "Sobremesa",
			"serves": 5,
			"ingredients": [
				{
					"ingredient_id": 1,
					"title": "arroz",
					"unit": [
						"kg",
						"g"
					],
					"amount": [
						2.0,
						100.0
					]
				},
				{
					"ingredient_id": 6,
					"title": "leite",
					"unit": [
						"l"
					],
					"amount": [
						2.0
					]
				}
			],
			"links": {
				"Show more": "/recipe/6"
			}
		}
	]
}
```

---

<br />

## Get by Category

<br />

**Rota necessita de autenticação**

`GET/recipe/type/<type>`

```json
No body
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 200 - OK`

```json
[
	{
		"recipe_id": 6,
		"title": "Arroz Doce",
		"time": "40 minutos",
		"type": "Sobremesa",
		"method": "Coloca arroz e leite dentro da panela e ferve",
		"status": "MyEnum.NOT_VERIFIED",
		"serves": 5,
		"img_link": "https://claudia.abril.com.br/wp-content/uploads/2020/02/receita-arroz-doce-light.jpg?quality=85&strip=info",
		"user_id": 23471818027871931346858999649384407418,
		"ingredients": [
			{
				"ingredient_id": 1,
				"title": "arroz",
				"unit": [
					"kg",
					"g"
				],
				"amount": [
					2.0,
					100.0
				]
			},
			{
				"ingredient_id": 6,
				"title": "leite",
				"unit": [
					"l"
				],
				"amount": [
					2.0
				]
			}
		],
		"links": {
			"Show more": "/recipe/6"
		}
	}
]
```

---
<br />

## Patch

<br />

**Rota necessita de autenticação**

`PATCH/recipe/<recipe_id>`

```json
{
		"ingredients":[
			{
				"title": "arroz",
				"unit": "GRAMA",
				"amount": 100
			},
			{
				"title": "leite",
				"unit": "LITRO",
				"amount": 2
			},
			{
				"title": "canela",
				"unit": "UNIDADE",
				"amount": 10
			}
		]
}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 200 - OK`

```json
{
	"recipe_id": 6,
	"title": "Arroz Doce",
	"time": "40 minutos",
	"type": "Sobremesa",
	"method": "Coloca arroz e leite dentro da panela e ferve",
	"status": "MyEnum.NOT_VERIFIED",
	"serves": 5,
	"img_link": "https://claudia.abril.com.br/wp-content/uploads/2020/02/receita-arroz-doce-light.jpg?quality=85&strip=info",
	"user_id": 23471818027871931346858999649384407418,
	"ingredients": [
		{
			"ingredient_id": 1,
			"title": "arroz",
			"unit": [
				"g"
			],
			"amount": [
				100.0
			]
		},
		{
			"ingredient_id": 6,
			"title": "leite",
			"unit": [
				"l"
			],
			"amount": [
				2.0
			]
		},
		{
			"ingredient_id": 8,
			"title": "canela",
			"unit": [
				"unidade"
			],
			"amount": [
				10.0
			]
		}
	],
	"links": {
		"Show more": "/recipe/6"
	}
}

```

---

<br />

## Delete

<br />

**Rota necessita de autenticação**

`DELETE/recipe/<recipe_id>`

```json
NO BODY
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
{
	"recipes_id": 6
}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 200 - OK`

```json
{
	"message": "successfully added"
}
```

---

<br />

## Get

<br />

**Rota necessita de autenticação**

`GET/user/<user_id>/favorite_recipe`

```json
NO BODY
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 200 - OK`

```json
[
	{
		"title": "Arroz Doce"
	}
]
```

---

<br />

## Delete

<br />

**Rota necessita de autenticação**

`DELETE/favorites/<recipe-id>`

```json
NO BODY
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

`POST/feed`

### Icon não é um campo obrigatório.

```json
{
	"publication": "A receita de arroz doce com cerveja fica top",
	"icon": "miranha"
}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 201 - CREATED`

```json
{
	"user_name": "kenzinho jonson da silva",
	"feed_id": 3,
	"publication_date": "2022-05-04 15:37:31.095870",
	"publication": "A receita de arroz doce com cerveja fica top",
	"icon": "miranha"
}
```

---

<br />

## Get by Id

<br />

**Rota necessita de autenticação**

`GET/feed/<post-id>`

```json
NO BODY
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 200 - OK`

```json
{
	"user_name": "kenzinho jonson da silva",
	"feed_id": 3,
	"publication_date": "2022-05-04 15:37:31.095870",
	"publication": "A receita de arroz doce com cerveja fica top",
	"icon": "miranha"
}
```

---

<br />

## Get

<br />

**Rota necessita de autenticação**

`GET/feed/<post-id>`

```json
NO BODY
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 200 - OK`

```json
[
	{
		"user_name": "kenzinho",
		"feed_id": 1,
		"publication_date": "2022-05-04 11:52:05.230885",
		"publication": "4",
		"icon": null
	},
	{
		"user_name": "kenzinho jonson da silva",
		"feed_id": 2,
		"publication_date": "2022-05-04 15:36:31.185899",
		"publication": "A receita de arroz doce com cerveja fica top",
		"icon": null
	},
	{
		"user_name": "kenzinho jonson da silva",
		"feed_id": 3,
		"publication_date": "2022-05-04 15:37:31.095870",
		"publication": "A receita de arroz doce com cerveja fica top",
		"icon": "miranha"
	}
]
```

---

<br />

## Patch

<br />

**Rota necessita de autenticação**

`PATCH/feed/<post_id>`

```json
{
	"publication": "A receita de arroz doce com alcool fica top",
	"icon": "capetao america"
}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 200 - OK`

```json
{
	"user_name": "kenzinho",
	"feed_id": 1,
	"publication_date": "2022-05-04 11:52:05.230885",
	"publication": "A receita de arroz doce com alcool fica top",
	"icon": "capetao america"
}
```

---

<br />

## Delete

<br />

**Rota necessita de autenticação**

`DELETE/feed/<post_id>`

```json
NO BODY
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 204 - NO CONTENT`

```json
{}
```

---