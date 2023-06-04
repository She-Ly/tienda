from .entities.Usuario import Usuario
from .entities.TipoUsuario import TipoUsuario

class ModeloUsuario():
    @classmethod
    def login(self,db,usuario):
        try:
            cursor=db.connection.cursor()
            sql="""SELECT id, usuario, password FROM usuario WHERE usuario= '{0}'""".format(usuario.usuario)
            cursor.execute(sql)
            data=cursor.fetchone()
            if data != None:

                coincide=Usuario.verificar_password(data[2],usuario.password)
                if coincide:
                    usuario_logeado=Usuario(data[0],data[1],None, None)
                    return usuario_logeado
                else:
                    return None
            else:
                    return None
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def obtener_por_id(self,db,id):
        try:
            cursor=db.connection.cursor()
            sql="""SELECT usuario.id, usuario.usuario, tipousuario.id, tipousuario.nombre FROM usuario  JOIN tipousuario ON usuario.tipousuario_id = tipousuario.id WHERE usuario.id = {0}""".format(id)
            cursor.execute(sql)
            data=cursor.fetchone()
            tipousuario=TipoUsuario(data[2],data[3])
            usuario_logeado=Usuario(data[0],data[1],None,tipousuario)
            return usuario_logeado
        except Exception as ex:
            raise Exception(ex)