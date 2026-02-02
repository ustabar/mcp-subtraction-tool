# MCP Subtraction Tool

A Model Context Protocol (MCP) server that provides a subtraction tool for mathematical operations.

## Overview

This project implements a simple yet functional MCP server with a subtraction tool that can perform arithmetic subtraction operations (a - b). It demonstrates how to create an MCP-compliant tool server in Python.

The project includes:
- **Server** (`subtraction_tool.py`): MCP server implementation with the subtraction tool
- **Client** (`client.py`): Interactive client application to communicate with the server

## Features

- **Subtraction Tool**: Performs subtraction operations on two numbers
- **MCP Compliance**: Follows the Model Context Protocol specification
- **Client Application**: Easy-to-use client for interacting with the server
- **Multiple Modes**: Interactive, demo, and command-line modes
- **Type Safe**: Input validation and error handling
- **Support for Multiple Number Types**: Works with integers and floating-point numbers

## Getting Started

### Prerequisites
- Python 3.7+

### Installation

```bash
git clone https://github.com/ustabar/mcp-subtraction-tool.git
cd mcp-subtraction-tool
```

### Running the Tool

```bash
python subtraction_tool.py
```

This will display available tools and run test cases.

## Usage

### Using the Client Application

The client application provides an easy way to interact with the MCP Subtraction Server.

#### Interactive Mode

Run the client in interactive mode to enter commands manually:

```bash
python client.py
```

This will start an interactive session where you can:
- Type `list` to see available tools
- Type `subtract` to perform subtraction operations
- Type `quit` or `exit` to exit

#### Demo Mode

Run the client in demo mode to see predefined examples:

```bash
python client.py --demo
```

This will demonstrate various subtraction operations.

#### Command Line Mode

Perform a single subtraction operation directly:

```bash
python client.py --subtract 10 3
# Output: Result: 7.0
```

#### Help

Display usage information:

```bash
python client.py --help
```

### As a Python Module

```python
from subtraction_tool import MCPSubtractionServer

server = MCPSubtractionServer()
result = server.call_tool("subtract", {"minuend": 10, "subtrahend": 3})
print(result)
# Output: {"success": true, "operation": "10 - 3", "result": 7, ...}
```

### Using the Client Programmatically

```python
from client import MCPClient

client = MCPClient()
client.list_available_tools()
result = client.call_subtract_tool(10, 3)
```

### Tool Schema

**Tool Name**: `subtract`

**Description**: Subtracts one number from another (a - b)

**Input Parameters**:
- `minuend` (number, required): The number to subtract from
- `subtrahend` (number, required): The number to subtract

**Output**:
```json
{
  "success": true,
  "operation": "10 - 3",
  "result": 7,
  "minuend": 10,
  "subtrahend": 3
}
```

## Test Cases

The tool has been tested with:
- Positive integers: 10 - 3 = 7
- Floating-point numbers: 5.5 - 2.3 = 3.2
- Negative numbers: -10 - 5 = -15
- Zero values: 0 - 0 = 0

## Project Details

- **Created By**: Baris Usta
- **Creation Date**: February 2, 2026
- **Repository**: https://github.com/ustabar/mcp-subtraction-tool

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
