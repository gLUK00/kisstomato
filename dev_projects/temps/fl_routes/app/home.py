from flask import render_template

from .. import routes

# retourne les informations de bases du programme
@routes.route('/home', methods=['GET', 'POST', 'HEAD'])
def app_index():

    return render_template('app/index.html')