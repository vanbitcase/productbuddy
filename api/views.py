from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer
import joblib
import pandas as pd
from scipy.sparse import load_npz
from sklearn.metrics.pairwise import cosine_similarity
from django.conf import settings
import os

# Load recommend system assets once
VECTORIZER_PATH = os.path.join(settings.BASE_DIR, 'tfidf_vectorizer.pkl')
MATRIX_PATH = os.path.join(settings.BASE_DIR, 'tfidf_matrix.npz')
PRODUCTS_PATH = os.path.join(settings.BASE_DIR, 'products.csv')

vectorizer = joblib.load(VECTORIZER_PATH)
tfidf_matrix = load_npz(MATRIX_PATH)
df_products = pd.read_csv(PRODUCTS_PATH)
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def get_recommendations_partial(query, df, cosine_sim, top_n=3):
    matches = df[df['name'].str.lower().str.contains(query.lower())]
    if matches.empty:
        return []
    idx = matches.index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_products = sim_scores[1:top_n+1]
    return df.iloc[[i[0] for i in top_products]][['name']].name.to_json()

# Create your views here.

@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def order_list(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def order_detail(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def recommend_products(request):
    query = request.GET.get('query', '')
    if not query:
        return Response({'error': 'Query parameter is required.'})
    recommendations = get_recommendations_partial(query, df_products, cosine_sim, top_n=6)
    if not recommendations:
        return Response({'recommendations': [], 'message': f'No products found for "{query}".'})
    return Response({'recommendations': recommendations})
