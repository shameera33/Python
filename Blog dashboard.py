blog_views = [150, 800, 2500, 600, 1200, 450, 3000]
Total_trending = 0
for views in blog_views:
    if views > 1000:
        print("Trending")
        Total_trending +=1
    elif views>=500 and views<=1000:
        print("Average")
    else:
        print("low traffic")

print("Total no of views:", sum(blog_views))
print("total trending post:", Total_trending)