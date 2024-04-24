# views.py
# views.py
from urllib import request
from httpcore import Response

from rest_framework.views import APIView
from rest_framework.response import Response
import redis
from rest_framework import status
from .serializers import AuthorSerializer, BookSerializer



class AuthorAPI(APIView):
    def get(self,request):
        redis_client = redis.Redis(host='localhost',port='6379',db=0)
        author_data = redis_client.hgetall('author')
        author_data_decoded = {key.decode('utf-8'): value.decode('utf-8') for key, value in author_data.items()}
        return Response(
            {
                'author':author_data_decoded,
            }
        )
    
    
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            number = serializer.validated_data.get('number')
            domicile = serializer.validated_data.get('domicile')
            family_name = serializer.validated_data.get('family_name')
            
            # Save data to Redis using HMSET
            redis_client = redis.Redis(host='localhost', port='6379', db=0)
            author_data = {
                'name': name,
                'number': number,
                'domicile': domicile,
                'family_name': family_name
            }
            redis_client.hmset('author', author_data)
            
            return Response({"message": "Author data saved successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class BookAPI(APIView):
    def get(self,request):
        redis_client = redis.Redis(host='localhost',port='6379',db=0)
        author_data = redis_client.hgetall('book')
        author_data_decoded = {key.decode('utf-8'): value.decode('utf-8') for key, value in author_data.items()}
        return Response(
            {
                'book':author_data_decoded,
            }
        )
    
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            number = serializer.validated_data.get('number')
            price = serializer.validated_data.get('price')
            title = serializer.validated_data.get('title')
            tu
            # Save data to Redis using HMSET
            redis_client = redis.Redis(host='localhost', port='6379', db=0)
            author_data = {
                'number': number,
                'price': price,
                'title': title,
            }
            redis_client.hmset('book', author_data)
            
            return Response({"message": "Book data saved successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   





class RelationAPI(APIView):             
    def get(self,request):
        redis_client = redis.Redis(host='localhost',port='6379',db=0)
        # author_data = redis_client.hget('author','name')
        # book_data = redis_client.hget('book','title')
        relation_data = redis_client.hgetall('relation')
        relation_data_decoded = {key.decode('utf-8'): value.decode('utf-8') for key, value in relation_data.items()}
        return Response(
            {
                # 'name_author':author_data,
                # 'title_book':book_data,
                'relation_data':relation_data_decoded
            }
        )
    
    def post(self,request):
        redis_client = redis.Redis(host='localhost',port='6379',db=0)
        author_name = redis_client.hget('author', 'name')
        book_title = redis_client.hget('book', 'title')

        if author_name and book_title:
            relation_data = {
                'name': author_name,
                'title': book_title,
            }
            redis_client.hmset('relation', relation_data)
            return Response({"message": "Relation data saved successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Failed to create relation. Author name or book title not found."}, status=status.HTTP_400_BAD_REQUEST)