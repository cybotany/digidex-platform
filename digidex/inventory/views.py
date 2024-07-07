from django.shortcuts import render

from base.components import (
    Section,
    Block,
    Heading,
    Paragraph
)


def index(request):
    block = Block(
        children=[
            Heading(text='Block Heading', size=1, style='top'),
            Paragraph(text='This is a paragraph in a block.', style='top')
        ],
        style='top'
    )
    content = Section(
        children=[
            block,
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
