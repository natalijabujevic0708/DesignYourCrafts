## Information Architecture
### Database 
During the development phase the **sqlite3** database was used which is installed with Django.   
For deployment(production), a **PostgreSQL** database is provided by Heroku as an add-on.
- The **User model** used in this project is provided by Django as a part of defaults `django.contrib.auth.models`. More information about Django’s authentication system can be found [here](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/).
## Data Modelling
<p>&nbsp</p>   

### Profiles App
#### User Profile
| **Name** | **Database Key** | **Field Type** | **Arguments** |
--- | --- | --- | --- 
 User | user | OneToOneField 'User' |  on_delete=models.CASCADE
 Phone number | default_phone_number | CharField | max_length=20, null=True, blank=True
 Address Line1 | default_street_address1 | CharField | max_length=80, null=True, blank=True
 Address Line2 | default_street_address2 | CharField | max_length=80, null=True, blank=True
 Town/City | default_town_or_city | CharField | max_length=40, null=True, blank=True
 County | default_county | CharField | max_length=80, null=True, blank=True
 Postcode | default_postcode | CharField | max_length=20, null=True, blank=True
 Country | default_country | CountryField | blank_label='Country', null=True, blank=True
<p>&nbsp</p>   

### Products App
#### Product
| **Name** | **Database Key** | **Field Type** | **Arguments** |
--- | --- | --- | --- 
 Category | category | ForeignKey 'Category' | null=True, on_delete=models.SET_NULL
 Sku | sku | CharField | max_length=254, null=True, blank=True
 Name | name | CharField | max_length=254 
 Description | description | TextField
 Price | price | DecimalField | max_digits=6, decimal_places=2
 Image | image| ImageField | null=True
 Lock Image | image_lock| ImageField | null=True, blank=True
 Svg Path | svg_path | CharField |  max_length=1000, null=True
 Svg Id | svg_id | CharField | max_length=254, null=True
 Top Svg Path | top_svg_path | CharField | max_length=1000, null=True
 Top Svg Id | top_svg_id | CharField | max_length=254, null=True
 Bottom Svg Path | bottom_svg_path | CharField | max_length=1000, null=True
 Bottom Svg Id | bottom_svg_id | CharField | max_length=254, null=True
 Svg Width | svg_width | CharField |  max_length=1000
 Svg Height | svg_height | CharField |  max_length=1000
 Icon | icon | ForeignKey 'Icon' | null=True, on_delete=models.SET_NULL
<p>&nbsp</p>   

#### Category
| **Name** | **Database Key** | **Field Type** | **Arguments** |
--- | --- | --- | --- 
Name | name | CharField | max_length=254
Friendly Name | friendly_name | CharField | max_length=254, null=True, blank=True
Category Image| category_image | ImageField | null=True
<p>&nbsp</p>   

#### Icon
| **Name** | **Database Key** | **Field Type** | **Arguments** |
--- | --- | --- | --- 
Full Icon | icon_full | ImageField | null=True
Top Icon | icon_top | ImageField | null=True
Bottom Icon | icon_bottom | ImageField | null=True
<p>&nbsp</p>   

#### Decoration
| **Name** | **Database Key** | **Field Type** | **Arguments** |
--- | --- | --- | --- 
Name | name | CharField | max_length=254, null=True, blank=True
Decoration image | decoration_image | ImageField | null=True
<p>&nbsp</p>   

#### Pattern
| **Name** | **Database Key** | **Field Type** | **Arguments** |
--- | --- | --- | --- 
Name | name | CharField | max_length=254, null=True, blank=True
Href | href |  CharField | max_length=1000, null=True
<p>&nbsp</p>   

### Checkout App
#### Order
| **Name** | **Database Key** | **Field Type** | **Arguments** |
--- | --- | --- | --- 
Order Number | order_number | CharField | max_length=32, null=False, editable=False
Profile | user_profile | ForeignKey 'UserProfile' | on_delete=models.SET_NULL, null=True, blank=True, related_name='orders'
Full Name | full_name | CharField | max_length=50, null=False, blank=False                                  
Email | email | EmailField | max_length=254, null=False, blank=False
Phone number | phone_number | CharField | max_length=20, null=False, blank=False  
Country | country | CountryField | blank_label='Country *', null=False, blank=False    
Postcode | postcode | CharField | max_length=20, null=True, blank=True
Town/City | town_or_city | CharField | max_length=40, null=False, blank=False
Street Address1 | street_address1 | CharField | max_length=80, null=False, blank=False
Street Address2 | street_address2 | CharField | max_length=80, null=True, blank=True
County | county | CharField | max_length=80, null=True, blank=True
Purchase Date | date | DateTimeField | auto_now_add=True
Delivery Cost | delivery_cost | DecimalField | max_digits=6, decimal_places=2, null=False, default=0
Order Total | order_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0
Grand Total | grand_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0
Original Bag | original_bag | TextField | null=False, blank=False, default=''
Stripe Pid | stripe_pid | CharField | max_length=254, null=False, blank=False, default=''
Design | design | TextField | null=False, blank=False, default=""
<p>&nbsp</p>   

#### Order Item Details 
| **Name** | **Database Key** | **Field Type** | **Arguments** |
--- | --- | --- | --- 
Order | order | ForeignKey 'Order' | null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems'
Product | product | ForeignKey 'Product' | null=False, blank=False, on_delete=models.CASCADE
Quantity | quantity | IntegerField | null=False, blank=False, default=0
Item Total | lineitem_total | DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False




