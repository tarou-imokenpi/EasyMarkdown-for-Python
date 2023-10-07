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
# method
|Name|Argument|Description|
|----|--------|-----------|
|get_MD_text|self|Get the current markdown text|
|save_file|self, fileName: str, root: str|Save markdown text in markdown format|
|add_Header|self, level: Literal[1, 2, 3, 4, 5, 6], text: str|Add a header|
|add_InlineCode|self, text: str|Add an inline code|
|add_CodeBlock|self, From: Literal["text", "file"], code_type, text: str, file_path: str|Add a CodeBlock|
|add_Link|self, title: str, URL: str|add a Link|
|add_RawMarkdown|self, text: str|The text as is is reflected in the markdown|
|add_Table|self, row: int, coumum: int, title: list[str], data: list|under development|
|add_Image|self, path: str, alt: str|Add an image|
|add_Line|self|add a line|
|add_Comment|self, text: str|add a comment|
- - -

# Exampl add_CodeBlock 

```python
from EasyMarkdown import EasyMarkdown

markdown = EasyMarkdown()

markdown.add_CodeBlock(From="file", code_type="python", file_path=file_path)
```
