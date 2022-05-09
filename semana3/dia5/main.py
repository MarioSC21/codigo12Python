
from flask import Flask,jsonify,request
from flask_mysqldb import MySQL


app = Flask(__name__)

#* CONEXION A BASE DE DATOS
app.config['MYSQL_HOST'] ='localhost'
app.config['MYSQL_USER'] ='root'
app.config['MYSQL_PASSWORD'] ='Amigos01'
app.config['MYSQL_DB'] ='db_colegio'

mysql = MySQL(app)

@app.route('/')
def index():
    return jsonify({
        'status':'OK',
        'mensaje':'Bienvenido a mi api'
    })

@app.route('/alumno')
def getAlumno():
    cursor = mysql.connection.cursor()
    cursor.execute("select * from tbl_alumno")
    
    data = cursor.fetchall()
    
    cursor.close()
    
    print(data)
    return jsonify({
       'ok':True,
       'mensaje': 'lista de alumnos',
       'content': data
    })

@app.route('/alumno',methods=['POST'])
def setAlumno():
    nombre = request.json['nombre']
    celular = request.json['celular']
    github = request.json['github']
    
    cursor = mysql.connection.cursor()
    cursor.execute("insert into tbl_alumno(alumno_nombre,alumno_celular,alumno_github)values('"+nombre+"','"+celular+"','"+github+"')")
    
    mysql.connection.commit()
    cursor.close()
    return({
        'ok':True,
        'mensaje': 'registro insertado',
    })

@app.route('/alumno/<id>')
def getAlumnoById(id):
    cursor = mysql.connection.cursor()
    cursor.execute("select * from tbl_alumno where alumno_id = '"+ id +"'")
    
    data = cursor.fetchall()
    
    cursor.close()
    
    print(data)
    return jsonify({
       'ok':True,
       'mensaje': 'datos de alumnos',
       'content': data
    })
 
@app.route('/alumno/<id>',methods=['PUT'])
def updateAlumno(id):
    nombre = request.json['nombre']
    email = request.json['email']
    celular = request.json['celular']
    github = request.json['github']
    
    cursor = mysql.connection.cursor()
    sqlUpdateAlumno = "update tbl_alumno set "
    sqlUpdateAlumno += "alumno_nombre='"+ nombre +"',alumno_email='"+ email +"'"
    sqlUpdateAlumno += ",alumno_celular='"+ celular+"',alumno_github='"+ github +"' "
    sqlUpdateAlumno += "where alumno_id = '"+ id +"'"
    cursor.execute(sqlUpdateAlumno)
    
    mysql.connection.commit()
    
    cursor.close()
    
    return jsonify({
       'ok':True,
       'mensaje': 'datos de modificados'
    })

@app.route('/alumno/<id>',methods=['DELETE'])
def deleteAlumno(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("delete from tbl_alumno where alumno_id = '"+ id +"'")
        
        mysql.connection.commit()
        cursor.close()
        
        return jsonify({
        'ok':True,
        'mensaje': 'datos de eliminados'
        })
    except Exception as err:
        return jsonify({
        'ok':False,
        'mensaje': 'error no se puede eliminar : '+ str(err)
        }),501#EL ERROR A MOSTRAR
        
if __name__ == "__main__":
    app.run(debug=True,port=5000)
