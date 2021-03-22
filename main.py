from flask import Flask
from app import models
from app.db import SessionLocal, engine
from flask import request
app = Flask(__name__)

@app.route("/receive_data/",  methods=['POST'])
def receive_data():
    if request.method == 'POST':
        # Nessa variavel nós temos o Dicionário (JSON) que foi enviado 
        # pelo post...
        received_data = request.json
        print(f"RECEBEU OS SEGUINTES DADOS:\n{received_data}")
                
        # Aqui Vai a Lógica do Programa.                
        #   Aqui fazemos uma Query e salvamos o resultado na variavel usuarios
        usuarios = query_db("SELECT * FROM users;")
        #   Caso houver usuários no Banco de dados, retorna um Dicionário com os mesmos
        #   e printa no console        
        print(usuarios)
        
        
        # Responde ao client que chamou (Pode responder string ou Json)
        return "OK"
        
    else:
        return "METODO NÃO ACEITO"


@app.route("/retrieve_data/",  methods=['GET'])
def retrieve_data():
    # Aqui retorna como um Dicionário (JSON) os dados que você quer enviar 
    # ao client    
    usuarios = query_db("SELECT * FROM users;")
    return {"result":usuarios}


def query_db(query):    
    #   Aqui abrimos a conexão com o banco de dados para fazer querys..
    with engine.connect() as conn:
        result = conn.execute(query)
        if "select" in query.lower():
            return [{column: value for column, value in row._mapping.items()} for row in result]
        else:
            return True

# if __name__ == '__main__':
models.Base.metadata.create_all(bind=engine)
app.run(host='0.0.0.0', debug=True, port=5000)
