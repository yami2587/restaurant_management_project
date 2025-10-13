from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import Coupon
from .serializers import CouponSerializer

class CouponValidationView(APIView):
    def post(self, request):
        code = request.data.get('code')

        if not code:
            return Response({"error": "Coupon code is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            coupon = Coupon.objects.get(code__iexact=code)  # case-insensitive match
        except Coupon.DoesNotExist:
            return Response({"error": "Invalid coupon code."}, status=status.HTTP_400_BAD_REQUEST)

        today = timezone.now().date()
        if not coupon.is_active:
            return Response({"error": "This coupon is not active."}, status=status.HTTP_400_BAD_REQUEST)
        if not (coupon.valid_from <= today <= coupon.valid_until):
            return Response({"error": "This coupon is expired or not yet valid."}, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "success": True,
            "code": coupon.code,
            "discount_percentage": float(coupon.discount_percentage),
            "message": f"Coupon '{coupon.code}' is valid and gives {coupon.discount_percentage}% off!"
        }, status=status.HTTP_200_OK)
