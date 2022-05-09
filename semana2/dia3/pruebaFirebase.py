import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("token.json")
firebase_admin.initialize_app(cred)

#?para conectar a fireStore
from firebase_admin import firestore

db = firestore.client();

colProyectos = db.collection('proyecto')
docProyectos = colProyectos.get()

proyectoArray = []

for doc in docProyectos:
    proyecto = doc.to_dict()
    print(proyecto['nombre'])
    proyectoArray.append(proyecto)






    