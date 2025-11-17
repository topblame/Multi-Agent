from typing import List

from fastapi import APIRouter, HTTPException

from anonymous_board.adapter.input.web.request.create_board_request import CreateBoardRequest
from anonymous_board.adapter.input.web.response.board_response import BoardResponse
from anonymous_board.application.usecase.board_usecase import BoardUseCase
from anonymous_board.infrastructure.repository.board_repository_impl import BoardRepositoryImpl

board_router = APIRouter

usecase = BoardUseCase(BoardRepositoryImpl)

@board_router.post("/create", response_model=BoardResponse)
def create_board(request: CreateBoardRequest):
    board = usecase.create_board(request.title, request.content)
    return BoardResponse(
        id=board.id,
        userid=board.userid,
        title=board.title,
        content=board.content,
        created_at=board.created_at,
        updated_at=board.updated_at,
    )

@board_router.get("/list", response_model=List[BoardResponse])
def list_boards():
    boards = usecase.list_boards()
    return [
        BoardResponse(
            id=b.id,
            userid=b.userid,
            title=b.title,
            content=b.content,
            created_at=b.created_at,
            updated_at=b.updated_at,
        ) for b in boards
    ]

@board_router.get("/read/{board_id}", response_model=BoardResponse)
def get_board(board_id: int):
    board = usecase.get_board(board_id)
    if not board:
        raise HTTPException(status_code=404, detail="Board not found")
    return BoardResponse(
        id=board.id,
        userid= board.userid,
        title=board.title,
        content=board.content,
        created_at=board.created_at,
        updated_at=board.updated_at,
    )

@board_router.delete("/delete/{board_id}")
def delete_board(board_id: int):
    success = usecase.delete_board(board_id)
    if not success:
        raise HTTPException(status_code=404, detail="Board not found")
    return {"message": "Deleted successfully"}