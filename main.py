import asyncio
from typing import List, Dict



books: List[Dict] = [
    {"id": 1, "title": "Things Fall Apart", "available": True},
    {"id": 2, "title": "Half of a Yellow Sun", "available": True}
]

borrowed: List[Dict] = []



async def borrow_book(user_id: int, book_id: int) -> str:
    await asyncio.sleep(1)  # simulate delay (like real API)

    for book in books:
        if book["id"] == book_id:
            if book["available"]:
                book["available"] = False
                borrowed.append({"user_id": user_id, "book_id": book_id})
                return f"User {user_id} borrowed book {book_id}"
            else:
                return f"Book {book_id} is not available"

    return "Book not found"




async def return_book(user_id: int, book_id: int) -> str:
    await asyncio.sleep(1)  # simulate delay

    for record in borrowed:
        if record["user_id"] == user_id and record["book_id"] == book_id:
            borrowed.remove(record)

            for book in books:
                if book["id"] == book_id:
                    book["available"] = True

            return f"User {user_id} returned book {book_id}"

    return "Return failed: record not found"




async def main() -> None:
    print("Initial Books:", books)

    tasks = [
        borrow_book(1, 1),
        borrow_book(2, 1),  
        borrow_book(3, 2)
    ]

    results = await asyncio.gather(*tasks)
    print("\nBorrow Results:")
    for r in results:
        print(r)

    print("\nBooks After Borrowing:", books)

    
    tasks_return = [
        return_book(1, 1),
        return_book(3, 2)
    ]

    results_return = await asyncio.gather(*tasks_return)
    print("\nReturn Results:")
    for r in results_return:
        print(r)

    print("\nFinal Books:", books)



if __name__ == "__main__":
    asyncio.run(main())