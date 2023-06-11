from modules.peewee import *
db = SqliteDatabase('db.sqlite3')

class BaseModel(Model):
    class Meta:
        database = db

class Inventory_Invoice(BaseModel):
    customer = CharField()
    date = DateTimeField()
    amount = IntegerField()                 

class Inventory_Product(BaseModel): 
    name = CharField()
    description = CharField()
    price = IntegerField(default=0)

class Inventory_InvoiceItem(BaseModel):
    invoice = ForeignKeyField(Inventory_Invoice,backref='invoice_invoiceitems')
    product = ForeignKeyField(Inventory_Product,backref='product_invoiceitems')
    quantity = IntegerField()

def create_tables_if_not_exist():
    if not Inventory_Product.table_exists():
        db.create_tables([Inventory_Invoice, Inventory_Product, Inventory_InvoiceItem])