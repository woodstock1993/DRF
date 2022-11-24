# DRF를 활용한 CRUD

## APIView 
- 게시글 작성과 관련한 CRUD를 APIView를 상속 받아 구현하였습니다.

## GenericAPIView
- 게시글 작성과 관련한 CRUD를 generics.GenericAPIView를 상속 받아 구현하였습니다.

## mixins
- 게시글과 관련한 CRUD를 [mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView], [mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView]를 상속받아 구현하였습니다.

## generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView
- 게시글과 관련한 CRUD를 위 두개를 상속받아 구현하였습니다.

## viewsets
- 게시글과 관련한 CRUD를 viewsets.ModelViewSet을 상속받아 구현하였습니다.
