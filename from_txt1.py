import xlwt
filed = []
all_good_id={}
error_list=[]
str1="good_id:199071307, good_url:https://www.etsy.com/listing/199071307/locket-silver-photo-locket-filigree?ref=shop_review, pic:https://img.etsystatic.com/il/30b5cc/637131530/il_fullxfull.637131530_ftc6.jpg, title:Locket; Silver Photo Locket; Filigree Round Pendants  27mm Set of 5 pcs A7147, price_now:USD 3.99, reviews:21086.0, favorites:95.0, shop_name:VeryCharms, shop_url:https://www.etsy.com/shop/VeryCharms?ref=l2-shopheader-name, descriptions:    You&#39;ll receive 5 pcs of silver photo lockets.;;Very nice looking and high quality.;;Size: 27mm;Base metal: brass;;All our items are NICKEL FREE and LEAD FREE.;;Please feel free to convo me for other quantity.;;Check out my other items as we&#39;re adding new items everyday. \n"
for i in str1.split(","):
    print(i)
    con = i.split(":", 1)[1]
    filed.append(con)
print(filed)






