"""
CP1404 Practical
Code to use Languages Class
Estimated time: 30 minutes
Actual time:
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    languages = [python, ruby, visual_basic]
    print(f"The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic() is True:
            print(f"{language.name}")


main()
