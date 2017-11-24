from haystack import indexes
from .models import Post

class PostIndex(indexes.SearchIndex, indexes.Indexable):
    """Create a customm SearchIndex for the Post model. Haystack will know which
    data from this model has to be indexed in the search engine."""
    text = indexes.CharField(document=True, use_template=True)
    publish =  indexes.DateTimeField(model_attr='publish')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().published.all()
