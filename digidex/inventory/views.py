from django.shortcuts import render

from base.components import (
    Section,
    Heading,
    Paragraph
)


def index(request):
    content = Section(
        children=[
            Heading(
                text='Inventory',
                size=1,
                style='top'
            ),
            Paragraph(
                text='Welcome to the Inventory page!',
                style='top'
            ),
        ],
        style='top'
    )
    context = {'content': content}
    template = 'inventory/index.html'
    return render(
        request,
        template,
        context
    )
