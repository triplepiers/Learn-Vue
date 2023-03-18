from flask import Blueprint, request, jsonify
from src.models import Txt
from src.database import db
from sqlalchemy.orm import sessionmaker

text = Blueprint('text', __name__)