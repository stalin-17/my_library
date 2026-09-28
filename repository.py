from sqlalchemy.ext.asyncio import AsyncSession

from models.books import Book
from schemas.books import SBookAdd
class BookRepository:
    @classmethod
    async def add_book(cls, data: SBookAdd, session: AsyncSession) -> Book:
        book_dict = data.model_dump()
        book = Book(**book_dict)
        session.add(book)
        await session.commit()
        await session.refresh(book)
        return book

