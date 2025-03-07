from sqlalchemy import Table, Column, Integer, ForeignKey, PrimaryKeyConstraint
from models.base import Base

task_tag_table = Table(
    "task_tag",
    Base.metadata,
    Column(
        "task_id", Integer, ForeignKey("tasks.id", ondelete="CASCADE"), nullable=False
    ),
    Column(
        "tag_id", Integer, ForeignKey("tags.id", ondelete="CASCADE"), nullable=False
    ),
    PrimaryKeyConstraint("task_id", "tag_id"),
)
