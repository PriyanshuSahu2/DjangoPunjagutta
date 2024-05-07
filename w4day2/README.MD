## Creating models[Tables] to Store The Data

step 1) create an app and register it

step 2) in app there is file models.py open the file

step 3) create a class ,that class need to inherit from models.Model class

    class Student(models.Model):
    		pass

step 4) create required columns[fields ] inside the created class as
variables

    class Student(models.Model):
    		# colName= models.FieldName()
    		name=models.CharField(max_length=25)
    		age=models.IntegerField()
    		address=models.CharField(max_length=25)

step 5) now generated python need to be converted as SQL code by using
command
python manage.py makemigrations

note to see sql code:
python manage.py sqlmigrate appName 0001

step 6) the generated sql code neeed to executed as Query so to do that
give migrate command

    python manage.py mig







FIELDS
--------------------
Field Name Description
-------------------------
AutoField()
----------
 It An IntegerField that automatically increments.

BinaryField:
-------------
 A field to store raw binary data.

BooleanField:
-----------------
A true/false field.
The default form widget for this field is a CheckboxInput.

CharField
------------
 A field to store text based values.


DateField
------------
A date, represented in Python by a datetime. date instance
it is used for date and time, represented in Python by a 
datetime.datetime instance.


EmailField:
---------------
It is a CharField that checks that the value is a valid email 
address.

FileField 
----------------
It is a file-upload field.


FloatField
-----------------
It is a floating-point number represented in Python by a float instance.

ImageField:
----------------
It inherits all attributes and methods from FileField, but also validates that the uploaded object is a valid image.

IntegerField:
------------
It is an integer field. Values from -2147483648 to 
2147483647 are safe in all databases supported by 
Relationship Fields
Django also defines a set of fields that represent relations.Field Name Description

ForeignKey:
----------------
A many-to-one relationship. Requires two positional arguments: the 
class to which the model is related and the on_delete option.

ManyToManyField:
--------------------
A many-to-many relationship. Requires a positional argument: the 
class to which the model is related, which works exactly the same as it 
does for ForeignKey, including recursive and lazy relationships.

OneToOneField:
-----------------
A one-to-one relationship. Conceptually, this is similar to a 
ForeignKey with unique=True, but the ―reverse‖ side of the relation 
will directly return a single object.