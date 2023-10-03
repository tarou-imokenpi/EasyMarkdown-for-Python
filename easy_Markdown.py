from typing import Literal
from MD_codeblock_list import codeBlock_list

header_text = []
result_text = "実行結果"


class EasyMarkdown:
    def __init__(self) -> None:
        self.MD_text = ""

    def get_MD_text(self):
        return self.MD_text

    def output_MD(self, fileName: str = "output_MD", root: str = "./"):
        with open(root + fileName + ".md", mode="w", encoding="UTF-8") as f:
            f.write(self.MD_text)

    def add_Header(
        self,
        level: Literal["1", "2", "3", "4", "5", "6"] | int = "1",
        text: str = "HeaderText",
    ):
        level = int(level)
        if level == 1:
            self.MD_text += "# "
        elif level == 2:
            self.MD_text += "## "
        elif level == 3:
            self.MD_text += "### "
        elif level == 4:
            self.MD_text += "#### "
        elif level == 5:
            self.MD_text += "##### "
        elif level == 6:
            self.MD_text += "###### "

        self.MD_text += text + "\n\n"

    def add_InlineCode(text: str):
        pass

    def add_CodeBlock(self, code_type: codeBlock_list = "", text=""):
        self.MD_text += "```"
        self.MD_text += code_type + "\n"
        self.MD_text += text + "\n"
        self.MD_text += "```" + "\n"

    def add_Link(URL: str, title: str):
        pass

    def add_RawMarkdown(text: str):
        pass

    def add_Table():
        pass

    def add_Image(path: str):
        pass

    def add_Line() -> None:
        pass

    def add_Comment(text: str):
        pass
