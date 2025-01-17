from django import template

register = template.Library()

@register.filter(name='chunks')
def chunks(list,chunk_size):
    chunk=[]
    i=0
    for product in list:
        chunk.append(product)
        i+=1
        if i==chunk_size:
            yield chunk
            i=0
            chunk=[]
    yield chunk
