from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import logging, sys

app = Flask(__name__)
api = Api(app)

TODOS = {
    'intervention_1': {'libelle': 'build an API', 'description': 'do the exercice', 'nom_intervenant': 'Adrian', 'lieu': 'bureau', 'date': '01-01-1970' },
    'intervention_2': {'libelle': 'acheter le pain', 'description': 'trouver un truc dans lequel mettre mon pat&eacute;', 'nom_intervenant': 'Sebastien', 'lieu': 'boulangerie', 'date': '02-03-2020' },
    'intervention_3': {'libelle': 'Trouver un emploi', 'description': '', 'nom_intervenant': 'Adrian', 'lieu': 'Nantes', 'date': '03-03-2020' },
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="L'intervention {} n'existe pas".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('libelle', 'description', 'nom_intervenant', 'lieu', 'date')


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'libelle': args['libelle'], 'description': args['description'], 'nom_intervenant': args['nom_intervenant'], 'lieu': args['lieu'], 'date': args['date']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        logging.debug(args)
        #todo_id = int(max(TODOS.keys()).lstrip('intervention_')) + 1
        #todo_id = 'intervention_%i' % todo_id
        TODOS[todo_id] = {'libelle': args['libelle'], 'description': args['description'], 'nom_intervenant': args['nom_intervenant'], 'lieu': args['lieu'], 'date': args['date']}
        return TODOS[todo_id], 201
        return TODOS['intervention_1'], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True)