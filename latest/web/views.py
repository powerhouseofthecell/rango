from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def posts(request):
    context = dict()
    context['post_content'] = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Et tamen tantis vectigalibus ad liberalitatem utens etiam sine hac Pyladea amicitia multorum te benivolentia praeclare tuebere et munies. Ita redarguitur ipse a sese, convincunturque scripta eius probitate ipsius ac moribus. Ratio ista, quam defendis, praecepta, quae didicisti, quae probas, funditus evertunt amicitiam, quamvis eam Epicurus, ut facit, in caelum efferat laudibus. Ut ad minora veniam, mathematici, poëtae, musici, medici denique ex hac tamquam omnium artificum officina profecti sunt. Scientiam pollicentur, quam non erat mirum sapientiae cupido patria esse cariorem.'
    return render(request, 'posts.html', context=context)