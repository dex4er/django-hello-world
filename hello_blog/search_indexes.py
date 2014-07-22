from haystack import indexes


from hello_blog.models import Note

class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, template_name='search/indexes/note.txt')
    user = indexes.CharField(model_attr='user')
    category = indexes.CharField(model_attr='category')
    keywords = indexes.MultiValueField()
    title = indexes.CharField(model_attr='title')
    date = indexes.DateTimeField(model_attr='date')

    def get_model(self):
        return Note

    def prepare_keywords(self, obj):
        return obj.keywords.split(", ")

    def get_updated_field(self):
        return 'date'


from hello_blog.models import Category

class CategoryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, template_name='search/indexes/category.txt')

    def get_model(self):
        return Category


from django.contrib.auth.models import User

class UserIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, template_name='search/indexes/user.txt')

    def get_model(self):
        return User


from whoosh.analysis.analyzers import StemmingAnalyzer

def Analyzer():
    return StemmingAnalyzer()
