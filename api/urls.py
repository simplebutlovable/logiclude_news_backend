from django.urls import path

from api.views import ( 
                        LatestNewsView,
                        NewsView, 
                        TopOfTheWeekView,
                        NewsDetails, 
                        CategorizedNewsView,
                        ScienceLatestView,
                        ReadMoreView,
                        AlsoReadNewsView,
                        TrendingNewsView,
                        EditorsPickView,
                        TabLatestNewsView,
                        TabTopNewsView,
                        OtherNewsView,
                        TabBotNewsView,
                    )

app_name = "api"

urlpatterns = [
    path("news/latest/<int:rank>/", LatestNewsView.as_view(), name="LatestNews"),
    path("news/trending/", TrendingNewsView.as_view(), name="RandomNews"),
    path("news/topoftheweek/", TopOfTheWeekView.as_view(), name="TopOfTheWeek"),   
    path("news/editorspick/", EditorsPickView.as_view(), name="EditorsPick"),
    path("news/category/<str:category>/", CategorizedNewsView.as_view(), name="CategorizedNews"),
    path("news/alsoread/<str:category>/<int:index>/", AlsoReadNewsView.as_view(), name="AlsoReadNews"),
    path("news/readmore/<str:category>/<int:index>/", ReadMoreView.as_view(), name="ReadMore"),
     # Tabs
    path("news/<str:category>/latest/", TabLatestNewsView.as_view(), name="TabLatest"),
    path("news/<str:category>/top/", TabTopNewsView.as_view(), name="TabTopNews"),
    path("news/<str:category>/othernews/", OtherNewsView.as_view(), name="OtherNews"),
    path("news/<str:category>/tabbotnews/", TabBotNewsView.as_view(), name="TabBotNews"),


    path("news/<int:index>/", NewsView.as_view(), name="NewsView"),
    path("news/details/<int:pk>/", NewsDetails.as_view(), name="NewsDetails"),
    
   
    path("news/science/latest/", ScienceLatestView.as_view(), name="ScienceLatest"),
   
    
   
]