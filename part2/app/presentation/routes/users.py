from flask_restx import Namespace, Resource

api = Namespace('users', description='User operations')

@api.route('/health')
class HealthCheck(Resource):
    def get(self):
        return {'message': 'API is running'}, 200

