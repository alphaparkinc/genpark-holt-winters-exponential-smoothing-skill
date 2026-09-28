import sys
import json
from client import HoltWintersSmoother

def handle_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-holt-winters-exponential-smoothing-skill", "version": "1.0.0"}
            }
        }
    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "forecast_holt_winters",
                        "description": "Fit Holt-Winters triple exponential smoothing model and forecast future points",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "series": {"type": "array", "items": {"type": "number"}},
                                "season_length": {"type": "integer", "default": 4},
                                "horizon": {"type": "integer", "default": 2}
                            },
                            "required": ["series"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        
        if tool_name == "forecast_holt_winters":
            s = args.get("series", [])
            m = args.get("season_length", 4)
            h = args.get("horizon", 2)
            hw = HoltWintersSmoother(season_length=m)
            res = hw.fit_forecast(s, horizon=h)
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [{"type": "text", "text": json.dumps(res)}]
                }
            }
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}}
            sys.stdout.write(json.dumps(err) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
