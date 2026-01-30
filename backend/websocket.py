"""WebSocket endpoint va event dispatch."""
from fastapi import WebSocket, WebSocketDisconnect
from utils.websocket_manager import manager


async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint."""
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast({"message": data})
    except WebSocketDisconnect:
        manager.disconnect(websocket)
