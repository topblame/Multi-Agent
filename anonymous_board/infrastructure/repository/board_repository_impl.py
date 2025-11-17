from typing import Optional, List

from requests import Session

from anonymous_board.application.port.board_repository_port import BoardRepositoryPort
from anonymous_board.domain.board import Board
from anonymous_board.infrastructure.orm.board_orm import BoardORM
from config.database.session import get_db_session


class BoardRepositoryImpl(BoardRepositoryPort):
    def __init__(self):
        self.db: Session = get_db_session()

    def save(self, board: Board) -> Board:
        orm_board = BoardORM(
            userid= board.userid,
            title=board.title,
            content=board.content,
        )
        board.id = orm_board.id
        board.created_at = orm_board.created_at
        board.updated_at = orm_board.updated_at
        return board

    def get_by_id(self, board_id: int) -> Optional[Board]:
        orm_board = self.db.query(BoardORM).filter(BoardORM.id == board_id).first()
        if orm_board:
            board = Board(
                title=orm_board.title,
                content=orm_board.content,
            )
            board.id = orm_board.id
            board.userid = orm_board.userid
            board.created_at = orm_board.created_at
            board.updated_at = orm_board.updated_at
            return board
        return None

    def list_all(self) -> List[Board]:
        orm_boards = self.db.query(BoardORM).all()
        boards = []
        for orm_board in orm_boards:
            board = Board(
                title=orm_board.title,
                content=orm_board.content,
            )
            board.id = orm_board.id
            board.userid = orm_board.userid
            board.created_at = orm_board.created_at
            board.updated_at = orm_board.updated_at
            boards.append(board)
        return boards

    def delete(self, board_id: int, userid: str) -> None:
        self.db.query(BoardORM).filter(BoardORM.id == board_id and BoardORM.userid == userid).delete()
        self.db.commit()