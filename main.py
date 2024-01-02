import flet as ft
from random import randint

def main(page: ft.Page):
    page.window_width = 800
    page.window_height = 800
    page.bgcolor = "#27374D"
    page.title = "Flashademics"
    page.padding = 20
    page.scroll = "always"
    page.horizontal_alignment = "center"

    questions = [
    ("What is the supreme law of the land in the United States?", "The Constitution"),
    ("How many branches of government are there in the United States?", "Three (Executive, Legislative, Judicial)"),
    ("Who is known as the 'Father of the Constitution'?", "James Madison"),
    ("What is the minimum voting age in the United States?", "18 years old"),
    ("How many amendments are there in the United States Constitution?", "27 amendments"),
    ("What document declared the American colonies independent from Great Britain?", "The Declaration of Independence"),
    ("Who is the current Chief Justice of the United States Supreme Court?", "John G. Roberts Jr."),
    ("What is the purpose of the Bill of Rights?", "To protect individual rights and freedoms"),
    ("How many senators are there in the U.S. Senate?", "100 senators"),
    ("In what year did the United States declare its independence?", "1776"),
    ("What is the capital of the United States?", "Washington, D.C."),
    ("Who was the first President of the United States?", "George Washington"),
    ("What is the official language of the United States?", "There is no official language at the federal level."),
    ("How many members are there in the U.S. House of Representatives?", "435 members"),
    ("Who is the current Vice President of the United States?", "Kamala Harris"),
    ("What is the term length for a U.S. Senator?", "6 years"),
    ("Which amendment gave women the right to vote?", "19th Amendment"),
    ("What is the economic system of the United States?", "Mixed economy"),
    ("Who wrote the Gettysburg Address?", "Abraham Lincoln"),
    ("What is the nickname of the U.S. flag?", "The Stars and Stripes"),
    ("Who has the power to declare war in the United States?", "Congress"),
    ("What is the highest court in the United States?", "The Supreme Court"),
    ("Which ocean is on the east coast of the United States?", "Atlantic Ocean"),
    ("What is the nickname of the U.S. national anthem?", "The Star-Spangled Banner"),
    ("What are the first ten amendments to the Constitution called?", "The Bill of Rights"),
    ("Who was the main author of the Declaration of Independence?", "Thomas Jefferson"),
    ("Which President is associated with the Emancipation Proclamation?", "Abraham Lincoln"),
    ("What is the electoral college?", "A group of electors chosen to elect the President and Vice President"),
    ("What is the primary responsibility of the Executive Branch?", "To enforce and carry out laws"),
    ("What is the purpose of the Preamble to the U.S. Constitution?", "To introduce and explain the purpose of the Constitution")
]
    
    question_count = len(questions)

    def display_question(e):
        answer_text.value = ""
        global random_question
        random_question = randint(0, question_count-1)
        question_text.value = questions[random_question][0]
        page.update()

    def display_answer(e):
        answer_text.value = questions[random_question][1]
        page.update()

    title_label = ft.Container(
        content=ft.Text(value="American Civics", size=25, color="white"),
        padding=30
    )
    button_row = ft.Row(
        alignment="center",
        #height=250,
        controls=[
            ft.ElevatedButton(bgcolor="#00818A", color="white", text="Next Question", width=160, on_click=display_question),
            ft.ElevatedButton(bgcolor="#00818A", color="white", text="Answer", width=160, on_click=display_answer), 
        ]
    )

    question_container_header = ft.Text(value="Question:", size=20, color="white", text_align="center")

    answer_container_header = ft.Text(value="Question:", size=20, color="white", text_align="center")

    question_text = ft.Text(value="", size=20, color="white", text_align="center")

    answer_text = ft.Text(value="", size=20, color="white", text_align="center")

    content_layout = ft.Column(
        width=600,
        horizontal_alignment="center",
        controls=[
            ft.Container(
                content=(question_text),
                bgcolor="#526D82",
                width=600,
                height=250,
                border_radius=6,
                padding=ft.padding.symmetric(85)
                    
            ),
            ft.Container(
                content=button_row, padding=20,
            ),
            ft.Container(
                content=answer_text,
                bgcolor="#526D82",
                width=600,
                height=250,
                border_radius=6,
                padding=ft.padding.symmetric(90),
            ),
        ]
    )


    page.add(
        title_label,
        content_layout,

    )


    page.update()

    
ft.app(target=main)