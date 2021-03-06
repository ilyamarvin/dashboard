# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse


class Ads(models.Model):
    id_ad = models.AutoField(primary_key=True)
    id_category = models.ForeignKey('Categories', models.PROTECT, db_column='id_category')
    id_subcategory = models.ForeignKey('Subcategories', models.PROTECT, db_column='id_subcategory')
    id_location = models.ForeignKey('Locations', models.PROTECT, db_column='id_location')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    link_to_photos = models.TextField(blank=True, null=True)
    id_user = models.ForeignKey('Users', models.PROTECT, db_column='id_user')
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ads'

    
    def __str__(self):
        return self.name

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.PROTECT)
    permission = models.ForeignKey('AuthPermission', models.PROTECT)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.PROTECT)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.PROTECT)
    group = models.ForeignKey(AuthGroup, models.PROTECT)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.PROTECT)
    permission = models.ForeignKey(AuthPermission, models.PROTECT)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categories(models.Model):
    id_category = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.PROTECT, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.PROTECT)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Locations(models.Model):
    id_location = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'locations'

    def __str__(self):
        return self.name


class Positions(models.Model):
    id_position = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'positions'

    def __str__(self):
        return self.name


class ReviewsOnUser(models.Model):
    id_review = models.AutoField(primary_key=True)
    id_ad = models.ForeignKey(Ads, models.PROTECT, db_column='id_ad')
    review_text = models.TextField(blank=True, null=True)
    rating = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'reviews_on_user'


class Subcategories(models.Model):
    id_subcategory = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'subcategories'

    def __str__(self):
        return self.name


class Users(models.Model):
    id_user = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    secondname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telephone_number = models.IntegerField()
    birth_date = models.DateField()
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'users'
    
    def __str__(self):
        return self.username

class Workers(models.Model):
    id_worker = models.AutoField(primary_key=True)
    id_position = models.ForeignKey(Positions, models.PROTECT, db_column='id_position')
    first_day_work = models.DateField()
    last_day_work = models.DateField(blank=True, null=True)
    id_user = models.ForeignKey(Users, models.PROTECT, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'workers'
