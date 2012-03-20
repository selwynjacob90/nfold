""" Module containing views for the app.
"""

__author__ = 'Selwyn Jacob <selwynjacob90@gmail.com>'

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
      exclude = ['output_seq', 'bracketed_str', 'graph_svg']

@csrf_exempt
def RnaInput(request):
  """This view generates the input form and creates the requires represntations
     with the help of logic module and save the seuence to the database.
  """
  if request.method == 'POST':
     form = InputForm(request.POST)
     if form.is_valid():
       new_seq = form.save(commit=False)
       input_seq = form.cleaned_data['raw_seq']
       
       # Build nussinov sequence 
       sequence = buildSequence(input_seq.encode('ascii', 'ignore')) 
       new_seq.output_seq = sequence
       
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

def DisplayRepresentations(request, object_id):
  """This view displays the different representations for the input sequence.
  """
  seq_entity = get_object_or_404(Sequence, pk=object_id)
  return render_to_response('app/representations.html',
                              { 'title': seq_entity.title,
                                'seq': seq_entity.raw_seq,
                                'out_seq': seq_entity.bracketed_str,
                                'graph': seq_entity.graph_svg },
                              context_instance=RequestContext(request))

