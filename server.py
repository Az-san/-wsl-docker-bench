# server.py — エコーサーバ (asyncio TCP)
import asyncio, struct

PORT = 50007

async def handle(reader, writer):
    try:
        while True:
            data = await reader.readexactly(8)
            writer.write(data)
            await writer.drain()
    except asyncio.IncompleteReadError:
        # クライアントが切断しただけなので終了
        pass
    finally:
        writer.close()
        await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle, host='0.0.0.0', port=PORT)
    addrs = ", ".join(str(sock.getsockname()) for sock in server.sockets)
    print(f"Listening on {addrs}")
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
