import os
import sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.config import settings
from app.db.session import Base

# This line is critical - imports all models so Base knows about them
from app.models.user import User
from app.models.course import Course
from app.models.enrollment import Enrollment