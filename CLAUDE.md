# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an educational repository focused on software engineering concepts, containing algorithm implementations, design patterns, and programming examples in multiple languages (primarily Java and Python).

## Common Development Commands

### Python Development

```bash
# Run algorithm implementations
python algorithms/binary-search.py
python algorithms/dijkstras_algorithm.py
python algorithms/breath-first-search.py

# Run Python examples from chapters
python python-src/chap2/name.py
python python-src/chap9/car.py

# Run unit tests
python -m unittest python-src/chap11/test_name_function.py
python python-src/chap11/test_survey.py
```

### Java Development

Since there's no build system (Maven/Gradle), compile and run Java files directly:

```bash
# For simple Java programs
javac java-src/Addition.java
java -cp java-src Addition

# For package-based programs (design patterns)
javac -d . designpatterns-src/headfirst/designpatterns/strategy/*.java
java headfirst.designpatterns.strategy.MiniDuckSimulator

# For GRASP patterns
javac -d . designpatterns-src/patterns/grasp/controller/*.java
java patterns.grasp.controller.Main
```

### C Development

```bash
# Compile and run C programs
gcc c-src/point.c -o c-src/point
./c-src/point
```

## Project Architecture

### Directory Structure

- **algorithms/**: Python implementations of classic algorithms (search, sort, graph algorithms)
  - Each algorithm is a standalone Python file
  - Some use the `big_o` library for complexity analysis
  - Includes visualization outputs as PNG files

- **designpatterns-src/**: Comprehensive Java design pattern implementations
  - **headfirst/designpatterns/**: Examples from "Head First Design Patterns" book
  - **patterns/**: Additional pattern implementations including GRASP patterns
  - Each pattern has its own package with example implementations

- **java-src/**: Basic Java programming examples (arrays, classes, control structures)
- **oo-src/**: Object-oriented programming examples in Java
- **python-src/**: Python Crash Course book examples organized by chapters
- **c-src/**: Simple C programming examples

### Key Design Pattern Packages

The repository includes implementations of:
- Behavioral: Strategy, Observer, Command, Iterator, Template Method, State, Visitor
- Creational: Factory, Abstract Factory, Singleton, Builder, Prototype
- Structural: Decorator, Adapter, Facade, Proxy, Composite, Flyweight, Bridge
- GRASP: Controller, Creator, High Cohesion, Low Coupling, Polymorphism, Pure Fabrication

### Testing Approach

- Python: Uses `unittest` framework for test files
- Java: Main method test drives (e.g., `*TestDrive.java` classes)
- No automated test runners or CI/CD configuration

### Virtual Environment

A Python virtual environment `software-engineering-venv` is gitignored but can be created for Python dependencies.

## Important Notes

- This is an educational repository without formal build systems
- Code is meant to be run directly for learning purposes
- Each subdirectory is relatively independent
- Focus on algorithm understanding and design pattern implementation rather than production deployment