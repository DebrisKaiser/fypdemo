from django.shortcuts import render
from transformers import T5Tokenizer, T5ForConditionalGeneration
import os

print(os.getcwd())

def table_view(request):
    return render(request, 'table.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def test_view(request):
    if request.method == 'POST':
        # 从POST请求中获取用户输入的数据
        user_input = request.POST.get('user_input')

        # 使用T5模型处理用户输入的数据
        summary = process_text(user_input)

        # 将处理后的结果传递给模板
        return render(request, 'test.html', {'summary': summary})
    else:
        # 对于GET请求，你可以选择渲染一个空的表单或者其他内容
        return render(request, 'test.html')

def process_text(text):
    # 加载预训练模型和分词器
    model_name = 't5-base'
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)

    # 使用分词器处理文本
    encoded_input = tokenizer.encode("summarize: " + text, return_tensors='pt')

    # 进行模型推理，生成摘要
    output = model.generate(encoded_input, max_length=100, temperature=0.7)

    # 将生成的摘要解码回字符串
    generated_summary = tokenizer.decode(output[0])

    # 移除开头的 '<pad>' 和结尾的 '</s>'
    generated_summary = generated_summary.replace('<pad>', '').replace('</s>', '')

    return generated_summary