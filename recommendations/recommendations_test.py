from recommendations import RecommendationsService
from recommendations_pb2 import MoviesCategory, RecommendationRequest


def test_recommendations():
    service = RecommendationsService()
    request = RecommendationRequest(
        user_id=1, category=MoviesCategory.ACTION, max_results=1
    )
    response = service.Recommend(request, None)
    assert len(response.recommendations) == 1
