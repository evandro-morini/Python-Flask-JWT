- Banco de Dados MYSQL:
    - Via Python Console:
        - Criar Schema testeb
        - Para importar as tabelas / entidades através do console do Python: 
            - from app import db
            - db.create_all()
    - Via arquivo SQL:
        - Importar dump do arquivo testeb_dump.sql

- Para iniciar a API: python -m flask run

- Geração do token JWT:
    - http://127.0.0.1:5000/auth
    - Basic auth: email/senha do revendedor(exemplo => pedro.pereira@testeb.com.br/abc123)
    - O Token tem validade de 12h

- Demais funcionalidades:*
    - /revendedor/add;
    - /revendedor/validar_login;
    - /compra/add;
    - /compra/update/<id>;
    - /compra/delete/<id>;
    - /compra/list;
    - /compra/acumulado;
* Todas as rotas acima exigem Token válido

Dúvidas: evandro.morini@gmail.com
