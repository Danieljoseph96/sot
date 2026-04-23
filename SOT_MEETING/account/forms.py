from django import forms
from .models import UserReg, LocalityWise


class LocalityWiseForm(forms.ModelForm):
    class Meta:
        model = LocalityWise
        fields = "__all__"


class LocalityRegisterForm(LocalityWiseForm):
    locality = forms.ChoiceField(choices=(), required=True)

    class Meta(LocalityWiseForm.Meta):
        model = LocalityWise
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        paid_localities = set(
            LocalityWise.objects.filter(total_balance=0)
            .values_list("locality", flat=True)
        )
        locality_choices = [("", "Select locality")]
        locality_choices.extend(
            [
                (locality, locality)
                for locality in UserReg.objects.exclude(locality__isnull=True)
                .exclude(locality="")
                .exclude(locality__in=paid_localities)
                .order_by("locality")
                .values_list("locality", flat=True)
                .distinct()
            ]
        )

        selected_locality = ""
        if self.is_bound:
            selected_locality = str(self.data.get("locality", "")).strip()
        else:
            selected_locality = str(self.initial.get("locality", "")).strip()
        if selected_locality and selected_locality not in {choice[0] for choice in locality_choices}:
            locality_choices.append((selected_locality, selected_locality))

        self.fields["locality"].choices = locality_choices

        readonly_fields = ("state", "persons_count", "total_balance")
        for field_name in readonly_fields:
            if field_name in self.fields:
                self.fields[field_name].widget.attrs["readonly"] = "readonly"

        for field in self.fields.values():
            existing_class = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = (existing_class + " form-control").strip()

        if "payment_method" in self.fields:
            self.fields["payment_method"].widget.attrs["class"] = "form-select"


class UserRegForm(forms.ModelForm):
    class Meta:
        model = UserReg
        fields = "__all__"  
        
