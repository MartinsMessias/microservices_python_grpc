import grpc
import random
from concurrent import futures
from recommendations_pb2 import (
    MovieCategory,
    MovieRecommendation,
    RecommendationResponse
)
import recommendations_pb2_grpc

movies_by_category = {
    MovieCategory.ACTION: [
        MovieRecommendation(id=1, title='Mad Max: Fury Road'),
        MovieRecommendation(id=2, title='Die Hard'),
        MovieRecommendation(id=3, title='John Wick'),
    ],
    MovieCategory.COMEDY: [
        MovieRecommendation(id=4, title='Dumb & Dumber'),
        MovieRecommendation(id=5, title='Four Lions'),
        MovieRecommendation(id=6, title='Ghostbusters'),
    ],
    MovieCategory.HORROR: [
        MovieRecommendation(id=7, title='The Exorcist'),
        MovieRecommendation(id=8, title='Psycho'),
        MovieRecommendation(id=9, title='Poltergeist'),
    ],
    MovieCategory.SCIENCE_FICTION: [
        MovieRecommendation(id=10, title='Star Wars'),
        MovieRecommendation(id=11, title='Back to The Future'),
        MovieRecommendation(id=12, title='Interstellar'),
    ]
}


class RecommendationService(
    recommendations_pb2_grpc.RecommendationsServicer
):
    def Recommend(self, request, context):
        if request.category not in movies_by_category:
            context.abort(grpc.StatusCode.NOT_FOUND, "Category not found")

        movies_for_category = movies_by_category[request.category]
        num_results = min(request.max_results, len(movies_for_category))
        movies_to_recommend = random.sample(
            movies_for_category, num_results
        )

        return RecommendationResponse(recommendations=movies_to_recommend)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    recommendations_pb2_grpc.add_RecommendationsServicer_to_server(
        RecommendationService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
