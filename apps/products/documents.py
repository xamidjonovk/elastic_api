from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl import analyzer
from .models import Product
from elasticsearch_dsl import analysis, tokenizer

html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)
ngram_tokenizer = tokenizer('ngram_tokenizer', type='ngram', min_gram=3, max_gram=3)
ngram_analyzer = analysis.analyzer('ngram_analyzer', tokenizer=ngram_tokenizer, filter=['lowercase'])


@registry.register_document
class ProductDocument(Document):
    name = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.KeywordField(),
            'ngram': fields.TextField(analyzer=ngram_analyzer),  # N-gram field for partial matches
        }
    )
    description = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
            'ngram': fields.TextField(analyzer=ngram_analyzer),  # N-gram field for partial matches
        }
    )

    class Index:
        name = 'products'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
            'analysis': {
                'tokenizer': {
                    'ngram_tokenizer': ngram_tokenizer.to_dict(),
                },
                'analyzer': {
                    'ngram_analyzer': ngram_analyzer.to_dict(),
                },
            },
        }

    class Django:
        model = Product
        fields = [
            'id',
            'product_type',
            'size',
        ]
