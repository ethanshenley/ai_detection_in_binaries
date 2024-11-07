# AI Binary Detector Demo

This repository demonstrates the detection and analysis of AI models embedded within binary executables. It's a proof-of-concept implementation showing the first stages of a comprehensive binary analysis system.

## Features

- Binary executable loading and validation
- Basic block identification and analysis
- Control Flow Graph (CFG) construction
- Machine Learning framework detection
- Tensor operation pattern recognition
- Interactive visualization of analysis results

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/ethanshenley/ai_detection_in_binaries.git
cd ai_binary_detector
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -e .
```

4. Run the demo:
```bash
python -m ai_binary_detector.web.app
```

## Project Structure

- `src/ai_binary_detector/`: Core implementation
- `tests/`: Unit tests
- `demo/`: Sample binaries and demonstration notebooks
- `docs/`: Documentation and guides

## Development

```bash
# Run tests
pytest

# Run demo with hot reloading
uvicorn ai_binary_detector.web.app:app --reload
```

## License

[Your chosen license]