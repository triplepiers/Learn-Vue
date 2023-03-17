from uuid import uuid4
import os

from flask import Blueprint, request, jsonify
from src.path import FILE_DIR

file = Blueprint('file', __name__)


# 上传文件
@file.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    suffix = os.path.splitext(file.filename)[-1] # 获取后缀
    print(suffix)
    return jsonify({
        "status": 500
    })