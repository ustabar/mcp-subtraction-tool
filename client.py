#!/usr/bin/env python3
"""
MCP Subtraction Tool Client
A client application to interact with the MCP Subtraction Server.
"""

import json
import sys
from subtraction_tool import MCPSubtractionServer


class MCPClient:
    """Client for interacting with MCP Subtraction Server."""
    
    def __init__(self):
        self.server = MCPSubtractionServer()
    
    def list_available_tools(self):
        """List all available tools from the server."""
        tools_response = self.server.list_tools()
        print("\n" + "="*60)
        print("AVAILABLE TOOLS")
        print("="*60)
        
        for tool in tools_response.get("tools", []):
            print(f"\nTool Name: {tool['name']}")
            print(f"Description: {tool['description']}")
            print(f"\nInput Schema:")
            print(json.dumps(tool['inputSchema'], indent=2))
        print("="*60 + "\n")
    
    def call_subtract_tool(self, minuend, subtrahend):
        """
        Call the subtract tool with given parameters.
        
        Args:
            minuend: The number to subtract from
            subtrahend: The number to subtract
            
        Returns:
            Result dictionary from the tool
        """
        arguments = {
            "minuend": minuend,
            "subtrahend": subtrahend
        }
        
        print(f"\nCalling 'subtract' tool with:")
        print(f"  Minuend (a): {minuend}")
        print(f"  Subtrahend (b): {subtrahend}")
        
        result = self.server.call_tool("subtract", arguments)
        
        print("\n" + "-"*60)
        print("RESULT")
        print("-"*60)
        
        if result.get("success"):
            print(f"Operation: {result['operation']}")
            print(f"Result: {result['result']}")
            print(f"Success: {result['success']}")
        else:
            print(f"Error: {result.get('error', 'Unknown error')}")
            print(f"Success: {result['success']}")
        
        print("-"*60 + "\n")
        return result
    
    def run_interactive_mode(self):
        """Run the client in interactive mode."""
        print("\n" + "="*60)
        print("MCP SUBTRACTION TOOL - INTERACTIVE CLIENT")
        print("="*60)
        print("This client connects to the MCP Subtraction Server")
        print("Type 'list' to see available tools")
        print("Type 'subtract' to perform subtraction")
        print("Type 'quit' or 'exit' to quit")
        print("="*60 + "\n")
        
        while True:
            try:
                command = input("Enter command (list/subtract/quit): ").strip().lower()
                
                if command in ['quit', 'exit', 'q']:
                    print("\nExiting client. Goodbye!")
                    break
                
                elif command == 'list':
                    self.list_available_tools()
                
                elif command == 'subtract':
                    try:
                        minuend_str = input("Enter the minuend (number to subtract from): ")
                        subtrahend_str = input("Enter the subtrahend (number to subtract): ")
                        
                        minuend = float(minuend_str)
                        subtrahend = float(subtrahend_str)
                        
                        self.call_subtract_tool(minuend, subtrahend)
                    except ValueError:
                        print("\nError: Please enter valid numbers.\n")
                
                else:
                    print(f"\nUnknown command: '{command}'")
                    print("Available commands: list, subtract, quit\n")
            
            except KeyboardInterrupt:
                print("\n\nInterrupted. Exiting...")
                break
            except EOFError:
                print("\n\nEnd of input. Exiting...")
                break
    
    def run_demo_mode(self):
        """Run the client in demo mode with predefined examples."""
        print("\n" + "="*60)
        print("MCP SUBTRACTION TOOL - DEMO MODE")
        print("="*60)
        print("Demonstrating client-server interaction\n")
        
        # List available tools
        self.list_available_tools()
        
        # Run demo test cases
        print("Running demonstration subtraction operations...\n")
        
        demo_cases = [
            (10, 3, "Basic subtraction"),
            (5.5, 2.3, "Floating-point subtraction"),
            (-10, 5, "Negative minuend"),
            (100, 150, "Result is negative"),
            (0, 0, "Both zeros"),
        ]
        
        for minuend, subtrahend, description in demo_cases:
            print(f"\nDemo Case: {description}")
            self.call_subtract_tool(minuend, subtrahend)
            input("Press Enter to continue to next demo...")


def print_usage():
    """Print usage information."""
    print("\nUsage:")
    print("  python client.py                  # Run in interactive mode")
    print("  python client.py --demo           # Run demo mode with examples")
    print("  python client.py --subtract A B   # Subtract B from A")
    print("  python client.py --help           # Show this help message")
    print()


def main():
    """Main function for the client application."""
    client = MCPClient()
    
    # Parse command line arguments
    if len(sys.argv) == 1:
        # No arguments - run interactive mode
        client.run_interactive_mode()
    
    elif len(sys.argv) == 2:
        if sys.argv[1] in ['--help', '-h']:
            print_usage()
        elif sys.argv[1] == '--demo':
            client.run_demo_mode()
        else:
            print(f"Unknown option: {sys.argv[1]}")
            print_usage()
    
    elif len(sys.argv) == 4 and sys.argv[1] == '--subtract':
        try:
            minuend = float(sys.argv[2])
            subtrahend = float(sys.argv[3])
            client.list_available_tools()
            client.call_subtract_tool(minuend, subtrahend)
        except ValueError:
            print("\nError: Arguments must be numbers")
            print_usage()
            sys.exit(1)
    
    else:
        print("\nError: Invalid arguments")
        print_usage()
        sys.exit(1)


if __name__ == "__main__":
    main()
