<!-- # Checking if a object exists on save in Django -->
<!-- Published: 2016-06-01 -->

Having used integer primary keys for many projects, I've only recently switched over to using UUIDs on a few projects about a little less than a year ago. In the switch, an old solution I've often used for checking if an object exists, or is being created, has become obsolete.

A typical solution for checking if an object is being created in the `save` method is usually to check if `self.pk` is `None` as such:

**This isn't always true (see below)**
```python
class Parrot(UUIDModel):
    is_loud = models.BooleanField(default=True)
    ...

    def save(self, *args, **kwargs):
        if self.pk is None:
            do_some_stuff()
        super(Parrot, self).save(*args, **kwargs)
```

## The problem

The issue with the above solution is that we are relying on a "hack" that utilizes [Django's cached attributes](https://docs.djangoproject.com/en/1.9/topics/db/optimization/#understand-cached-attributes), that checks to see if the primary key is `None`. This will certainly fail if you're using UUIDs or any primary key that sets the `default` parameter on the field.

Ex:
```python
import uuid


class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    ...

    class Meta:
        abstract = True
```

## Solutions

1. One solution would be to add a `created` timestamp field to the model and check `if created is not None` instead.
But this is potentially the same issue as above if a `default` value is ever set on the `created` field.

2. Another solution would be to perform a query to check if the object exists.
Ex:
```python
class Parrot(UUIDModel):
    is_loud = models.BooleanField(default=True)
    ...

    def save(self, *args, **kwargs):
        try:
            parrot = Parrot.objects.get(id=parrot.pk)
        except Parrot.DoesNotExist:
            parrot = None
        if parrot is None:
            do_some_stuff()
        super(Parrot, self).save(*args, **kwargs)
```
The downside with this solution is that you are now performing an extra query just to check if the object exists. But barring any possible race condition situations or `n+1` query scenario, this is probably your best bet for checking if the object exists.

If anyone else has a solution feel free to contact me, I'd love to hear your thoughts.


### Sources:
* [Stack Overflow Answer highlighting the partially correct solution](http://stackoverflow.com/questions/907695/in-a-django-model-custom-save-method-how-should-you-identify-a-new-object/907703#907703)

* [Stack Overflow Answer highlighting the issue with using `self.pk is None`](http://stackoverflow.com/questions/907695/in-a-django-model-custom-save-method-how-should-you-identify-a-new-object/940928#940928)