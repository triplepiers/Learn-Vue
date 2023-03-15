from flask import Blueprint, request, jsonify
from src.models import User
from src.database import db
from sqlalchemy.orm import sessionmaker

user = Blueprint('user', __name__)


# 新建用户
@user.route('/add', methods=['POST'])
def add_user():
    data = request.get_json()
    k_set = data.keys()

    neo_usr = User()
    neo_usr.__setattr__('password', '123456')  # 因为表单里没有 pwd
    for key in User.keys():
        if key in k_set:  # 对提交数据中包含的属性进行赋值
            neo_usr.__setattr__(key, data[key])
            # print(getattr(neo_usr, key))

    session = sessionmaker(bind=db)()
    session.add(neo_usr)
    session.commit()
    session.close()

    return jsonify({
        "status": 500  # 正常插入
    })


# 根据 nick_name 查找用户
@user.route('/all', methods=['GET'])
def get_all():
    page = int(request.values.get("page")) - 1
    size = int(request.values.get("size"))
    search = request.values.get("search")

    session = sessionmaker(bind=db)()
    if len(search):
        res = session.query(User).filter(User.nick_name.like("%"+search+"%")).limit(size).offset(page*size).all()  # 手动分页查询
    else:
        res = session.query(User).limit(size).offset(page*size).all()
    session.close()

    tableData = []
    for item in res:
        tableData.append(item.to_json())

    return jsonify({
        "status": 500,
        "data": {
            "tableData": tableData
        }
    })