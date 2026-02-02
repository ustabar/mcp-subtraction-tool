# MCP Subtraction Tool

A Model Context Protocol (MCP) server that provides a subtraction tool for mathematical operations.

## Overview

This project implements a simple yet functional MCP server with a subtraction tool that can perform arithmetic subtraction operations (a - b). It demonstrates how to create an MCP-compliant tool server in Python.

## Features

- **Subtraction Tool**: Performs subtraction operations on two numbers
- **MCP Compliance**: Follows the Model Context Protocol specification
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

### As a Python Module

```python
from subtraction_tool import MCPSubtractionServer

server = MCPSubtractionServer()
result = server.call_tool("subtract", {"minuend": 10, "subtrahend": 3})
print(result)
# Output: {"success": true, "operation": "10 - 3", "result": 7, ...}
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
