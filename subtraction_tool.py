#!/usr/bin/env python3
"""
MCP Subtraction Tool
A simple Model Context Protocol server that provides a subtraction tool.
"""

import json
from typing import Any, Dict

class SubtractionTool:
    """A tool that performs subtraction operations."""
    
    def __init__(self):
        self.name = "subtract"
        self.description = "Subtracts one number from another (a - b)"
        self.input_schema = {
            "type": "object",
            "properties": {
                "minuend": {
                    "type": "number",
                    "description": "The number to subtract from"
                },
                "subtrahend": {
                    "type": "number",
                    "description": "The number to subtract"
                }
            },
            "required": ["minuend", "subtrahend"]
        }
    
    def execute(self, minuend: float, subtrahend: float) -> Dict[str, Any]:
        """
        Execute subtraction operation.
        
        Args:
            minuend: The number to subtract from
            subtrahend: The number to subtract
            
        Returns:
            Dictionary with result and details
        """
        result = minuend - subtrahend
        return {
            "success": True,
            "operation": f"{minuend} - {subtrahend}",
            "result": result,
            "minuend": minuend,
            "subtrahend": subtrahend
        }
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert tool to dictionary format for MCP protocol."""
        return {
            "name": self.name,
            "description": self.description,
            "inputSchema": self.input_schema
        }


class MCPSubtractionServer:
    """Simple MCP Server implementation for subtraction tool."""
    
    def __init__(self):
        self.tool = SubtractionTool()
    
    def list_tools(self) -> Dict[str, Any]:
        """Return available tools."""
        return {
            "tools": [self.tool.to_dict()]
        }
    
    def call_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Call a tool with given arguments."""
        if name == "subtract":
            try:
                minuend = arguments.get("minuend")
                subtrahend = arguments.get("subtrahend")
                
                if minuend is None or subtrahend is None:
                    return {
                        "success": False,
                        "error": "Missing required arguments: minuend and subtrahend"
                    }
                
                return self.tool.execute(minuend, subtrahend)
            except TypeError as e:
                return {
                    "success": False,
                    "error": f"Invalid argument types: {str(e)}"
                }
        else:
            return {
                "success": False,
                "error": f"Unknown tool: {name}"
            }


def main():
    """Main function for testing the subtraction tool."""
    server = MCPSubtractionServer()
    
    # Show available tools
    print("Available Tools:")
    print(json.dumps(server.list_tools(), indent=2))
    
    # Test subtraction
    print("\n\nTest Cases:")
    test_cases = [
        {"minuend": 10, "subtrahend": 3},
        {"minuend": 5.5, "subtrahend": 2.3},
        {"minuend": -10, "subtrahend": 5},
        {"minuend": 0, "subtrahend": 0},
    ]
    
    for test in test_cases:
        result = server.call_tool("subtract", test)
        print(f"\nInput: {test}")
        print(f"Result: {json.dumps(result, indent=2)}")


if __name__ == "__main__":
    main()