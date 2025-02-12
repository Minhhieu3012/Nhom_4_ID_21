from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from .models import Feedback

@csrf_exempt  # Tắt CSRF (nếu cần)
@require_POST  # Chỉ cho phép phương thức POST
def submit_feedback(request):
    try:
        data = json.loads(request.body)
        name = data.get("name")
        email = data.get("email")
        rating = data.get("rating")
        message = data.get("message")

        if not name or not email or not rating or not message:
            return JsonResponse({"error": "Vui lòng nhập đầy đủ thông tin!"}, status=400)

        Feedback.objects.create(name=name, email=email, rating=rating, message=message)
        return JsonResponse({"message": "Phản hồi đã được gửi!"}, status=201)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Dữ liệu không hợp lệ!"}, status=400)

def get_feedback_list(request):
    feedbacks = Feedback.objects.all().values("name", "rating", "message", "created_at")
    return JsonResponse(list(feedbacks), safe=False)