from rest_framework import serializers
from .models import Sales,Stakeholder,Customer,SalesLineItems,Product,SalesFooter,ShippingInformation
class SalesLineItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesLineItems
        fields = '__all__'

class SalesFooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesFooter
        fields = '__all__'

class ShippingInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingInformation
        fields = '__all__'

class SalesSerializer(serializers.ModelSerializer):
    line_items = SalesLineItemsSerializer(many=True)
    footer = SalesFooterSerializer(required=False)
    shipping_information = ShippingInformationSerializer()

    class Meta:
        model = Sales
        fields = '__all__'
