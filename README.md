# django-num2word
Django app which obtains by specified url a number and changes it in response to json words

*urls.py*

```
urlpatterns = patterns('',
    ...
    url(r'^num2words/', include('num2word.urls')),
    ...
)
```
*usage*

```
http://example.com/num2words/float_number/lang_code/
http://example.com/num2words/float_number/
```

*example*

```
http://example.com/num2words/-3231.3454/de/
http://xample.com/num2words/3231.3454/
```

*supported languages*

```
en - default
en_GB 
en_IN
fr
de
es
lt
lv
```
