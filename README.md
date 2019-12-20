API Revendedores

Configuração
- MYSQL:
    - Via Python Console
        - Criar Schema testeb
        - Para importar as tabelas / entidades através do console do Python: 
            - from app import db
            - db.create_all()
    - Via arquivo SQL:
        - Importar dump do arquivo testeb_dump.sql

- Para iniciar a API - Dentro da pasta do projeto executar: python -m flask run

- Geração do token JWT
    - http://127.0.0.1:5000/auth
    - Basic auth: email/senha do revendedor(exemplo => pedro.pereira@testeb.com.br/abc123)
    - O Token tem validade de 12h

- Demais funcionalidades:*
    - /revendedor/add
    - /revendedor/validar_login
    - /compra/add
    - /compra/update/<id>
    - /compra/delete/<id>
    - /compra/list
    - /compra/acumulado
    
    Todas as rotas acima exigem Token válido (via GET)*
    
Ex: http://127.0.0.1:5000/compra/acumulado?cpf=12312312323&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InBlZHJvLnBlcmVpcmFAdGVzdGViLmNvbS5iciIsImV4cCI6MTU3NjgyMzE0M30.UF1OlduPEBSSPirTo5ctkNhbC1xgo5uBCNUdFoXC6Co

Dúvidas: evandro.morini@gmail.com
