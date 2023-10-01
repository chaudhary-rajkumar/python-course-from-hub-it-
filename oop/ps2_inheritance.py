class Youtube:
    def __init__(self,like,comment,dislike):
        self.like=like 
        self.comment=comment
        self.dislike=dislike
    def y_detail(self):
        print(f"In Youtube your total like {self.like} is your total comment {self.comment} is and your total dislike is {self.dislike} ")


class facebook:
    def __init__(self,photo,video,friends):
        self.photo=photo
        self.video=video
        self.friends=friends
    def f_detail(self):
        print(f"your total {self.photo} and total video is {self.video} and total friends is {self.friends}")


class tiktok(Youtube,facebook):
    def __init__(self, like, comment, dislike , photo , video , friends , followers , views):
        Youtube.__init__(self,like, comment,dislike )
        facebook.__init__(self, photo , video , friends )
        self.followers=followers
        self.views=views

    def t_detail(self):
        print(f"In Youtube your total like {self.like} is your total comment {self.comment} is and your total dislike is {self.dislike} your total {self.photo} and total video is {self.video} and total friends is {self.friends} and your total followers is {self.followers} and total views in your video is {self.views}")

obj=tiktok('200k','40k','4k','500','888','4k','10k','2m')
obj.t_detail()

