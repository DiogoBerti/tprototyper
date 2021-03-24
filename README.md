# tprototyper
Prototipador em Flask.

Para utilização é necessário ter o Docker e DockerCompose instalados na Maquina

# Utilização
Navegue até a pasta do projeto e roder `docker-compose up --build`
A aplicação ficará disponível em http://localhost:5000

# Rotas inicias
Para recebimento de dados, fazer um post para `receive_data`.
Para resgatar dados, fazer um get para `retrieve_data`.

Exemplos:
- ``` http://localhost:5000/retrieve_data ```

# PG Admin.
Para utilização do PGADMIN, abrir o navegador no endereço http://localhost:5050, será necessário incluir Usuário e senha:
- User: admin@admin.com
- Senha: pwdpwd

Na primeira utilização será necessário setar a conexão ao banco:
- Clicar em servers com botão direito > Create > Server.
- Ao entrar na tela de criação, preencher os seguintes dados:
- Name: Pode colocar o que preferir (é obrigatório)
- Na Aba connection:
- - Host:                 db_prot
- - Maintenance Database: prototyper
- - Username:             prototyper
- - Password:             admin
- Clique em save
- Após isso, Abra o server, vá em databases > prototyper > Schemas > Public > Tables.
- Clique com o botão direito na tabela que quer acessar e escolha a opção (normalmente utilizamos Scripts)