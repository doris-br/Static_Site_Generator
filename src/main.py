from textnode import TextNode
from textnode import TextType

def main():
    new_textnode = TextNode("hi there", TextType.LINK, "https://www.notsureyet.de")
    print(new_textnode)
main()