import os


PATH_TO_TOC = './Билеты'

toc: str = ''


def wrap_theme(header: str):
    return header + ':\n'

def wrap_content(content: str):
    return f'- {content}\n'

tickets : dict
themes: list = []

for _, dirs, _ in os.walk(PATH_TO_TOC):
    themes = dirs
    break

for theme in themes:
    toc += wrap_theme(theme)
    for root, dirs, files in os.walk(PATH_TO_TOC + '/' + theme):
        #print(root, dirs, files)
        for file in files:
            toc += wrap_content(file)

print(toc)
