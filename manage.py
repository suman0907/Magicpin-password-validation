from app.password_authentication.views import *
from app import create_app


app = create_app()

if  __name__ =='__main__':
    app.run(debug=True,use_reloader=True)