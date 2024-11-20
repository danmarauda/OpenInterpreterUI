import streamlit as st
import interpreter
from typing import Optional

def initialize_interpreter() -> None:
    """Initialize interpreter with default settings if not already in session state"""
    if 'interpreter' not in st.session_state:
        st.session_state['interpreter'] = interpreter
        # Set default configuration
        interpreter.auto_run = True
        interpreter.debug_mode = False
        
def setup_interpreter():
    """Configure interpreter with current session settings"""
    try:
        initialize_interpreter()
        st.session_state['interpreter'].reset()
    except Exception as e:
        st.error(f"Error resetting interpreter: {str(e)}")
        pass
    
    # Basic configuration
    interpreter = st.session_state['interpreter']
    interpreter.conversation_id = st.session_state['current_conversation']["id"]
    interpreter.conversation_history = True
    interpreter.messages = st.session_state.get('messages', st.session_state.get('mensajes',[]))
    
    # Model configuration
    interpreter.model = st.session_state['model']
    interpreter.temperature = st.session_state['temperature']
    interpreter.max_tokens = st.session_state['max_tokens']
    interpreter.system_message = st.session_state['system_message']
    interpreter.auto_run = True

    # Enable image support
    interpreter.computer.emit_images = True
    
    # Enable vision capabilities if available
    if hasattr(interpreter, 'vision'):
        interpreter.vision = True

    # API Configuration
    api_choice = st.session_state['api_choice']
    
    if api_choice == 'openrouter':
        interpreter.api_key = st.session_state['openrouter_key']
        interpreter.context_window = st.session_state['context_window']
        interpreter.api_base = "https://openrouter.ai/api/v1"
        
    elif api_choice == 'openai':
        interpreter.api_key = st.session_state['openai_key']
        interpreter.context_window = st.session_state['context_window']
        
    elif api_choice == 'azure_openai':
        interpreter.api_key = st.session_state['openai_key']
        interpreter.api_base = st.session_state['azure_endpoint']
        interpreter.api_version = st.session_state['api_version']
        
    elif api_choice == 'vertexai':
        interpreter.context_window = st.session_state['context_window']
        # Additional VertexAI specific settings can be added here
        
    elif api_choice == 'local':
        interpreter.context_window = st.session_state['context_window']
        interpreter.offline = True
        
        if st.session_state['provider'] == 'Lmstudio':
            interpreter.model = "openai/x"  # OpenAI format compatibility
            interpreter.api_key = "fake_key"  # Required for LiteLLM
            interpreter.api_base = st.session_state.get('api_base')
        else:
            interpreter.model = f"ollama/{st.session_state.get('model')}"
            interpreter.api_base = st.session_state.get('api_base')

    # Debug
    # st.write(interpreter.__dict__)
    # st.write(f'{interpreter.conversation_history_path=}')
    # st.write(f'{interpreter.conversation_filename =}')