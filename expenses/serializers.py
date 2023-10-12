from rest_framework import serializers
from .models import Expense, ExpenseLineItem

class ExpenseLineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseLineItem
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    line_items = ExpenseLineItemSerializer(many=True)

    class Meta:
        model = Expense
        fields = ('expense_id', 'user_id', 'date', 'note', 'line_items')  # add other fields as needed
