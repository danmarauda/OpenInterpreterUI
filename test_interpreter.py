import interpreter
import sys
import os

def test_interpreter_setup():
    """Test basic interpreter setup and functionality"""
    print("Testing Open Interpreter Development Branch Integration")
    print(f"Interpreter Version: {interpreter.__version__}")
    print(f"Python Version: {sys.version}")
    
    # Test basic interpreter initialization
    interpreter.auto_run = False
    interpreter.api_key = os.getenv('OPENAI_API_KEY', 'dummy_key')
    
    # Test basic settings
    print("\nTesting Configuration:")
    print(f"Model: {interpreter.model}")
    print(f"Context Window: {interpreter.context_window}")
    print(f"Auto Run: {interpreter.auto_run}")
    print(f"Max Tokens: {interpreter.max_tokens}")
    
    # Test vision capabilities
    print("\nTesting Vision Support:")
    print(f"Vision Support Available: {hasattr(interpreter, 'vision')}")
    
    # Test computer capabilities
    print("\nTesting Computer Capabilities:")
    print(f"Computer Object Available: {hasattr(interpreter, 'computer')}")
    if hasattr(interpreter, 'computer'):
        print(f"Emit Images: {interpreter.computer.emit_images}")
    
    return "Tests completed successfully!"

if __name__ == "__main__":
    test_interpreter_setup()