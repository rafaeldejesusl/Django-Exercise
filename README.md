# Django-Exercise

O projeto Django Exercise apresenta uma API REST que faz o gerenciamento das informações relativas a um cadastro de clientes. A aplicação foi desenvolvida em Python, com o auxílio dos frameworks Django e DjangoRest. Os dados são armazenados num banco de dados SQLite.

## Inicialização

Primeiramente, faça o clone do projeto na sua máquina:

- ```git clone git@github.com:rafaeldejesusl/Django-Exercise.git```

Entre na pasta do projeto:

- ```cd Django-Exercise/```

Para rodar a aplicação, utilize os seguintes comandos:

- ```python3 -m venv venv && source venv/bin/activate```

- ```python3 -m pip install -r dev-requirements.txt```

OBS: Caso apareça algum erro na instalação, repita o comando anterior;

- ```python manage.py runserver```

A aplicação estará acessível no seguinte endereço: http://localhost:8000

## Testes

Foram realizados alguns testes na aplicação utilizando as ferramentas para testar APIs do framework DjangoRest, executados através do seguinte comando:

- ```python manage.py test```

## Feedbacks

Caso tenha alguma sugestão ou tenha encontrado algum erro no código, estou disponível para contato no meu [LinkedIn](https://www.linkedin.com/in/rafael-de-jesus-lima/)
