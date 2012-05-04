""" Module containing views for the app.
"""
 
__author__ = 'Selwyn Jacob <selwynjacob90@gmail.com'

from markdown import markdown

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from app.models import Sequence
from app.logic.nussinov import buildSequence
from app.logic.bracket import bracketRep
from app.logic.graph import graphRep

class InputForm(ModelForm):
   class Meta:
      model = Sequence
      exclude = ['output_seq', 'bracketed_str', 'graph_svg', 'mat', 'length']

@csrf_exempt
def input_page(request):
  """This view generates the input form and creates the required representations
     with the help of logic module and save the sequence to the database.
  """

  if request.method == 'POST':
     form = InputForm(request.POST)
     if form.is_valid():
       new_seq = form.save(commit=False)
       input_seq = form.cleaned_data['raw_seq']
       
       # Build nussinov sequence 
       sequence, mat, length = buildSequence(input_seq.encode('ascii', 'ignore')) 
       new_seq.output_seq = sequence
       new_seq.mat = mat
       new_seq.length = length
       
       # Generating bracketed representation
       bracket_seq = bracketRep(sequence)
       bracketed_str = ''.join(i for i in bracket_seq)
       new_seq.bracketed_str = bracketed_str
       
       #Generate planar graph
       graph_svg = graphRep(input_seq, bracketed_str)
       new_seq.graph_svg = graph_svg

       new_seq.save()  
       return HttpResponseRedirect(new_seq.get_absolute_url())
  else:
       form = InputForm()
  return render_to_response('app/input_form.html',
                             { 'form': form },
                             context_instance=RequestContext(request))

def seq_process(request, object_id):
  """This view processess the sequence and renders it's different representations for the input sequence.
  """
  
  seq_entity = get_object_or_404(Sequence, pk=object_id)
  mat_str = seq_entity.mat.strip('[]')
  matrix = [int(x) for x in mat_str.split(',')] 
  seq_list = list(seq_entity.raw_seq)

  mat_out = []
  length = seq_entity.length
  index = 0
  for i in range(0,len(matrix)):
     if i%length == 0:
        mat_out.append(seq_list[index])
        index = index+1
        mat_out.append(matrix[i])
     else:
        mat_out.append(matrix[i])
  print seq_entity.output_seq

  return render_to_response('app/seq_detail.html',
                              { 'title': seq_entity.title, 
                                'seq': seq_entity.raw_seq,
                                'out_seq': seq_entity.bracketed_str,
                                'mat': mat_out,
                                'length': seq_entity.length+1,
                                'seq_list': seq_list,
                                'graph': seq_entity.graph_svg }, 
                                context_instance=RequestContext(request))

def home(request):
  return render_to_response('base.html')
