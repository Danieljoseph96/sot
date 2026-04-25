from django.db import models
from django.contrib.auth.models import User


class UserReg(models.Model):
    sl_no = models.AutoField(primary_key=True)

    name = models.CharField(max_length=255)
    bs = models.CharField(max_length=20, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)

    locality = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=100, blank=True, null=True)

    extra_stay = models.CharField(max_length=100, blank=True, null=True)
    details = models.TextField(blank=True, null=True)

    acc = models.CharField(max_length=100, blank=True, null=True)
    acc_room = models.CharField(max_length=100, blank=True, null=True)

    extra_stay_30th = models.CharField(max_length=100, blank=True, null=True)
    extra_stay_3rd = models.CharField(max_length=100, blank=True, null=True)

    transport = models.CharField(max_length=100, blank=True, null=True)

    arrival_train_no = models.CharField(max_length=50, blank=True, null=True)
    arrival_station = models.CharField(max_length=100, blank=True, null=True)
    arrival_date = models.DateField(blank=True, null=True)
    arrival_time = models.TimeField(blank=True, null=True)

    departure_train_no = models.CharField(max_length=50, blank=True, null=True)
    departure_station = models.CharField(max_length=100, blank=True, null=True)
    departure_date = models.DateField(blank=True, null=True)
    departure_time = models.TimeField(blank=True, null=True)

    received_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    registration_balance_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    extra_stay_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    balance_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    remarks = models.TextField(blank=True, null=True)
    bus_no = models.CharField(max_length=50, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user_registration"
        ordering = ['sl_no']

    def __str__(self):
        return self.name


class LocalityWise(models.Model):

    PAYMENT_CHOICES = [
        ('cash', 'Cash'),
        ('upi', 'UPI'),
        ('bank', 'Bank Transfer'),
        ('pending', 'Pending'),
    ]

    locality = models.CharField(max_length=255, unique=True)
    state = models.CharField(max_length=255, blank=True, null=True)
   

    persons_count = models.PositiveIntegerField(default=0)

    total_paid = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_CHOICES,
        default='pending'
    )

    remarks = models.TextField(blank=True, null=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "locality_summary"
        ordering = ['locality']

    def __str__(self):
        return self.locality


class UserProfile(models.Model):

    USER_TYPES = [
        ('admin', 'Admin'),
        ('regular', 'Regular'),
        ('staff', 'Staff'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPES,
        default='regular'
    )

    def __str__(self):
        return self.user.username
    

