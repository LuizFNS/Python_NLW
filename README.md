# Python_NLW

## Descrição
Python_NLW é um projeto desenvolvido com Flask e SQLAlchemy para a gestão de eventos e inscritos. Ele segue uma arquitetura modular, separando controllers, modelos e camadas de servidor para melhor organização e manutenção do código.

## Estrutura do Projeto
```
Python_NLW/
│── .vscode/
│── init/
│── src/
│   ├── controllers/
│   │   ├── events/
│   │   │   ├── __init__.py
│   │   │   ├── events_creator.py
│   │   ├── events_link/
│   │   │   ├── __init__.py
│   │   │   ├── events_link_creator.py
│   │   ├── subscribers/
│   │       ├── __init__.py
│   ├── http_types/
│   ├── main/
│   │   ├── server/
│   │   │   ├── routes/
│   │   │   │   ├── __init__.py
│   │   │   ├── server.py
│   │   │   ├── __init__.py
│   ├── model/
│   │   ├── configs/
│   │   ├── entities/
│   │   ├── repositories/
│   │   │   ├── __init__.py
│   │   ├── validators/
```

## Tecnologias Utilizadas
- Python 3
- Flask 3.1.0
- SQLAlchemy 2.0.38
- Cerberus 1.3.7
- Pytest 8.3.4

## Instalação
1. Clone este repositório:
   ```sh
   git clone https://github.com/seu-usuario/Python_NLW.git
   ```
2. Acesse o diretório do projeto:
   ```sh
   cd Python_NLW
   ```
3. Crie um ambiente virtual e ative-o:
   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```
4. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

## Uso
Para iniciar o servidor Flask:
```sh
python src/main/server/server.py
```
O servidor estará rodando em `http://localhost:5000/`

## Testes
Para rodar os testes automatizados:
```sh
pytest
```

## Contribuição
Sinta-se à vontade para contribuir! Basta criar um fork, fazer suas modificações e abrir um Pull Request.

## Licença
Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

