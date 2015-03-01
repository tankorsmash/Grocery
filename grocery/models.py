from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return u"%s" % self.name

    def __repr__(self):
        return u"<Company: %s>" % unicode(self)

class Store(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    company = models.ForeignKey(Company, related_name="stores")

    def __unicode__(self):
        return u"%s" % self.name

    def __repr__(self):
        return u"<Store: %s>" % unicode(self)

class Aisle(models.Model):
    name = models.CharField(max_length=255)

    store = models.ForeignKey(Store, related_name="aisles")
    def __unicode__(self):
        return u"%s" % self.name

    def __repr__(self):
        return u"<Aisle: %s>" % unicode(self)


class FoodItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    cost = models.IntegerField()

    aisle = models.ForeignKey(Aisle, related_name="food_items")

    def __unicode__(self):
        return u"%s" % self.name

    def __repr__(self):
        return u"<FoodItem: %s>" % unicode(self)

