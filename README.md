
# API REST para a criaçao de recursos

## Tecnologias

Neste projeto foi usado as seguintes tecnologias,
Django framework,
Django REST Framework,
Linguagem de programação Python e
Banco de dados postgres.

## Sobre o Projeto

[Django](https://www.djangoproject.com/) é um framework muito estável onde existe uma comunidade sempre trabalhando para melhorias
deixando sempre atualizado, corrigindo bugs e melhorando a segurança.

[Django REST](http://www.django-rest-framework.org/) foi usado para criar o API REST responsável pela integração, esse framework é bem robusto e atende as necessidades de um grande ou pequeno projeto umas da vantagens dele é a grande familiaridade com o Django tornando assim uma programação mais simples para manutenção e melhorias do projeto

Banco de dados [postgres](https://www.sqlite.org/)

**Estrutura Shoe**

```json
    {
        "sku": "SA232SHF27GEI", // SKU do produto
        "name": "Slip On Santa Lolla Suede Bege", // Nome
        "details": "Slip On Santa Lolla Suede Bege Tipo de Produto: Slip OnOcasião/Estilo: CasualMaterial Externo: TêxtilMaterial Interno: SintéticoMaterial da Sola: Sintético", // Detalhes
        "informations": {
            "Cor": "Bege", // Informaçoes, é um campo dinamico para se inserir qualquer dado
            "Modelo": "Santa Lolla 01AC.11E4.0048.0157",
            "Tipo de frete:": "Leve"
        },
        "tags": [
            "Santa Lolla",
            "Tênis Santa Lolla", // Tags do produto
            "Bege",
            "Tênis"
        ],
        "price": 84.915, // preço
        "sizes": [ // tamanhos disponiveis para o sapato
            {
            "size": 42,
            "available_quantity": 5
            },
            {
            "size": 34,
            "available_quantity": 13
            },
            {
            "size": 34,
            "available_quantity": 10
            }
        ]
        }
    }
```

## Filtragem

Para executar uma filtragem é preciso passar como parâmetro o atributo desejado que deseja filtrar eo valor na requisição, por exemplo:

`http://127.0.0.1:8000/shoe/?name=Jordan XV`

## Como rodar

Criei um [docker-compose.yml](https://hub.docker.com/) e disponibilizei as dockers no docker hub [hub easyresourcefront](hhttps://cloud.docker.com/u/arturribeiro/repository/docker/arturribeiro/easyresourcefront)
[hub easyresource](https://cloud.docker.com/u/arturribeiro/repository/docker/arturribeiro/easyresource)


https://cloud.docker.com/u/arturribeiro/repository/docker/arturribeiro/easyresource
Então para rodar o projeto é só executar o comando:

é só executar docker-compose up -d e logo em seguida executar este comando para que o 
database seja criado: 

    docker exec -it postgres bin/sh

    e logo em seguida executar este.

    PGPASSWORD=postgres psql -h postgres -p 5432  -U postgres -c "CREATE DATABASE easyResource;"

## Extra

Para criar uma massa de dados para se usar na rota csv_import criei taxmbém um web scraping para coletar os calçados contidos na dafiti.
O repositório da interface é esse [https://github.com/arturAdr/easyResourceFront](https://github.com/arturAdr/easyResourceFront)
