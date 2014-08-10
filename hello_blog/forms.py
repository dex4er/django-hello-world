from django import forms
from haystack.forms import HighlightedModelSearchForm
from haystack.inputs import Raw, Clean
from haystack.query import SearchQuerySet

class BlogSearchForm(HighlightedModelSearchForm):
    operator = forms.ChoiceField(choices=(('AND', 'AND'),('OR', 'OR'),))

    def search(self):
        sqs = SearchQuerySet().filter(content=Raw(Clean((' %s ' % self.cleaned_data['operator']).join(self.cleaned_data['q'].split(' ')))))
        print(unicode(sqs.query))
        if self.cleaned_data['models']:
            sqs = sqs.models(*self.get_models())
        return sqs
