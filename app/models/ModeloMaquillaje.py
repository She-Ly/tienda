from .entities.Marca import Marca
from .entities.Maquillaje import Maquillaje

class ModeloMaquillaje():
    @classmethod
    def listar_maquillaje(self,db):
        try:
            cursor= db.connection.cursor()
            sql="SELECT maquillaje.codigo, maquillaje.tipo, maquillaje.fecha_lanzamiento, maquillaje.precio, marca.nombre, marca.origen FROM maquillaje JOIN marca  ON maquillaje.marca_id=marca.id ORDER BY maquillaje.tipo ASC"
            cursor.execute(sql)
            data=cursor.fetchall()
            maquillaje=[]
            for row in data:
                marc =Marca(0,row[4],row[5])
                maq =Maquillaje(row[0],row[1],marc, row[2],row[3])
                maquillaje.append(maq)
            return maquillaje


        except Exception as ex:
            raise Exception(ex)
