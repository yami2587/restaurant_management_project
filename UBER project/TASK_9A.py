# ride/serializers.py
from rest_framework import serializers
from ride.models import Ride, RideFeedback

class RideFeedbackSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=1, max_value=5)
    comment = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = RideFeedback
        fields = ['rating', 'comment']

    def validate(self, data):
        request = self.context['request']
        user = request.user
        ride = self.context.get('ride')   # pass ride via context in view

        # ✅ Ride must exist and be completed
        if not ride or ride.status != "COMPLETED":
            raise serializers.ValidationError("Ride is not completed yet.")

        # ✅ Check if user is rider or driver of this ride
        if ride.rider != user and ride.driver != user:
            raise serializers.ValidationError("You are not part of this ride.")

        # ✅ Prevent duplicate feedback
        if RideFeedback.objects.filter(ride=ride, submitted_by=user).exists():
            raise serializers.ValidationError("Feedback already submitted.")

        return data

    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        ride = self.context.get('ride')

        # ✅ Identify if feedback is from driver or rider
        is_driver = True if ride.driver == user else False

        feedback = RideFeedback.objects.create(
            ride=ride,
            submitted_by=user,
            rating=validated_data['rating'],
            comment=validated_data.get('comment', ''),
            is_driver=is_driver
        )
        return feedback
