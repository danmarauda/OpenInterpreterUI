# Development Setup

This project now uses the development branch of Open Interpreter to access the latest features and improvements.

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/YourUsername/OpenInterpreterUI.git
cd OpenInterpreterUI
```

2. Run the setup script:
```bash
chmod +x setup_dev.sh
./setup_dev.sh
```

## New Features from Development Branch

The development branch includes several new features and improvements:

1. Enhanced Vision Capabilities
   - Support for image analysis and generation
   - Improved visual context understanding

2. Improved Code Execution
   - Better sandboxing and security
   - Enhanced isolation of execution environments

3. Extended Model Support
   - Additional model providers
   - Better handling of different model capabilities

4. Configuration Improvements
   - More flexible API settings
   - Enhanced conversation management

## Testing

You can run the test script separately to verify the integration:
```bash
python test_interpreter.py
```

## Troubleshooting

If you encounter any issues:

1. Make sure you have the latest version of the development branch:
```bash
pip uninstall open-interpreter
pip install -r requirements.txt --no-cache-dir
```

2. Check the logs in your terminal for any error messages

3. Verify your API keys and settings are correctly configured

## Contributing

When contributing to this project, please ensure you test against the development branch of Open Interpreter to maintain compatibility.