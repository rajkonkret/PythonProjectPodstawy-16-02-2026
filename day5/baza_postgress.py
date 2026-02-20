import asyncio
import asyncpg


async def main():
    pool = await asyncpg.create_pool(
        user="37970432_dane",
        password="",
        database="37970432_dane",
        host="serwer2348480.home.pl",
        min_size=1, max_size=5
    )

    async with pool.acquire() as conn:
        async with conn.transaction():
            await conn.execute(
                "CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name TEXT)"
            )

            row = await conn.fetchrow(
                "INSERT INTO users(name) VALUES($1) RETURNING id, name", "John"
            )
            print(f"Inserted: {dict(row)}")
    await pool.close()


if __name__ == '__main__':
    asyncio.run(main())
# Inserted: {'id': 24, 'name': 'John'}
