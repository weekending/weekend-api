from datetime import timezone

from sqlalchemy import text

from app.adapter.outbound.persistence.reporitory.base import BaseRepository
from app.application.port.output import PostCommentRepositoryPort
from app.domain import PostComment, User


class PostCommentPersistenceAdapter(BaseRepository, PostCommentRepositoryPort):
    async def find_by_post(self, post_id: int) -> list[PostComment]:
        query = """
        WITH RECURSIVE comment_tree AS (
            SELECT pc.id
                 , pc.user_id
                 , pc.post_id
                 , pc.parent_id
                 , pc.level 
                 , pc.content
                 , pc.is_active
                 , pc.created_dtm
                 , LPAD(pc.id::text, :lpad_length, '0') AS sort_path
            FROM t_post_comment AS pc
            WHERE pc.post_id = :post_id
              AND pc.parent_id IS NULL
            UNION ALL
            SELECT pc.id
                 , pc.user_id
                 , pc.post_id
                 , pc.parent_id
                 , pc.level
                 , pc.content
                 , pc.is_active
                 , pc.created_dtm
                 , ct.sort_path || '-' || LPAD(pc.id::text, :lpad_length, '0') AS sort_path
            FROM t_post_comment AS pc
                     INNER JOIN comment_tree AS ct ON pc.parent_id = ct.id
            WHERE pc.post_id = :post_id
        )
        SELECT ct.id
             , ct.user_id
             , ct.post_id
             , ct.parent_id
             , ct.level
             , ct.content
             , ct.is_active
             , ct.created_dtm
             , u.name AS user_name
             , u.email AS user_email
             , u.is_active AS user_is_active
             , u.is_admin AS user_is_admin
        FROM comment_tree AS ct
                 LEFT JOIN t_user AS u ON ct.user_id = u.id
        ORDER BY ct.sort_path
        """
        result = await self._session.execute(
            text(query), {"post_id": post_id, "lpad_length": 5}
        )
        return [
            PostComment(
                id=row.id,
                user_id=row.user_id,
                post_id=row.post_id,
                parent_id=row.parent_id,
                level=row.level,
                content=row.content if row.is_active else "[삭제된 댓글]",
                is_active=row.is_active,
                created_dtm=row.created_dtm.replace(tzinfo=timezone.utc),
                user=User(
                    id=row.user_id,
                    name=row.user_name,
                    email=row.user_email,
                    password="",
                    is_active=row.user_is_active,
                    is_admin=row.user_is_admin,

                ) if row.user_id is not None else None,
            )
            for row in result.fetchall()
        ]
