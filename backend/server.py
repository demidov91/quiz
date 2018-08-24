import asyncio

import aioredis
from aiohttp import web


PREFIX = 'some_prefix'

async def hello(request):
    count = await request.app['redis'].incr(f'{PREFIX}-counter')
    return web.Response(text=f"Hello, {count} world!")


async def create_redis_pool(app):
    app['redis'] = await aioredis.create_redis_pool(
        'redis://redis:6379',
        minsize=5, maxsize=10,
        loop=app.loop)


async def close_redis_pool(app):
    await app['redis'].wait_closed()


if __name__ == '__main__':
    app = web.Application()
    app.add_routes([web.get('/', hello)])
    app.on_startup.append(create_redis_pool)
    app.on_shutdown.append(close_redis_pool)

    web.run_app(app)
