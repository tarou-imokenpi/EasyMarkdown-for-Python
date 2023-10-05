from typing import Literal, Union
from MD_codeblock_list import codeBlock_list


class EasyMarkdown:
    def __init__(self) -> None:
        self.MD_text = ""

    def get_MD_text(self) -> str:
        return self.MD_text

    def save_file(self, fileName: str = "output", root: str = "./") -> None:
        with open(root + fileName + ".md", mode="w", encoding="UTF-8") as f:
            f.write(self.MD_text)

    def add_Header(
        self,
        level: Literal[1, 2, 3, 4, 5, 6] = 1,
        text: str = "HeaderText",
    ) -> None:
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

    def add_InlineCode(text: str) -> None:
        pass

    def add_CodeBlock(
        self,
        From: Literal["text", "file"] = "text",
        code_type: codeBlock_list = "",
        text: str = "",
        file_path: str = "",
    ) -> None:
        self.MD_text += "```" + code_type + "\n"
        if From == "text":
            self.MD_text += text + "\n"
        elif From == "file":
            with open(file_path, mode="r", encoding="UTF-8") as f:
                self.MD_text += f.read() + "\n"
        else:
            raise ValueError("Invalid value.\n text or file only")

        self.MD_text += "```" + "\n"

    def add_Link(self, title: str, URL: str) -> None:
        pass

    def add_RawMarkdown(self, text: str) -> None:
        pass

    def add_Table(
        self, row: int, coumum: int, Table_list: list[list[Union[int, str]]]
    ) -> None:
        pass

    def add_Image(self, path: str) -> None:
        pass

    def add_Line(self) -> None:
        pass

    def add_Comment(self, text: str) -> None:
        pass
