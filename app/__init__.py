from flask import Flask, render_template, request , url_for, redirect, flash
from flask_mysqldb import MySQL 
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user


from .models.ModeloMaquillaje import ModeloMaquillaje
from .models.ModeloUsuario import ModeloUsuario
from .models.entities.Usuario import Usuario

from .consts import *

app = Flask(__name__)

csrf= CSRFProtect()
db=MySQL(app)
login_manager_app=LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModeloUsuario.obtener_por_id(db,id)






@app.route('/login', methods=['GET','POST'])
def login():
   
    if request.method=='POST':
        usuario=Usuario(None,request.form['usuario'],request.form['password'],None)
        usuario_logeado=ModeloUsuario.login(db,usuario)
        if usuario_logeado != None:
            login_user(usuario_logeado)
            flash(MENSAJE_BIENVENIDA,'success')
            return redirect(url_for('index'))
        else:
            flash(LOGIN_CREDENCIALESINVALIDAS,'warning')
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/logout')
def logout():
    logout_user()
    flash(LOGOUT, 'success')
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    if current_user.is_authenticated:
         if current_user.tipousuario.id == 1:
             maquillaje_vendido=[]
             data={
                 'titulo':'Productos Vendidos',
                 'maquillaje_vendido':maquillaje_vendido
             }
         else:
            compras=[]
            data={
                 'titulo':'Mis Compras',
                 'compras':compras
            }
         return render_template('index.html',data=data)
    else:
        return redirect(url_for('login'))

@app.route('/maquillaje')
@login_required
def listar_maquillaje():
    try:
        maquillaje=ModeloMaquillaje.listar_maquillaje(db)
        data={
            'titulo':'Listado de Productos',
            'maquillaje':maquillaje
        }
        return render_template('listado_maquillaje.html',data=data)
    except Exception as ex:
       return render_template('errores/error.html',mensaje=format(ex))
    

def pagina_no_encontrada(error):
    return render_template('errores/404.html'),404

def pagina_no_autorizada(error):
    return redirect(url_for('login'))

def inicializar_app(config):
    app.config.from_object(config)
    csrf.init_app(app)
    app.register_error_handler(401,pagina_no_autorizada)
    app.register_error_handler(404,pagina_no_encontrada)
    return app
