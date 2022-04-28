from fastapi import FastAPI
from lib import get_balance, get_interest 


app = FastAPI(debug=False)

@app.get("/api/v1/anchor/balance/{address}")
async def get_address(address: str) -> dict:
    """Return balance"""
    return { "ok": True, "balance": get_balance(address), "unit": "UST"}
    
@app.get("/api/v1/anchor/interest/latest")
async def get_latest_interest():
    """Return lastest interest in APY"""
    return { "ok": True, "interest": get_interest(), "unit": "APY"}