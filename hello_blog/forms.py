from haystack.forms import HighlightedModelSearchForm

class BlogSearchForm(HighlightedModelSearchForm):
    def search(self):
        qs = super(BlogSearchForm, self).search()
        return qs
