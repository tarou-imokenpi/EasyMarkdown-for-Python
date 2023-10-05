# EasyMarkdown

# Install
```
pip install EasyMarkdown
```

# Usage

```python
from EasyMarkdown import EasyMarkdown

markdown = EasyMarkdown()


markdown.add_Header(level=1, text="Hello")
markdown.add_Header(level=2, text="Hello")

markdown.add_CodeBlock(From="text", code_type="python", text='print("hello")')

markdown.save_file()

```
## output.md

# Hello

## Hello

### Hello

```python
print("hello")
```

# Exampl add_CodeBlock 

```python
from EasyMarkdown import EasyMarkdown

markdown = EasyMarkdown()

markdown.add_CodeBlock(From="file", code_type="python", file_path=file_path)
```
