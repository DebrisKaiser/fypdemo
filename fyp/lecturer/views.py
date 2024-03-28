from django.shortcuts import render
from gensim.summarization import summarize

def table_view(request):
    return render(request, 'table.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def test_view(request):
    processed_text = ''
    if request.method == 'POST':
        input_text = request.POST.get('inputText', '')
        processed_text = process_text(input_text)
    return render(request, 'test.html', {'processed_text': processed_text})

def process_text(text):
    # 使用 gensim 的 summarize 函数来生成文本的摘要
    return summarize(text)

