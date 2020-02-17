from flask import Blueprint, request, make_response, jsonify, abort
from api.models import User, UserSchema
import json

# ルーティング設定
user_router = Blueprint('user_router', __name__)

@user_router.errorhandler(400)
@user_router.errorhandler(401)
@user_router.errorhandler(403)
def error_handler(err):
  res = jsonify({
    'error': {
      'message': err.description['message']
    },
    'code': err.code
  })
  return res, err.code

@user_router.route('/users',methods=['GET'])
def get_user_list():
  try:
    users = User.getUserList()
    user_schema = UserSchema(many=True)
  except ValueError:
    print('error')

  return make_response(jsonify({
    'code': 200,
    'users': user_schema.dump(users)
  }))

@user_router.route('/users', methods=['POST'])
def registUser():
  # jsonデータを取得する
  jsonData = json.dumps(request.json)
  userData = json.loads(jsonData)

  if not 'name' in userData:
    abort(400, {
      'message': 'Name is a required!!'
    })
  
  try:
    user = User.registUser(userData)
    user_schema = UserSchema(many=True)
  except ValueError:
    print('error')

  return make_response(jsonify({
    'code': 200,
    'user': user
  }))

