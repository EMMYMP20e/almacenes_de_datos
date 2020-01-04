import mysql.connector
from flask import Flask, render_template

# Méndez Pérez Emmanuel
# I5906 D07
# Almacenes de Datos
# Proyecto Final 
# Desarrollado en Python 3.7.5


app = Flask(__name__)

mydb = mysql.connector.connect(
    host="37.59.55.185",
    user="WCqgiEsLy3",
    passwd="I9yyxDyDIJ",
    database="WCqgiEsLy3"
)

cursor = mydb.cursor()
cursor.execute(
    "select municipio from preparatoria where" +
    " municipio = 'GUADALAJARA' or municipio = 'ZAPOPAN'" +
    " or municipio = 'SAN PEDRO TLAQUEPAQUE' or municipio = 'TONALA'" +
    " or municipio = 'TLAJOMULCO DE ZUÑIGA' or municipio ='EL SALTO'" +
    " or municipio = 'IXTLAHUACAN DE LOS MEMBRILLOS' or municipio ='JUANACATLAN'")
escuelas = cursor.fetchall()
cursor.execute(
    "select municipio from secundaria where" +
    " municipio = 'GUADALAJARA' or municipio = 'ZAPOPAN'" +
    " or municipio = 'SAN PEDRO TLAQUEPAQUE' or municipio = 'TONALA'" +
    " or municipio = 'TLAJOMULCO DE ZUÑIGA' or municipio ='EL SALTO'" +
    " or municipio = 'IXTLAHUACAN DE LOS MEMBRILLOS' or municipio ='JUANACATLAN'")
secundarias = cursor.fetchall()
cursor.execute(
    "select municipio from primaria where" +
    " municipio = 'GUADALAJARA' or municipio = 'ZAPOPAN'" +
    " or municipio = 'SAN PEDRO TLAQUEPAQUE' or municipio = 'TONALA'" +
    " or municipio = 'TLAJOMULCO DE ZUÑIGA' or municipio ='EL SALTO'" +
    " or municipio = 'IXTLAHUACAN DE LOS MEMBRILLOS' or municipio ='JUANACATLAN'")
primarias = cursor.fetchall()
for elemento in secundarias:
    escuelas.append(elemento)
for elemento in primarias:
    escuelas.append(elemento)
# print(escuelas)


mun = [0, 0, 0, 0, 0, 0, 0, 0]
for municipio in escuelas:
    if(municipio[0] == 'GUADALAJARA'):
        mun[0] += 1
    elif(municipio[0] == 'ZAPOPAN'):
        mun[1] += 1
    elif(municipio[0] == 'SAN PEDRO TLAQUEPAQUE'):
        mun[2] += 1
    elif(municipio[0] == 'TONALA'):
        mun[3] += 1
    elif(municipio[0] == 'TLAJOMULCO DE ZUÑIGA'):
        mun[4] += 1
    elif(municipio[0] == 'EL SALTO'):
        mun[5] += 1
    elif(municipio[0] == 'IXTLAHUACAN DE LOS MEMBRILLOS'):
        mun[6] += 1
    elif(municipio[0] == 'JUANACATLAN'):
        mun[7] += 1
print(mun)

@app.route('/')
def iniciaVentana():
    #return "Hola mundo"
    return render_template('mapa.html',escuelas=mun)


if __name__ == "__main__":
    app.run(debug=True)
