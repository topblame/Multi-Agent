from typing import List, Optional

from anonymous_board.application.port.board_repository_port import BoardRepositoryPort
from anonymous_board.domain.board import Board


class BoardUseCase:
    def __init__(self, board_repo: BoardRepositoryPort):
        self.board_repo = board_repo

    def create_board(self,userid :str, title: str, content: str) -> Board:
        board = Board(userid= userid, title=title, content=content)
        return self.board_repo.save(board)

    def get_board(self, board_id: int) -> Optional[Board]:
        return self.board_repo.get_by_id(board_id)

    def list_boards(self) -> List[Board]:
        return self.board_repo.list_all()

    def delete_board(self, userid: str, board_id: int) -> None:
        self.board_repo.delete(userid, board_id)