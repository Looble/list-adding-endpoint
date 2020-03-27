from rest_framework import serializers


class NumberSumSerializer(serializers.Serializer):
    """
    Serializer that returns the total of a list of numbers
    """

    class Meta:
        fields = ("total")
    # SerializerMethodField is a custom field not defined by a model, this looks for the function "get_[field name]"
    total = serializers.SerializerMethodField()

    def get_total(self, obj):
        """
        Calculate the total of a list of numbers
        """
        numbers_to_add = list(range(10000001)) #TODO Replace with link to actual framework
        # Take each number in the list and add them to a total. Then return the total.
        total = 0
        for number in numbers_to_add:
            total += number
        return total
